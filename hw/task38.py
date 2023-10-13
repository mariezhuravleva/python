from csv import DictWriter, DictReader
from os.path import exists

file_name = 'hw/contacts.csv'

def create_file():
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()

def get_info():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    
    info = [last_name, first_name, patronymic, phone_number]
    return info

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res

def write_file(file_name, lst):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Отчество': lst[2], 'Номер телефона': lst[3]}

    existing_data = read_file(file_name)
    existing_data.append(obj)
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(existing_data)

def edit_contact(file_name, last_name_to_change):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    contact_found = False 
    for contact in res:
        if contact['Фамилия'] == last_name_to_change:
            print(f'Изменение контакта: {contact}')
            new_info = get_info()
            contact['Фамилия'] = new_info[0]
            contact['Имя'] = new_info[1]
            contact['Отчество'] = new_info[2]
            contact['Номер телефона'] = new_info[3]
            print(f'Контакт изменен: {contact}')
            contact_found = True
            break  
    if not contact_found:
        print('Контакт не найден.')
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(res)

def delete_contact(file_name, last_name_to_delete):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    contact_found = False
    for contact in res:
        if contact['Фамилия'] == last_name_to_delete:
            print(f'Удаление контакта: {contact}')
            res.remove(contact)
            print(f'Контакт удален')
            contact_found = True
            break
    if not contact_found:
        print('Контакт не найден.')
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(res)

def main():
    while True:
        command = input('Введите команду (r - чтение, w - запись, e - изменить контакт, d - удалить контакт, q - выход): ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists(file_name):
                break
            print(read_file(file_name))
        elif command == 'w':
            if not exists(file_name):
                create_file()
            write_file(file_name, get_info())
        elif command == 'e':
            last_name_to_change = input('Введите фамилию контакта для изменения: ')
            edit_contact(file_name, last_name_to_change)
        elif command == 'd':
            last_name_to_delete = input('Введите фамилию контакта для удаления: ')
            delete_contact(file_name, last_name_to_delete)

main()