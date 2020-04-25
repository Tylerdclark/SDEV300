# my_webpage.py
"""A website using flask and HTML and css templates"""
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

now = datetime.now()


@app.route('/')
def index():
    return render_template('index.html', current_time=now.strftime("%m/%d/%Y, %H:%M:%S"))


if __name__ == '__main__':
    app.run(debug=True)
