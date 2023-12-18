import dataclasses
import datetime
import json
import pprint
import uuid

from note import Note


class Handler:

    def __init__(self, filename: str):
        self.filename = filename
        self.notes = dict()

    def get(self):
        try:
            with open(self.filename, 'r') as f:
                self.notes = json.load(f)
        except:
            self.notes = dict()

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.notes, indent=4))

    def add(self, note: Note):
        self.notes[str(uuid.uuid4())] = dataclasses.asdict(note)
        print("Заметка добавлена")

    def delete(self, id: str):
        try:
            self.notes.pop(id)
        except KeyError:
            print("Заметка не найдена")
        else:
            print("Заметка удалена")

    def update(self, id: str):
        title = input("Введите название: ")
        msg = input("Введите тело: ")
        
        try:
            self.notes[id]['title'] = title
            self.notes[id]['msg'] = msg
            self.notes[id]['date'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        except KeyError:
            print("Заметка не найдена")
        else:
            print("Заметка обновлена")

    def show(self, id: str):
        note = self.notes.get(id)
        pprint.pprint(note)

    def showAll(self, isFiltered: bool):
        if isFiltered == False:
            pprint.pprint(self.notes)
        else:
            dateFilter = input("Введите дату для фильтрации в формате dd/mm/yyyy: ")
            for k, v in self.notes.items():
                note = str(self.notes.get(k)["date"]).split(", ")
                if note[0] == dateFilter:
                    pprint.pprint(k + ": "+ str(self.notes.get(k)))