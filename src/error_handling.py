from flask import Flask, jsonify

from src.exception.server_name_error import ServerNameNotFoundError


def handle_error(app: Flask):
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Route not found'}), 404

    @app.errorhandler(405)
    def internal_error(error):
        return jsonify({'error': 'Method not allowed'}), 500

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

    @app.errorhandler(ServerNameNotFoundError)
    def handle_server_name_not_found(error):
        response = jsonify({'message': str(error)})
        response.status_code = 400
        return response
