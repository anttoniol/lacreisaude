from flask import request

from api.app import get_app, build_response
from api.services import profissional_service

app = get_app()


@app.route("/profissional", methods=["POST"])
def save_profissional():
    data = request.get_json()

    try:
        return build_response(True, profissional_service.save(data), 200)
    except Exception as ex:
        error_message = "Error when saving professional: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/profissional/<id>", methods=["DELETE"])
def delete_profissional(id):
    try:
        return build_response(True, profissional_service.delete(id), 200)
    except Exception as ex:
        error_message = "Error when deleting professional: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/profissional/<id>", methods=["PUT"])
def update_profissional(id):
    data = request.get_json()

    try:
        return build_response(True, profissional_service.update(id, data), 200)
    except Exception as ex:
        error_message = "Error when updating professional: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)
