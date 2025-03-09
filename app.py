#importing necessary libraries
from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    #loading saved model here in this python file
    model = joblib.load('titanic_model.pkl')
    #creating data frame of JSON data
    df = pd.DataFrame(json, index=[0])
    df = df.infer_objects()
    print(df.dtypes)
    print("Original Data Types:")
    print(df.dtypes)
    print(df.to_string())
   
    
    y_predict = model.predict(df)
   
    res= {'Predicted Survival (1 is Yes 0 is No)': str(y_predict[0])}
    #res={"Survival": "in progress"}
    return jsonify(res)

if __name__ == "__main__":
    print("Model Running")
    app.run(host='0.0.0.0')