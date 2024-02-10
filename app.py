from flask import Flask, request, jsonify
from src.get_data import read_params
import pandas as pd
from prediction import api_response

params = read_params("params.yaml")
app = Flask(__name__)

# Load the trained machine learning model


@app.route("/predict", methods=["POST"])
def predict():
    # Get data from the request
    data = request.json
    # Perform prediction using the loaded model
    if request.json:
        response = api_response(request.json)
        return jsonify({"prediction": response})


if __name__ == "__main__":
    app.run(debug=True)
