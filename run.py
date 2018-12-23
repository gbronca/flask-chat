import os
from flask import Flask, redirect

app = Flask(__name__)

messages = []

def add_messages(username, message):
    '''Add messages to the messages list'''
    messages.append('{}: {}'.format(username, message))

def get_all_messages():
    '''Get all of the messages and separate them with a 'br' tag'''
    return '<br>'.join(messages)

@app.route('/')
def index():
    '''Main page with instructions'''
    return "<h1> Hello There</h1>"

@app.route('/<username>')
def user(username):
    '''Display chat messages'''
    return '<h1>Welcome, {0}</h1>{1}'.format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    '''Create a new message and redirect to the chat page'''
    add_messages(username, message)
    return redirect(username)



if __name__ == '__main__':
    app.run(debug=True)
 #   app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)