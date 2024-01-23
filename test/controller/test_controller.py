import json

import pytest
from flask.testing import FlaskClient

from main import create_app  # Import your Flask app
from test.test_utils import generate_n_videos


@pytest.fixture(scope="function")
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_add_server(client: FlaskClient):
    response = client.post("/server/Server4")
    assert response.status_code == 200
    assert "Server4" in response.data.decode()


def test_remove_server(client: FlaskClient):
    response = client.delete("/server/Server2")
    assert response.status_code == 200
    assert "Server2" in response.data.decode()


def test_store_video(client: FlaskClient):
    response = client.post("/server/video1.mp4")
    assert response.status_code == 200
    assert "video1.mp4" in response.data.decode()


def post_videos_to_store(num_videos: int, client: FlaskClient):
    video_names = generate_n_videos(num_videos)
    for video_name in video_names:
        client.post(f"/video/{video_name}")


def test_get_video(client: FlaskClient):
    post_videos_to_store(10, client)
    response = client.get("/video")
    assert response.status_code == 200
    video_names = json.loads(response.data.decode())
    assert len(video_names) == 10


def test_get_video_by_server(client: FlaskClient):
    post_videos_to_store(10, client)
    response = client.get("/video?details=true")
    assert response.status_code == 200
    video_names_per_server = json.loads(response.data.decode())
    assert list(video_names_per_server.keys()) == ["Server1", "Server2", "Server3"]
