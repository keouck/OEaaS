from fastapi import FastAPI
from keras.models import load_model
from numpy import argmax

model = load_model('accurate.h5')
classes = ['Odd', 'Even']

app = FastAPI()

def predict_target(number, model, classes): 
    pred = model.predict([number]) 
    return classes[int(argmax(pred, axis=1))] 

@app.get("/check/{number}")
async def check(number: float):
    return {number: predict_target(number, model, classes)}