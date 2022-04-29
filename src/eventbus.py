from collections import defaultdict

class Events:
    user_connected = "user_connected"


# key = event name, value is list of callbacks
events = defaultdict(lambda: [])

def fire_event(event_name, data):
    for callback in events[event_name]:
        callback()

def subscribe(event_name, callback):
    events[event_name].append(callback)