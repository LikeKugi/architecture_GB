from db import Database, Note
from menu import Menu


def main():
    progressing = True

    while progressing:
        Menu.print_main_menu()
        variant = input('choose one: ')
        if variant == '0':
            progressing = False
        else:
            _match_main_menu_variant(variant)


def note_main(note: Note):
    progressing = True

    while progressing:
        print(f'FILE: {note.title}')
        Menu.print_note_menu()
        variant = input('choose file variant: ')
        if variant in ('1', '2'):
            _match_note_menu_variant(variant, note.title)
        else:
            progressing = False


def _match_main_menu_variant(variant: str):
    match variant:
        case '1':
            Database.show_records()
        case '2':
            _create_new_record()
        case '3':
            _open_record()
        case '4':
            _delete_record()
        case _:
            pass


def _match_note_menu_variant(variant: str, title: str):
    print('menu', variant, title)
    match variant:
        case '1':
            _edit_record(title)
        case '2':
            Database.add_record(Database.get_record(title))
        case _:
            pass


def _create_new_record():
    title = input('title: ')
    description = input('description: ')
    record = Note.Note(title, description)
    Database.add_record(record)


def _delete_record():
    title = input('title: ')
    Database.delete_record(title)


def _open_record():
    title = input('title: ')
    note = Database.get_record(title)
    if note:
        note_main(note)


def _edit_record(title):
    print('editing')
    note: Note = Database.get_record(title)
    new_data = input('add new data: ')
    note.details += f'\n{new_data}'
    Database.add_record(note)
