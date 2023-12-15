import dataclasses
import json

@dataclasses.dataclass
class Note:
    title: str
    msg: str
    date: str

class Handler:

    notes = dict()

    def __init__(self, filename):
        self.filename = filename

    def get(self):
        try:
            with open(self.filename, 'r') as f:
                self.notes = json.load(f)
        except:
            self.notes = dict()