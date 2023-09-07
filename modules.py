from datetime import datetime


def read_file(file: str) -> list:
    """
    Возвращает список, содержащий строки, прочитанные из файла. Каждый элемент списка
    получает в конце символ \n
    :param file: строка, содержащая в себе путь к файлу
    :return: список, в качестве элементов содержащий строки, прочитанные из файла
    """
    with open(file, mode='r', encoding='utf-8') as notes_file:
        ls = []
        for line in notes_file:
            ls.append((line.strip() + '\n'))
        return ls


def write_file(file: str, ls: list):
    """
    Записывает список в файл
    :param file: строка, содержащая в себе путь к файлу
    :param ls: список
    """
    with open(file, mode='w', encoding='utf-8') as notes_file:
        notes_file.writelines(ls)


def find_max_id(list_of_rows: list) -> int:
    """
    Находит максимальный ID в списке и возвращает новое значение, большее максимального на 1. Для корректной работы
    необходимо, чтобы ID находился в строке до первого символа ';'
    :param list_of_rows: список строк, прочитанных из файла notes.csv
    :return: int значение нового ID
    """
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
    """
    Выводит в консоль перечень всех заметок, содержащихся в файле. Позволяет отсортировать заметки по дате
    :param file: строка, содержащая в себе путь к файлу note.csv
    :return:
    """
    print('Показать все заметки или отсортировать по дате?')
    print('1 - Показать все')
    print('2 - Отсортировать по дате')
    user_input = input()
    list_of_rows = read_file(file)
    match user_input:
        case '1':
            if list_of_rows:
                user_view = [d.replace(';', '|') for d in list_of_rows]
                print(*user_view)
            else:
                print('Заметок нет')
                return -1  # код ошибки
        case '2':
            if list_of_rows:
                show_notes_by_data(list_of_rows)
            else:
                print('Заметок нет')
                return -1  # код ошибки
        case _:
            print('Неверный ввод!')


def add_note(file: str):
    """
    Добавляет заметку в файл notes.csv
    :param file: строка, содержащая в себе путь к файлу note.csv
    :return:
    """
    list_of_rows = read_file(file)

    if not list_of_rows:
        list_of_rows.append('ID;Заголовок;Текст заметки;Дата изменения' + '\n')

    if len(list_of_rows) == 1:
        note_id = 0
    else:
        note_id = find_max_id(list_of_rows) + 1

    note_name = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    note_date = datetime.now().date()

    new_line = str(note_id) + ';' + note_name + ';' + note_text + ';' + str(note_date) + '\n'
    list_of_rows.append(new_line)
    write_file(file, list_of_rows)
    print('Запись успешно создана!')


def pick_note(file: str):
    """
    Открывает меню работы с конкретной заметкой для ее редактирования или удаления
    :param file: строка, содержащая в себе путь к файлу note.csv
    :return:
    """
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
    """
    Позволяет отредактировать текст и тело заметки, при этом заметка приобретает новый ID и время создания
    :param file: строка, содержащая в себе путь к файлу note.csv
    :param list_of_rows: список строк, прочитанных из файла notes.csv
    :param index: индекс изменяемой строки в списке list_of_rows
    :return:
    """
    note_name = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    note_date = datetime.now().date()

    list_of_rows[index] = str(find_max_id(list_of_rows) + 1) + ';' + note_name + ';' + note_text + ';' \
                          + str(note_date) + '\n'

    write_file(file, list_of_rows)


def delete_note(file: str, list_of_rows: list, index: int):
    """
    Удаляет заметку
    :param file: строка, содержащая в себе путь к файлу note.csv
    :param list_of_rows: список строк, прочитанных из файла notes.csv
    :param index: индекс удаляемой строки в списке list_of_rows
    :return:
    """
    list_of_rows.pop(index)

    write_file(file, list_of_rows)


def show_notes_by_data(list_of_rows: list):
    """
    Выводит в консоль заметки в заданном пользователем интервале по дате
    :param list_of_rows: список строк, прочитанных из файла notes.csv
    :return:
    """
    print('Дата начала')
    start_day = input('Введите день: ')
    start_month = input('Введите месяц: ')
    start_year = input('Введите год: ')
    start_date = datetime(int(start_year), int(start_month), int(start_day))

    print('Дата окончания')
    end_day = input('Введите день: ')
    end_month = input('Введите месяц: ')
    end_year = input('Введите год: ')
    end_date = datetime(int(end_year), int(end_month), int(end_day))

    list_of_id = []
    for i in range(1, len(list_of_rows)):
        line = list_of_rows[i]
        date_str = line[-11:]
        date = datetime(int(date_str[:4]), int(date_str[5:7]), int(date_str[8:]))
        if start_date < date < end_date:
            print(line)
