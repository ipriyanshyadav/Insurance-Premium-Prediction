import pickle
import pandas as pd

with open("model/model.pkl", "rb") as f:
    model= pickle.load(f)

# it's random here but to be extracted through mlflow
MODEL_VERSION= "1.0.1"

def predict_output(user_input: dict):
    input_df= pd.DataFrame([user_input])
    output= prediction = model.predict(input_df)[0]
    return output