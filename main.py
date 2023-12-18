from datetime import datetime
from handler import Handler
from note import Note

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