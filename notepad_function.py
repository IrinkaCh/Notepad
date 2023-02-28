from datetime import datetime
import csv
import os
import shutil


class Note_pad:

    def __init__(self):
        self.number_line = None

    def add_note(self):
        if os.path.isfile("file.csv") == False:
            headerlist = (
                {"name_note": [], "date_time_last_save": [], "text_note": []})
            with open("file.csv", "w", newline="", encoding="utf-8") as file_note:
                d_writer = csv.DictWriter(
                    file_note, delimiter=";", fieldnames=headerlist)
                d_writer.writeheader()
        print('Введите название заметки:')
        name_note = input()
        date_time_last_save = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print('Введите текст заметки:')
        text_note = input()

        with open("file.csv", "a", newline="", encoding="utf-8") as note:
            writer = csv.writer(note, delimiter=";")
            writer.writerow([name_note, date_time_last_save, text_note])
            print("Заметка успешно создана!")

    def list_note(self):
        print('Список заметок:')
        with open("file.csv", encoding="utf-8") as note_list:
            reader = csv.DictReader(note_list, delimiter=";")
            for row in reader:
                print(row["name_note"])

    def select_note(self):
        print("Введите название заметки:")
        name = input()

        with open("file.csv", encoding="utf-8") as line:
            reader = csv.DictReader(line, delimiter=";")
            for i, row in enumerate(reader):
                if row["name_note"] == name:
                    self.number_line = i
                    print(
                        "Выберете действие с заметкой:\n1) Посмотреть заметку\n2) Изменить заметку\n3) Удалить заметку")
                    count = input()
                    if count == "1":
                        with open("file.csv", encoding="utf-8") as csv_file:
                            csv_reader = csv.reader(csv_file)
                            rows = list(csv_reader)
                            print(rows[self.number_line + 1])
                    if count == "2":
                        with open("file.csv", encoding="utf-8", newline='') as source, open("new_file.csv", "w", encoding="utf-8", newline='') as dest:
                            reader = csv.reader(source, delimiter=';')
                            writer = csv.writer(dest, delimiter=';')
                            for line, rows in enumerate(reader):
                                if line != self.number_line + 1:
                                    writer.writerow(rows)
                                if line == self.number_line + 1:
                                    date_time_last_save = str(
                                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                    print("Введите новый текст:")
                                    new_text = input()
                                    writer.writerow(
                                        [row["name_note"], date_time_last_save, new_text])
                        shutil.copy2(r"new_file.csv", r"file.csv")
                        os.remove('new_file.csv')
                    if count == "3":
                        with open("file.csv", newline='') as source, open("new_file.csv", "w", newline='') as dest:
                            reader = csv.reader(source, delimiter=';')
                            writer = csv.writer(dest, delimiter=';')
                            for line, row in enumerate(reader):
                                if line != self.number_line + 1:
                                    writer.writerow(row)
                        shutil.copy2(r"new_file.csv", r"file.csv")
                        os.remove('new_file.csv')
                        print("Заметка успешно удалена!")
            if self.number_line == None:
                print("такой заметки нет!")
