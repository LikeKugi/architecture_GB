from .Note import Note

records = {}


def show_records():
    for k, v in records.items():
        print(f'\n{k}: {v}\n')


def add_record(record: Note):
    records.setdefault(record.title, record)


def delete_record(record_id: str):
    records.pop(record_id)


def get_record(record_id: str):
    return records.get(record_id)