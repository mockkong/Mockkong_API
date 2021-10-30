from flask import Flask, request, flash, jsonify, Blueprint, Response
from flask_cors import CORS
from web.app import create_app

app = Flask(__name__)
CORS(app)


@app.route("/signin", methods=["GET", "POST", "OPTIONS"])
def home():
    if request.method == "POST":
        my_res = request.form
        print(my_res)

        return my_res
    return "success"


if __name__ == "__main__":
    app.run(debug=True)
