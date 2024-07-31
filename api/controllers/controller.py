from flask import jsonify
from waitress import serve

from consulta_controller import *
from profissional_controller import *


@app.route("/healthcheck")
def health_check():
    return jsonify({
        "Message": "The Lacrei Saúde API is running successfully"
    })


if __name__ == "__main__":
    serve(app, port=5000)