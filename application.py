from flask import Flask, request, flash, jsonify, Blueprint, Response


app = Flask(__name__)


@app.route("/signin", methods=["GET", "POST", "OPTIONS"])
def home():
    if request.method == "POST":
        print(request.form)
        print(dict(request.form))
        my_res = Response(jsonify(request.form))
        my_res.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"

        return my_res
    return Response("Flask")


if __name__ == "__main__":
    app.run(debug=True)
