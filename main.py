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
            self.notes[id]['title'] = title if title is not None else ""
            self.notes[id]['msg'] = msg if msg is not None else ""
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
            a.update(id)
        elif command == "delete":
            id = input("Введите индентификатор: ")
            a.delete(id)
        elif command == "show":
            id = input("Введите индентификатор: ")
            a.show(id)
        elif command == "show all":
            isFiltered = True if input("Необходим фильтр по дате(Введите + или -): ") == "+" else False
            a.showAll(isFiltered)
        elif command == "exit":
            break
        a.save()