import os

from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = os.environ.get("PORT", "5000")
CHOKOMOKO_SECRET_SM = os.environ.get("CHOKOMOKO_SECRET_SM", None)
CHOKOMOKO_SECRET_SSM = os.environ.get("CHOKOMOKO_SECRET_SSM", None)


@app.route("/liveness", methods=["GET"])
def liveness():
    return jsonify({"message": "liveness OK"}), 200


@app.route("/readiness", methods=["GET"])
def readiness():
    return jsonify({"message": "readiness OK"}), 200


@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    return jsonify({"message": f"Hello {name}"}), 200


@app.route("/age", methods=["POST"])
def age():
    data = request.get_json()
    if not data or "age" not in data:
        return jsonify({"error": "Missing 'age' field in request body"}), 400
    return jsonify({"message": f"Your age is {data['age']}"}), 200


@app.route("/secret", methods=["GET"])
def greet():
    var_name = request.args.get("varName")
    if not var_name:
        return jsonify({"error": "Missing 'varName' parameter"}), 400
    elif var_name == "CHOKOMOKO_SECRET_SM":
        return jsonify({"message": f"Secret '{var_name}' value is: {CHOKOMOKO_SECRET_SM}"}), 200
    elif var_name == "CHOKOMOKO_SECRET_SSM":
        return jsonify({"message": f"Secret '{var_name}' value is: {CHOKOMOKO_SECRET_SSM}"}), 200
    else:
        return jsonify({
            "error": "Invalud parameter, 'varName' value must be one of ['CHOKOMOKO_SECRET_SM', CHOKOMOKO_SECRET_SSM]"
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
