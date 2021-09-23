from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)

pickle_file = open('lin_reg_model.sav','rb')
#pickle_file = open('lin_reg_model.pkl','rb')
pickle_model = pickle.load(pickle_file)


@app.route("/")
def home():
    return "Welcome to Machine Learning"

@app.route("/predict")
def predict_model():
    """ Predicting the MPG
    ---
    parameters:
      - name: Cylinders
        in: query
        type: number
        required: true
      - name: Displacement
        in: query
        type: number
        required: true
      - name: Horsepower
        in: query
        type: number
        required: true
      - name: Weight
        in: query
        type: number
        required: true
      - name: Acceleration
        in: query
        type: number
        required: true
    
    responses:
        200:
            description: Result is 
    """

    Cylinders  = request.args.get('Cylinders')
    Displacement = request.args.get('Displacement')
    Horsepower = request.args.get('Horsepower')
    Weight = request.args.get('Weight')
    Acceleration = request.args.get('Acceleration')

    output = pickle_model.predict([[Cylinders, Displacement, Horsepower, Weight, Acceleration]])

    return f"The Prediction is {output}"

if __name__ == '__main__':
    app.run(debug = True)