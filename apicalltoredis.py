
##Import Necessary Packages ##

import pandas as pd
import jsonpickle
import redis
import pickle
import json
import zlib
from app import app
from flask import jsonify
from flask import Flask, request

app = Flask(__name__)

## API Call ##

@app.route('/count', methods=['GET'])
def get_count():
    r = redis.Redis(host='localhost', port=6379)
    data = pickle.loads(zlib.decompress(r.get('WomensShoesList')))
    data1 = jsonpickle.encode(data, unpicklable=True)
    tasks = pickle.dumps(len(data1))
    return jsonify({'task': tasks})

@app.route('/getdata', methods=['GET'])
def get_data():
    r = redis.Redis(host='localhost', port=6379)
    data = pickle.loads(zlib.decompress(r.get('WomensShoesList')))
    data1 = jsonpickle.encode(data, unpicklable=True)
    tasks = data1
    return jsonify({'task': tasks})

if __name__ == "__main__":
    app.run()



