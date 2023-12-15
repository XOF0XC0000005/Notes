import dataclasses
import json
import uuid
from datetime import datetime

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
        print(self.notes)

    def delete(self, id: str):
        self.notes.pop(id)

    def update(self, id, title, msg):
        self.notes['id']['title'] = title if title else title
        self.notes['id']['msg'] = msg if msg else msg
        self.notes['id']['date'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")