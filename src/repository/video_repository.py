from typing import List, Dict

from src.app_logging import logger
from src.exception.server_name_error import ServerNameNotFoundError
from src.repository.server_manager import ServerManager

StorageStore = Dict[str, List[str]]


class VideoRepository:

    def __init__(self, servers: List[str], node_manager: ServerManager):
        self.__video_storage: StorageStore = self.init_store(servers)
        self.__server_manager: ServerManager = node_manager

    def init_store(self, servers: List[str]) -> StorageStore:
        return {server: [] for server in servers}

    def save_video(self, video_name: str):
        server_name = self.__server_manager.get_node(video_name)
        self.__video_storage[server_name].append(video_name)
        logger.info(f"Storing video '{video_name}' on server '{server_name}'.")

    def add_server(self, server_name: str):
        self.__video_storage[server_name] = []
        self.__server_manager.add_node(server_name)

    def remove_server(self, server_name: str):
        if server_name not in self.__video_storage:
            raise ServerNameNotFoundError(server_name, message="The requested server name does not exist")
        del self.__video_storage[server_name]
        self.__server_manager.remove_node(server_name)

    def get_all_videos(self):
        return [video_name for videos_in_server in self.__video_storage.values() for video_name in videos_in_server]

    def get_all_videos_by_servers(self) -> StorageStore:
        return self.__video_storage;
