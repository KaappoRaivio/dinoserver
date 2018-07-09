from findbyid import FindByIDFactory

from flask import Flask, request
from flask_api import status
import threading
import time
#HTTP_200_OK

import constants


class Connection(threading.Thread, FindByIDFactory):

    def __init__(self, ip_addr):
        # super(threading.Thread, self).__init__()
        # super(FindByIDFactory, self).__init__()
        # super().__init__()
        threading.Thread.__init__(self)
        FindByIDFactory.__init__(self)

        self.ip_addr = ip_addr

        self.alive = False

    def run(self):
        while True:
            time.sleep(2)
            if self.alive:
                self.alive = False
            else:
                break

        print(f"Connection {self.ID} was not refreshed on time! Halting!")
        del self

    def refresh(self):
        print(f"refreshed the thread with ID {self.ID}")
        self.alive = True



app = Flask(__name__)


@app.route('/')
def index():
    return "Nothing to see here"


@app.route('/get-highscore/', methods=["GET"])
def getHighscore():
    return "100 :D", status.HTTP_200_OK


@app.route('/set-score/', methods=["POST"])
def setScore():
    print(request.form[constants.SCORE_KEY])
    return "", status.HTTP_202_ACCEPTED


@app.route("/open-connection/", methods=["GET"])
def openConnection():
    ip = request.remote_addr.strip()
    temp = Connection(ip)
    temp.start()
    return f"{temp.ID}", status.HTTP_200_OK


@app.route("/refresh-connection/", methods=["POST"])
def refreshConnection():

    ip = request.remote_addr.strip()
    connection_id = int(request.form[constants.ID])

    connection = Connection.findByID(connection_id)


    if connection.ip_addr == ip:
        connection.refresh()
        return "", status.HTTP_202_ACCEPTED
    else:
        return "", status.HTTP_401_UNAUTHORIZED


app.run(port=5000, debug=False)