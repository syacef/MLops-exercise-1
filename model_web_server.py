from fastapi import FastAPI
import joblib
import uvicorn

app = FastAPI()

model = joblib.load("regression.joblib")

@app.post("/predict")
def predict(data: dict):
    features = [[data["size"], data["nb_rooms"], data["garden"]]]
    prediction = model.predict(features)
    return {"y_pred": prediction[0]}


if __name__ == "__main__":
    uvicorn.run("model_web_server:app", host="0.0.0.0", port=8000, reload=True)
