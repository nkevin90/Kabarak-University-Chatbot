from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_get():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.json["message"]
    response = get_response(message)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
