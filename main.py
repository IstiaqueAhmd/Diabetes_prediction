import uvicorn ##ASGI
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}

#Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome Diabetes Prediction Model': f'{name}'}


#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)




