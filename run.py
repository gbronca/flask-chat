import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''Main page with instructions'''
    return "<h1> Hello There</h1>"

@app.route('/<username>')
def user(username):
    return 'Hi ' + username

@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)



if __name__ == '__main__':
    app.run(debug=True)
 #   app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)