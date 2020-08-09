from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello_world():
    return {"hello":"Jose"}

@app.get("/abc")
def abc():
    return {"ABC":[1,2,3]}