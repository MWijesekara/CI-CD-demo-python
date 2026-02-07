from fastapi import FastAPI
from calculator import *

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the calculator app!"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": add(a, b)}

@app.get("/subtract")
def subtract_numbers(a: int, b: int):
    return {"result": subtract(a, b)}

