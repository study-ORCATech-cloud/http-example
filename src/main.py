import logging
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = os.environ.get("PORT", "5000")


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
