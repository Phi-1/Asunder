from uuid import uuid4
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import os
from numpy import broadcast
from src.game import Game, Click_event

SERVER = Flask(__name__)
SOCKETIO = SocketIO(SERVER)
GAME = Game()

def read_html(filepath):
    with open(filepath) as f:
        return f.read()

@SERVER.route("/", methods=["GET"])
def index():
    return read_html("./index.html")

@SOCKETIO.on("connect")
def user_connects(auth):
    if GAME.get_state() == Game.States.test or Game.get_state() == Game.States.setup:
        player_id = uuid4()
        GAME.add_player(player_id)
        emit("assign_id", {"data": str(player_id)}, broadcast=True)

@SOCKETIO.on("click")
def on_click(event):
    data = event["data"]
    GAME.handle_event(Click_event(data["player_id"], data["x"], data["y"]))
    objects = GAME.get_objects()
    emit("update", {"data": objects}, broadcast=True)

if __name__ == "__main__":
    load_dotenv()
    server_ip = os.environ.get("SERVER_IP")
    server_port = os.environ.get("SERVER_PORT")
    SOCKETIO.run(SERVER, host=server_ip, port=server_port, debug=True)