from dataclasses import dataclass
from uuid import uuid4
import json
import uuid

@dataclass
class Event:
    player_id: str

@dataclass
class Click_event(Event):
    x: int
    y: int

@dataclass
class Connection_event(Event):
    pass

@dataclass
class Object:
    id = str(uuid4())
    x: int
    y: int

@dataclass
class Player:
    id: str
    ship: Object

class Game:
    class States:
        setup = 0
        player_turn = 1
        combat = 2
        end = 3
        test = 4

    def __init__(self):
        self._state = Game.States.test
        self._players = []
        self._objects = []
        self._create_test_scene()

    def get_state(self):
        return self._state

    def add_player(self, player_id):
        self._players.append(Player(player_id, Object(300, 300)))

    def get_player(self, player_id):
        for player in self._players:
            if player.id == player_id:
                return player
        return None

    def get_players(self):
        return self._players

    def get_objects(self):
        return [{"x": obj.x, "y": obj.y} for obj in self._objects]

    def handle_event(self, event: Event):
        if isinstance(event, Click_event):
            self._objects.append(Object(event.x, event.y))

    def _create_test_scene(self):
        self._objects.append(Object(4, 5))
        self._objects.append(Object(200, 200))