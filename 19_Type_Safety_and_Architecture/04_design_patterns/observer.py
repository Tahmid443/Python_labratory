from typing import List, Callable

class EventEmitter:
    def __init__(self):
        self._listeners: dict = {}

    def on(self, event: str, callback: Callable):
        self._listeners.setdefault(event, []).append(callback)

    def off(self, event: str, callback: Callable):
        self._listeners.get(event, []).remove(callback)

    def emit(self, event: str, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)

# Usage
emitter = EventEmitter()

def on_user_created(name):
    print(f"Welcome, {name}!")

def log_event(name):
    print(f"[LOG] User {name} created")

emitter.on("user_created", on_user_created)
emitter.on("user_created", log_event)

emitter.emit("user_created", "Alice")

# Classic Observer pattern
class Subject:
    def __init__(self):
        self._observers: List = []
    def attach(self, obs): self._observers.append(obs)
    def detach(self, obs): self._observers.remove(obs)
    def notify(self, msg):
        for obs in self._observers:
            obs.update(msg)

class Observer:
    def __init__(self, name): self.name = name
    def update(self, msg): print(f"{self.name}: {msg}")

s = Subject()
s.attach(Observer("A"))
s.attach(Observer("B"))
s.notify("Hello")