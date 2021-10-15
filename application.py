from flask import Flask, request, flash, jsonify, Blueprint


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        print(request.form)

        return jsonify(request.form)
    return "<h1> Flask </h1>"


if __name__ == "__main__":
    app.run(debug=True)
