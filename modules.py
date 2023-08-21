def read_file(file: str) -> list:
    with open(file, mode='r', encoding='utf-8') as notes_file:
        ls = []
        for line in notes_file:
            ls.append(line.strip())
        return ls


def show_notes(file: str):
    list_of_rows = read_file(file)
    user_view = [d.replace(';', '|') for d in list_of_rows]
    print(*user_view, sep='\n')



