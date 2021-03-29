import os
from flask import Flask, jsonify, request
from gpx_tools import generate_map

app = Flask(__name__)
    
@app.route('/upload', methods=['POST'])
def home():
  print('Recieved from client: {}'.format(request.files['file']))
  return jsonify(
    html=generate_map(request.files['file'])
  )
