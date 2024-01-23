from flask import request, Blueprint, make_response, jsonify, current_app as app

controller = Blueprint('controller', __name__)


@controller.route('/server/<server_name>', methods=["POST"])
def add_server(server_name: str):
    app.video_service.add_server(server_name)
    return make_response(f"A new server: {server_name} has been added", 200)


@controller.route("/server/<server_name>", methods=["DELETE"])
def remove_server(server_name: str):
    app.video_service.remove_server(server_name)
    return make_response(f"The server: {server_name} has been removed", 200)


@controller.route("/video/<video_name>", methods=["POST"])
def store_video(video_name: str):
    app.video_service.store_video(video_name)
    return make_response(f"The video: {video_name} has been saved", 200)


@controller.route("/video", methods=["GET"])
def get_video():
    by_server = request.args.get('details', 'false').lower() == 'true'
    if by_server:
        videos = app.video_service.get_all_videos_by_server()
        return jsonify(videos), 200
    else:
        videos = app.video_service.get_all_videos_names()
        return jsonify(videos), 200
