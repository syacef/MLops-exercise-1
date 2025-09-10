from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("regression.joblib")

@app.post("/predict")
def predict(data: dict):
    features = [[data["size"], data["nb_rooms"], data["garden"]]]
    prediction = model.predict(features)
    return {"y_pred": prediction[0]}