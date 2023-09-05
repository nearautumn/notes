from modules import *

notes = 'notes.csv'

print('Программа "Заметки". Выберите действие: ')

print('1 - Показать все заметки.',
      '2 - Добавить заметку.',
      '3 - Выбрать заметку.')

select = input()
match select:
    case '1':
        show_notes(file=notes)
    case '2':
        add_note(file=notes)
    case '3':
        pick_note(file=notes)
    case _:
        print('Неверный ввод!')
