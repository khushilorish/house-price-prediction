from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from schema import HouseData

app = FastAPI(title ="House Price Prediction API", version="1.0")

feature_columns = joblib.load("feature_columns.pkl")
pipeline = joblib.load("house_price_pipeline.pkl")

@app.get("/")
def home():
    return{
        "message": "House Price Prediction API is running"
    }

@app.post("/predict")
def predict(data: HouseData):
    df = pd.DataFrame([data.dict()])
    df.columns = [col.replace("_", " ") for col in df.columns]
    df.rename(columns={"Year Remod Add": "Year Remod/Add","Second Flr SF": "2nd Flr SF"}, inplace = True)

    prediction = pipeline.predict(df)
    actual_price = np.expm1(prediction[0])

    return{
        "predicted_price": round(float(actual_price), 2)
    }