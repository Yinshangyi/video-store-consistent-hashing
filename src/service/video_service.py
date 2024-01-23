from typing import List

from src.app_logging import logger
from src.repository.server_manager import ServerManager
from src.repository.video_repository import VideoRepository
from src.exception.server_name_error import ServerNameNotFoundError


class VideoService:
    def __init__(self, servers: List[str], repository: VideoRepository):
        self.server_manager: ServerManager = ServerManager(servers)
        self.repository = repository

    def store_video(self, video_name: str):
        self.repository.save_video(video_name)

    def add_server(self, server_name: str):
        self.repository.add_server(server_name)
        logger.info(f"Server: {server_name} has been added")

    def remove_server(self, server_name: str):
        try:
            self.repository.remove_server(server_name)
            logger.info(f"Server: {server_name} has been removed")
        except ServerNameNotFoundError:
            logger.error(f"Server: {server_name} does not exist")
            raise ServerNameNotFoundError(server_name, message="The requested server name does not exist")

    def get_all_videos_names(self):
        return self.repository.get_all_videos()

    def get_all_videos_by_server(self):
        return self.repository.get_all_videos_by_servers()
