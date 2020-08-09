from flask import Flask

app=Flask(__name__)

#https://localhost:8080
@app.route("/",methods=['GET'])
def hello_world():
    #run other code here
    return "Hello Mundo This es Flask"

#https://localhost:8080
@app.route("/abc",methods=['GET'])
def abc():
    #run other code here
    return "Hello Mundo This es ABC"