from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import os
from src.game import Game

SERVER = Flask(__name__)
SOCKETIO = SocketIO(SERVER)
GAME_INSTANCE = Game()

def read_html(filepath):
    with open(filepath) as f:
        return f.read()

@SERVER.route("/", methods=["GET"])
def index():
    return read_html("./index.html")

@SOCKETIO.on("connect")
def user_connects(auth):
    print(auth)
    print("user connected")

    emit()

if __name__ == "__main__":
    load_dotenv()
    server_ip = os.environ.get("SERVER_IP")
    server_port = os.environ.get("SERVER_PORT")
    SOCKETIO.run(SERVER, host=server_ip, port=server_port, debug=True)