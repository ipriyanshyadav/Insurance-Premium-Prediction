from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.User_input import UserInput
from Schema.prediction_response import PredictionResponse
from model.predict import predict_output, MODEL_VERSION, model

app= FastAPI()

#human redable
@app.get("/")
def home_page():
    return {"Message": "Insurance Premium prediction API"}

#machine redable
@app.get("/health")
def health_check():
    return {"Status": "OK",
            "Model Version": MODEL_VERSION,
            "Model loaded": model is not None
            }

@app.post("/predict", response_model= PredictionResponse)
def predict_premium(data: UserInput):
    user_input={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))