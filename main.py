import datetime
import json
import os

# Глобальный список заметок
notes = []


# Функция для создания новой заметки
def create_note():
    print("Создание новой заметки")
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_at": created_at,
        "updated_at": updated_at,
    }
    notes.append(note)
    print("Заметка успешно создана!")


# Функция для просмотра списка заметок
def view_notes():
    print("Список заметок:")
    for note in notes:
        print(f"{note['id']}. {note['title']} ({note['created_at']})")
    if not notes:
        print("Список заметок пуст.")


# Функция для чтения заметок
def read_note():
    note_id = int(input("Введите ID заметки, которую вы хотите прочитать: "))
    for note in notes:
        if note["id"] == note_id:
            print("Заголовок:", note["title"])
            print("Текст:", note["body"])
            # print("Дата создания:", note["created_date"])
            print("Дата изменения:", note.get("modified_date", "неизвестно"))
            return
    print("Заметка с идентификатором", note_id, "не найдена.")


# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки, которую вы хотите отредактировать: "))
    for note in notes:
        if note["id"] == note_id:
            print(f"Редактирование заметки {note['id']}:")
            note["title"] = input("Введите новый заголовок заметки: ")
            note["body"] = input("Введите новый текст заметки: ")
            note["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Заметка успешно отредактирована!")
            return
    print("Заметка не найдена.")


# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки, которую вы хотите удалить: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            print("Заметка удалена!")
            return
    print("Заметка не найдена.")


# Функция для сохранения заметок в файл
def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)
    print("Заметки сохранены в файл.")


# Функция для загрузки заметок из файла
def load_notes():
    if os.path.isfile("notes.json"):
        with open("notes.json", "r") as f:
            data = json.load(f)
            for note in data:
                notes.append(note)


# Загрузка заметок из файла при запуске программы
load_notes()
# Основной цикл приложения
while True:
    print("Что бы вы хотели сделать?")
    print("1. Создать новую заметку")
    print("2. Посмотреть список заметок")
    print("3. Прочитать заметку")
    print("4. Отредактировать заметку")
    print("5. Удалить заметку")
    print("6. Сохранить заметки в файл")
    print("7. Выйти из приложения")
    choice = input("Введите номер выбранного действия: ")
    if choice == "1":
        create_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        read_note()
    elif choice == "4":
        edit_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        save_notes()
    elif choice == "7":
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
