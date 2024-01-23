from src.app_logging import logger
from src.repository.video_repository import VideoRepository


class UserInterface:

    def __init__(self, repository: VideoRepository):
        self.repository: VideoRepository = repository

    def display_storage(self, verbose=False):
        if verbose:
            self.__display_all_videos_per_server()
        else:
            self.__display_num_videos_per_server()

    def __display_num_videos_per_server(self):
        logger.info("-" * 50)
        logger.info("| Videos stored in the storage")
        for server, videos in self.repository.get_all_videos_by_servers().items():
            logger.info("| " + server + ": " + str(len(videos)) + " videos")
        logger.info("-" * 50)

    def __display_all_videos_per_server(self):
        logger.info("Videos stored in the storage")
        for server, videos in self.repository.get_all_videos_by_servers().items():
            logger.info(server + ": " + str(len(videos)) + " videos")
            for video in videos:
                logger.info(video)
            logger.info("#" * 50)
