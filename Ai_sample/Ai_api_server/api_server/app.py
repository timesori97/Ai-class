from flask import Flask #flask 클래스로 부터 Flask라는 함수를 가져와
from flask_cors import CORS
from top10 import mtop10
from cosine_top10 import toptop10
from flask import request

import json

app=Flask(__name__)
CORS(app) #cors를 무력화시키는 코드

@app.route("/getString")
def home():
    return 'big data AI System'

@app.route("/gettop10")
def top10():
    r=mtop10()
    rdata=r.to_json(orient="records")
    return rdata

@app.route("/get_costop10")
def cosinTop():
    fname=request.args.get('moviename',type=str,default='no')
    r=toptop10(fname)
    print(r)
    return r