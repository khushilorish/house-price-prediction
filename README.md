# House Price Prediction API

A Machine Learning API built with FastAPI that predicts house prices based on property features. The model is trained using the Ames Housing Dataset and served through a REST API.

## Features

- House price prediction using Machine Learning
- FastAPI-based REST API
- Automatic API documentation with Swagger UI
- Data validation using Pydantic
- Preprocessing and prediction handled through a saved Scikit-Learn pipeline
- Easy testing through browser-based API interface

## Tech Stack

- Python
- FastAPI
- Scikit-Learn
- Pandas
- NumPy
- Pydantic
- Joblib
- Uvicorn

## Project Structure

```text
house-price-prediction/
│
├── app.py                     # Main FastAPI application
├── schema.py                  # Input data schema
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── house_price_pipeline.pkl   # Trained ML pipeline
├── feature_columns.pkl        # Feature columns used during training
├── dataset.csv                # Dataset
└── code.ipynb                 # Model training notebook
```

## Dataset

This project uses the Ames Housing Dataset, which contains various residential property features such as:

- Lot Area
- Neighborhood
- Overall Quality
- Year Built
- Garage Information
- Basement Features
- Total Square Footage
- And many more

The target variable is:

```text
SalePrice
```

## Machine Learning Pipeline

The pipeline includes:

1. Data Cleaning
2. Missing Value Handling
3. Feature Engineering
4. One-Hot Encoding for Categorical Features
5. Linear Regression Model Training
6. Model Serialization using Joblib

The entire preprocessing and prediction workflow is saved inside:

```text
house_price_pipeline.pkl
```

## Installation

Clone the repository:

```bash
git clone https://github.com/khushilorish/house-price-prediction.git

cd house-price-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

## API Documentation

Interactive Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
    "message": "House Price Prediction API is running"
}
```

### Prediction Endpoint

```http
POST /predict
```

Request Body:

```json
{
    "MS_SubClass": 160,
    "MS_Zoning": "RL",
    "Lot_Frontage": 24,
    "Lot_Area": 2308
}
```

Response:

```json
{
    "predicted_price": 207313.71
}
```

## Example Prediction

After providing all required house features, the API returns the estimated house price:

```json
{
    "predicted_price": 207313.71
}
```

## Learning Outcomes

This project helped me understand:

- Machine Learning model deployment
- FastAPI fundamentals
- REST API development
- Pydantic data validation
- Model serialization with Joblib
- API testing with Swagger UI
- End-to-end ML workflow
