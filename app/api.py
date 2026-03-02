from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
import os
import sys
from prometheus_fastapi_instrumentator import Instrumentator

# --------------------------------------------------
# Create FastAPI app
# --------------------------------------------------
app = FastAPI(title="Loan Prediction API 🚀")

# Add Prometheus monitoring AFTER app creation
Instrumentator().instrument(app).expose(app)

# --------------------------------------------------
# Resolve absolute model path
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "full_system_new_version_one.pkl")

print("Python executable:", sys.executable)
print("Loading model from:", MODEL_PATH)

# --------------------------------------------------
# Load model safely
# --------------------------------------------------
try:
    with open(MODEL_PATH, "rb") as f:
        loaded_object = pickle.load(f)

    if isinstance(loaded_object, dict):
        if "model" in loaded_object:
            model = loaded_object["model"]
        else:
            raise ValueError("Dictionary found but no 'model' key inside.")
    else:
        model = loaded_object

    print("Model loaded successfully ✅")
    print("Model type:", type(model))

except Exception as e:
    raise RuntimeError(f"Model loading failed: {e}")

# --------------------------------------------------
# Input schema
# --------------------------------------------------
class LoanInput(BaseModel):
    Age: int
    Income: float
    LoanAmount: float
    CreditScore: float
    YearsExperience: int
    Gender: str
    Education: str
    City: str
    EmploymentType: str


# --------------------------------------------------
# Health route
# --------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "Loan Prediction API Running ✅",
        "model_type": str(type(model))
    }


# --------------------------------------------------
# Prediction route
# --------------------------------------------------
@app.post("/predict")
def predict(data: LoanInput):
    try:
        df = pd.DataFrame([data.model_dump()])

        if hasattr(model, "feature_names_in_"):
            expected_cols = list(model.feature_names_in_)
            missing_cols = set(expected_cols) - set(df.columns)

            if missing_cols:
                raise ValueError(f"Missing columns: {missing_cols}")

            df = df[expected_cols]

        prediction = model.predict(df)[0]

        return {
            "LoanApproved": int(prediction),
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))