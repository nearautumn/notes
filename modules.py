from datetime import datetime


def read_file(file: str) -> list:
    with open(file, mode='r', encoding='utf-8') as notes_file:
        ls = []
        for line in notes_file:
            ls.append((line.strip() + '\n'))
        return ls


def write_file(file: str, ls: list):
    with open(file, mode='w', encoding='utf-8') as notes_file:
        notes_file.writelines(ls)


def find_max_id(list_of_rows: list) -> int:
    note_id = []
    for i in range(1, len(list_of_rows)):
        id_now = str(list_of_rows[i])
        note_id.append(id_now[:id_now.find(';')])
    max_id = note_id[0]
    for i in note_id:
        if i > max_id:
            max_id = i
    return int(max_id)


def show_notes(file: str):
    list_of_rows = read_file(file)
    if list_of_rows:
        user_view = [d.replace(';', '|') for d in list_of_rows]
        print(*user_view)
    else:
        print('Заметок нет')
        return -1  # код ошибки


def add_note(file: str):
    list_of_rows = read_file(file)

    if not list_of_rows:
        list_of_rows.append('ID;Заголовок;Текст заметки;Дата изменения' + '\n')

    if len(list_of_rows) == 1:
        note_id = 0
    else:
        note_id = find_max_id(list_of_rows) + 1

    note_name = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    note_date = datetime.now()

    new_line = str(note_id) + ';' + note_name + ';' + note_text + ';' + str(note_date) + '\n'
    list_of_rows.append(new_line)
    write_file(file, list_of_rows)
    print('Запись успешно создана!')


def pick_note(file: str):
    if show_notes(file) == -1:
        pass
    else:
        user_id = input('Введите ID заметки, которую хотите выбрать: ')

        list_of_rows = read_file(file)

        for i in range(1, len(list_of_rows)):
            note = str(list_of_rows[i])
            if user_id == note[:note.find(';')]:
                note_id = user_id
                index = i
                print(f'1 - редактировать заметку {note_id}, \n'
                      f'2 - удалить заметку {note_id}')
                select_operation = input()
                match select_operation:
                    case '1':
                        edit_note(file, list_of_rows, index)
                    case '2':
                        delete_note(file, list_of_rows, index)
                    case _:
                        print('Неверный ввод!')
                return

        print('Нет такой заметки!')


def edit_note(file: str, list_of_rows: list, index: int):
    note_name = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    note_date = datetime.now()

    list_of_rows[index] = str(find_max_id(list_of_rows) + 1) + ';' + note_name + ';' + note_text + ';' \
                          + str(note_date) + '\n'

    write_file(file, list_of_rows)


def delete_note(file: str, list_of_rows: list, index: int):
    list_of_rows.pop(index)

    write_file(file, list_of_rows)
