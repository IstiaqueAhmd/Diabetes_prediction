from calendar import day_abbr

import uvicorn
from fastapi import FastAPI
from HealthData import HealthData
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Diabetes Prediction App': f'{name}'}

@app.post('/predict')
def predict_banknote(data: HealthData):
    data = data.dict()
    gender = data['gender']
    age = data['age']
    hypertension = data['hypertension']
    heart_disease = data['heart_disease']
    bmi = data['bmi']
    hbA1c_level = data['hbA1c_level']
    blood_glucose_level = data['blood_glucose_level']
    current = data['current']
    ever = data['ever']
    former = data['former']
    never = data['never']
    not_current = data['not_current']


    prediction = classifier.predict([[gender, age, hypertension,heart_disease,bmi,hbA1c_level,blood_glucose_level,current,ever,former,never,not_current]])
    if (prediction[0] == 0):
        prediction = "You Have Diabetes"
    else:
        prediction = "You do not have Diabetes"
    return {
        'prediction': prediction
    }


#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload