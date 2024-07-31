from flask import request

from api.app import get_app, build_response
from api.services import consulta_service

app = get_app()


@app.route("/consulta", methods=["POST"])
def save_consulta():
    data = request.get_json()

    try:
        return build_response(True, consulta_service.save(data), 200)
    except Exception as ex:
        error_message = "Error when saving appointment: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/consulta/<id>", methods=["DELETE"])
def delete_consulta(id):
    try:
        return build_response(True, consulta_service.delete(id), 200)
    except Exception as ex:
        error_message = "Error when deleting appointment: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/consulta/<id>", methods=["PUT"])
def update_consulta(id):
    data = request.get_json()

    try:
        return build_response(True, consulta_service.update(id, data), 200)
    except Exception as ex:
        error_message = "Error when updating appointment: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


@app.route("/consulta/", methods=["GET"])
def get_consulta_by_id_profissional():
    id_profissional = request.args.get('id_profissional')

    try:
        return build_response(True, consulta_service.get_by_id_profissional(id_profissional), 200)
    except Exception as ex:
        error_message = "Error when getting appointment by professional ID: " + ex.__str__()
        print(error_message)
        return build_response(False, error_message, 500)


