from flask import Flask

from src.controller.video_controller import controller
from src.error_handling import handle_error
from src.repository.server_manager import ServerManager
from src.repository.video_repository import VideoRepository
from src.service.video_service import VideoService


def create_app() -> Flask:
    app = Flask(__name__)

    servers = ['Server1', 'Server2', 'Server3']
    server_manager = ServerManager(servers)
    repository = VideoRepository(servers, server_manager)
    app.video_service = VideoService(servers, repository)
    handle_error(app)
    app.register_blueprint(controller, url_prefix='/')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')