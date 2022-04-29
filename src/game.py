from dataclasses import dataclass

class Game:

    class States:
        setup = 0
        player_turn = 1
        combat = 2
        end = 3

    def __init__(self):
        self._state = Game.States.setup
        self._objects = []

    def get_state(self):
        return self._state

    def _create_setup_scene(self):
        #maybe replace with scenes?
        #or maybe functions are enough
        pass