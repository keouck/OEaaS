from fastapi import FastAPI

app = FastAPI()

@app.get("/is-odd/{number}")
async def is_odd(number: float):
    return {number: True if number % 2 != 0 else False}

@app.get("/is-even/{number}")
async def is_even(number: float):
    return {number: True if number % 2 == 0 else False}