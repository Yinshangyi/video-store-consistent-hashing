import pytest

from src.exception.server_name_error import ServerNameNotFoundError
from src.repository.server_manager import ServerManager
from src.repository.video_repository import VideoRepository
from test.test_utils import *


def init_video_service() -> VideoService:
    init_servers = ['Server1', 'Server2', 'Server3']
    server_manager = ServerManager(init_servers)
    repository = VideoRepository(init_servers, server_manager)
    video_service = VideoService(init_servers, repository)
    return video_service


def test_should_add_20_video_across_servers():
    video_service = init_video_service()

    # Add 20 random videos
    add_random_videos(video_service, 20)
    storage_state = video_service.get_all_videos_by_server()

    assert len(storage_state.keys()) == 3
    assert count_elements_in_lists(storage_state) == 20


def test_should_throw_exception_if_the_server_is_not_found_when_attempt_to_drop_it():
    with pytest.raises(ServerNameNotFoundError):
        video_service = init_video_service()
        video_service.remove_server("Server4")


def test_should_add_20_videos_and_drop_one_server_and_add_two_servers():
    video_service = init_video_service()

    # Add 20 random videos
    add_random_videos(video_service, 20)

    # Add and drop servers
    add_servers(video_service, ["Server4", "Server5", "Server6"])
    drop_servers(video_service, ["Server2"])

    storage_state = video_service.get_all_videos_by_server()
    servers_list = list(storage_state.keys())
    assert servers_list == ["Server1", "Server3", "Server4", "Server5", "Server6"]
    assert (len(storage_state["Server4"]) == 0 and len(storage_state["Server5"]) == 0
            and len(storage_state["Server6"]) == 0)


def test_should_add_20_videos_and_drop_one_server_and_remove_two_servers_and_add_10_videos():
    video_service = init_video_service()

    # Add 20 random videos
    add_random_videos(video_service, 20)

    # Add and drop servers
    add_servers(video_service, ["Server4", "Server5", "Server6"])
    drop_servers(video_service, ["Server2"])

    # Add 10 random videos
    add_random_videos(video_service, 10)

    storage_state = video_service.get_all_videos_by_server()
    servers_list = list(storage_state.keys())

    assert servers_list == ["Server1", "Server3", "Server4", "Server5", "Server6"]
    assert (len(storage_state["Server4"]) != 0 or len(storage_state["Server5"]) != 0
            or len(storage_state["Server6"]) != 0)
