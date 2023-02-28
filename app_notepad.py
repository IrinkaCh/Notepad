from notepad_function import Note_pad


def app_notepad():
    note_Pad = Note_pad()
    print("Выберите действие:\n\
    1) Создать новую заметку\n\
    2) Просмотреть список всех заметок\n\
    3) Выбрать заметку по названию, для дальнейших действий")
    select = input()
    if select == "1":
        note_Pad.add_note()
    if select == "2":
        note_Pad.list_note()
    if select == "3":
        note_Pad.select_note()
