import datetime

import flask
from flask import Flask, session



class number(object):
    def __init__(self):
        self.number = 0

    def increment(self):
        self.number += 1

    def get_number(self):
        return self.number

app = Flask(__name__)
visitors = {}
init_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
totalvisits = number()

@app.route('/')
def dashboard():

    print(init_time)
    unique_visitors = len(visitors)
    total = totalvisits.get_number()

    print(total)
    print(visitors)

    return flask.render_template('dashboard.html', visitors=visitors, totalvisits=total, unique_visitors=unique_visitors, init_time=init_time)


@app.route('/track')
def track():
    totalvisits.increment()
    ip = flask.request.remote_addr
    if ip in visitors:
        nr = visitors[ip]
        visitors[ip] = nr + 1
        print("GAMMEL")
        print(nr)
    else:
        visitors[ip] = 0
        print("NY")

    return "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" #base 64 encoded 1x1px gif

if __name__ == '__main__':
    app.run()
