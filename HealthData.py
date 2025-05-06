from pydantic import BaseModel

class HealthData(BaseModel):
    gender: float
    age: float
    hypertension: float
    heart_disease: float
    bmi: float
    hbA1c_level: float
    blood_glucose_level: float
    current: float
    ever: float
    former: float
    never: float
    not_current: float


