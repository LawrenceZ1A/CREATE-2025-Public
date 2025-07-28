from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Activity 4.1: basis Hello World Web app

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

# Activity 4.2: Use routes, using routes to edit format


# Activity 4.3 Introduce --debug to allow refresh on change 

# Activity 4.4: rendering HTML templates


# Activity 4.5: 

if __name__ == '__main__':
    app.run(debug=True)
