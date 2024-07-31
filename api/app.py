from flask import Flask, jsonify

app = None


def get_app():
    global app

    if app is None:
        app = Flask(__name__)

    return app


def build_response(success, result, status):
    return jsonify(
        response = {
            "success": success,
            "result": result
        },
        status=status
    )
