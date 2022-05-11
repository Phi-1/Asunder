from uuid import uuid4
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import os
from src.game import Game

SERVER = Flask(__name__)
SOCKETIO = SocketIO(SERVER)
GAME = Game()

def read_html(filepath):
    with open(filepath) as f:
        return f.read()

@SERVER.route("/", methods=["GET"])
def index():
    return read_html("./index.html")

@SERVER.route("/lobby", methods=["GET"])
def lobby():
    return read_html("./game.html")

# setup screen requests list of available ships
@SOCKETIO.on("get_ship_selection")
def get_ship_selection():
    emit("get_ship_selection", {"ships": [{"name": "ship 1", "image": "0.png"}, {"name": "ship 2", "image": "1.png"}, {"name": "ship 3", "image": "3.png"}]}, broadcast=False)

# new player connects, provides callsign and ship type
# broadcasts new player to all existing players
@SOCKETIO.on("player_connect")
def player_connect():
    pass

# player changes affiliation, provides player id and new affiliation
# broadcasts player id and new affiliation
@SOCKETIO.on("player_change_affiliation")
def player_change_affiliation():
    pass

# player presses ready or unready button in lobby, OR client has played out combat scene and is ready for next turn
# broadcasts player id and ready state (ready/unready)
@SOCKETIO.on("player_ready")
def player_ready():
    pass

# player presses end turn button, provides player id and list of actions
# broadcasts start of combat phase ONLY when all players have ended their turn
@SOCKETIO.on("player_end_turn")
def player_end_turn():
    pass

if __name__ == "__main__":
    load_dotenv()
    server_ip = os.environ.get("SERVER_IP")
    server_port = os.environ.get("SERVER_PORT")
    SOCKETIO.run(SERVER, host="0.0.0.0", port=server_port, debug=True)