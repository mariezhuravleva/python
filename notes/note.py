import csv
from datetime import datetime
import uuid

class Note:
    def __init__(self, note_id, title, body, created_at=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at if created_at else datetime.now()

    @classmethod
    def from_csv(cls, row):
        note_id, title, body, created_at = row
        return cls(note_id, title, body, datetime.fromisoformat(created_at))

    @classmethod
    def create_new(cls, title, body):
        note_id = str(uuid.uuid1())
        return cls(note_id, title, body)

def save_notes_to_file(notes):
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for note in notes:
            writer.writerow([note.note_id, note.title, note.body, note.created_at.isoformat()])

def load_notes_from_file():
    notes = []
    try:
        with open('notes.csv', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                note = Note.from_csv(row)
                notes.append(note)
    except FileNotFoundError:
        pass
    return notes

def add_note():
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    new_note = Note.create_new(title, body)
    notes = load_notes_from_file()
    notes.append(new_note)
    save_notes_to_file(notes)