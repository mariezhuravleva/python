from csv import DictWriter, DictReader
from os.path import exists

def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия','Имя','Номер'])
        f_writer.writeheader()

def get_info():
    info = ['Иванов','Иван','12-16-18']
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
    obj = {'Фамилия': lst[0], 'Имя': lst[1],'Номер': lst[2]}
    res.append(obj)
    with open('phone.csv', 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия','Имя','Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                break
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
            write_file('phone.csv', get_info())

main()