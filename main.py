import dataclasses
import json
import uuid

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

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.notes, indent=4))

    def add(self, note):
        print(note)
        print(dataclasses.asdict(note))
        self.notes[str(uuid.uuid4())] = dataclasses.asdict(note)