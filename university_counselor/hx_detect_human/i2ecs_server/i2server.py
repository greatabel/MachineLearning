import os
from flask import Flask, request, Response
from flask import render_template
import jsonpickle
import numpy as np
import cv2
import pickle 


addr = 'http://localhost:5000'
test_url = addr + '/api/test'

# Initialize the Flask application
app = Flask(__name__)
app.debug = True


PEOPLE_FOLDER = os.path.join('static', 'received')

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

print('instance_path=', app.root_path)
status = False


def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
     
    dbfile.close() 
    return db['status'], db['time']

# route http posts to this method
@app.route('/api/status', methods=['POST', 'GET'])
def status():
    status, timestamp = loadData()
    print( status, timestamp, '@'*10)
    # build a response dict to send back to client
    response = {'message': status, 'timestamp':timestamp
                }



    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")



# start flask app
app.run(host="localhost", port=5000)