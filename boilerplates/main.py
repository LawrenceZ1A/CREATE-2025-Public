"""
This is a template for a Flask file for developing your web apps. 
Feel free to fork and clone this to modify as needed, or if you prefer, start from scratch on a new file.

Please ensure that this file is located in the main directory of your project.

To run, cd into your project directory and then run the following command:
flask --app (name of your project) run --debug
"""

from flask import Flask # imports
from datetime import datetime
app = Flask(__name__) # create Flask app

@app.route("/")
def hello():
    return "<h1>hello!</h1>"

@app.route("/helloall")
def hello_all():
    return "hello everyone!"

"""
Don't delete the code below! Needed for running the app.
"""

if __name__ == "__main__":
    app.run(debug=True)
