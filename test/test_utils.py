from src.service.video_service import VideoService
from src.utils.random_utils import *


def add_random_videos(video_service: VideoService, num_videos: int):
    videos = generate_n_videos(num_videos)
    for video in videos:
        video_service.store_video(video)


def drop_servers(video_service: VideoService, servers: List[str]):
    for server in servers:
        video_service.remove_server(server)


def add_servers(video_service: VideoService, servers: List[str]):
    for server in servers:
        video_service.add_server(server)


def count_elements_in_lists(my_dict):
    total_count = sum(len(lst) for lst in my_dict.values())
    return total_count
