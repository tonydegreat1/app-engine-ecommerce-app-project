from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '**DTW** Default App Engine Service - V1'