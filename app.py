#!/urs/bin/env python3

import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><h1>Hello, world!</h1></p>"