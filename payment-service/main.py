from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'DTW Application: Payment Service - V1'