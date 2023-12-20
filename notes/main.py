from note import Note, save_notes_to_file, load_notes_from_file

def main():
    # Создание трех заметок
    note1 = Note.create_new("First Note", "This is the first note!")
    note2 = Note.create_new("Second Note", "This is the second note.")
    note3 = Note.create_new("Another Note", "Yet another note.")

    # Сохранение заметок
    save_notes_to_file([note1, note2, note3])

    # Вывод всех заметок на экран
    print("All Notes:")
    notes = load_notes_from_file()
    for note in notes:
        print(f"ID: {note.note_id}, Title: {note.title}, Body: {note.body}, Datetime: {note.created_at}")

    # Поиск заметки "Вторая запись." и изменение текста
    for note in notes:
        if note.title == "Second Note":
            note.body = "Modified second note."
    
    # Сохранение изменений
    save_notes_to_file(notes)

    # Вывод всех заметок после изменения
    print("\nAll Notes After Modification:")
    modified_notes = load_notes_from_file()
    for note in modified_notes:
        print(f"ID: {note.note_id}, Title: {note.title}, Body: {note.body}, Datetime: {note.created_at}")

    # Добавление новой заметки
    new_note = Note.create_new("Added Note", "This is the added note.")
    modified_notes.append(new_note)
    save_notes_to_file(modified_notes)

    # Удаление заметки "Это первая заметка!"
    for note in modified_notes:
        if note.title == "First Note":
            modified_notes.remove(note)
            break

    # Сохранение изменений после удаления
    save_notes_to_file(modified_notes)

    # Вывод всех заметок после добавления и удаления
    print("\nAll Notes After Addition and Deletion:")
    final_notes = load_notes_from_file()
    for note in final_notes:
        print(f"ID: {note.note_id}, Title: {note.title}, Body: {note.body}, Datetime: {note.created_at}")

if __name__ == "__main__":
    main()