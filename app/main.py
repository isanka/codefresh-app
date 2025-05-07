# app/main.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    secret = os.getenv('DB_PASSWORD', 'Secret Not Found')
    return f"Vault Secret: {secret}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

