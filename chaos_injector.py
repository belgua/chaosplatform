from flask import Flask,jsonify,request
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/inject_fault',methods=['POST'])
def inject_fault():
    dns = request.json['dns']
    fault = request.json['fault']
    return "yaay"
    
if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
