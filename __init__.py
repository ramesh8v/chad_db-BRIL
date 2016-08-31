import os
import json
import py_scripts as ps
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ubuntu:hello@0.0.0.0:5432/chad_db'
#db = SQLAlchemy(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")
    
@app.route("/check", methods = ["POST", "GET"])
def check():
    return render_template("check.html")

@app.route("/db", methods = ["POST", "GET"])
def database():
    return render_template("database.html")

@app.route('/incoming', methods=['POST', 'GET'])
def incoming():
    session['data'] = json.loads(request.data.decode())
    return json.dumps(ps.listtodict(ps.db((session['data'].pop('marker', None)), (session['data'].pop('chrome', None)), (session['data'].pop('distmin', None)), (session['data'].pop('distmax', None)))), ensure_ascii=False)

@app.route('/singledat', methods=['POST', 'GET'])
def singledat():
    session['datas'] = json.loads(request.data.decode())
    return json.dumps(ps.fetchdbsd(session['datas'].pop("marker", None)), ensure_ascii=False)
    
@app.route('/singleseq', methods=['POST', 'GET'])
def singleseq():
    session['datas'] = json.loads(request.data.decode())
    return json.dumps(ps.fetchdbseq(session['datas'].pop("marker", None)), ensure_ascii=False)


if __name__ == "__main__":
    host=os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.secret_key= '70b99c5e-52e6-11e6-814e-000000000018'
    app.run(host=host, port =port, debug=True)