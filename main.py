import dataclasses
import json
import uuid
import pprint
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
        #print(note)
        #print(dataclasses.asdict(note))
        self.notes[str(uuid.uuid4())] = dataclasses.asdict(note)
        print("Заметка добавлена")

    def delete(self, id: str):
        self.notes.pop(id)
        print("Заметка удалена")

    def update(self, id, title, msg):
        self.notes[id]['title'] = title if title else title
        self.notes[id]['msg'] = msg if msg else msg
        self.notes[id]['date'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print("Заметка обновлена")

    def show(self, id):
        note = self.notes.get(id)
        pprint.pprint(note)

    def showAll(self, isFiltered):
        if (isFiltered == "-"):
            pprint.pprint(self.notes)
        elif (isFiltered == "+"):
            dateFilter = input("Введите дату для фильтрации в формате dd/mm/yyyy: ")
            for k, v in self.notes.items():
                note = str(self.notes.get(k)["date"]).split(", ")
                if note[0] == dateFilter:
                    pprint.pprint(self.notes.get(k))

if __name__ == '__main__':
    a = Handler('notes.json')
    a.get()
    print('Для выхода введите команду - exit')
    while True:
        command = input("Введите команду: ")
        if command == "add":
            title = input("Введите название: ")
            msg = input("Введите тело: ")
            a.add(Note(title=title, msg=msg, date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        elif command == "update":
            id = input('Введите индентификатор: ')
            title = input("Введите название: ")
            msg = input("Введите тело: ")
            a.update(id, title, msg)
        elif command == "delete":
            id = input("Введите индентификатор: ")
            a.delete(id)
        elif command == "show":
            id = input("Введите индентификатор: ")
            a.show(id)
        elif command == "show all":
            isFiltered = input("Необходим фильтр по дате(Введите + или -): ")
            a.showAll(isFiltered)
        elif command == "exit":
            break
        a.save()