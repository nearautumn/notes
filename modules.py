import pandas as pd


def show_notes(file: str):

    notes = pd.read_csv(file, delimiter=';')
    print(notes)


