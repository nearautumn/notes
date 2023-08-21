def show_notes(file: str):

    with open(file, mode='r', encoding='utf-8') as notes_file:
        ls = []
        for line in notes_file:
            ls.append(line.strip())
        user_view = [d.replace(';', '|') for d in ls]
        print(*user_view, sep='\n')


