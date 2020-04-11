from flask import Flask
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
print("app file")
from app import routes
print(__name__)
if __name__ == "app":
    app.run(host="0.0.0.0", port=80)
