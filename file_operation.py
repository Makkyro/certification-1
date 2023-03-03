import json

import Note


def write_file(filename, array):
    with open(f'{filename}.json', 'w', encoding='utf-8') as f:
        buf_array = []
        for notes in array:
            buf_array.append(Note.Note.to_file(notes))
        json.dump(buf_array, f)


def read_file(filename):
    try:
        array = []
        file = open(f'{filename}.json', 'r', encoding='utf-8')
        notes = json.load(file)
        for n in notes:
            note = Note.Note(
                id=n[0], title=n[1], body=n[2], date=n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array