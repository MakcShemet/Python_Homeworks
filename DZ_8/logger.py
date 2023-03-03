import os
from data_create import name_data, surname_data, phone_data, adress_data

filename = 'DZ_8\data.txt'
def print_data():    
    if os.path.exists(filename):
        print('\nВывод данных из файла: ')
        with open(filename, 'r', encoding = 'utf-8') as file:
            list_data = file.readlines()
            for el in list_data:
                print(el, end="")
    else:
        print('Файла не существует')

def input_data():
    print('Введите данные для записи в файл: ')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    with open(filename, 'a', encoding = 'utf-8') as file:
        file.write(f'{name}; {surname}; {phone}; {adress}\n')

def filter_data(filter_string):
    with open(filename, 'r', encoding = 'utf-8') as file:
        listData = file.readlines()
        listFilter = filter_string.split(';')       
        is_found = False
        for el in listData:
            count = 0
            temprecord = el.split(';')
            for record in temprecord:
                for elFilter in listFilter:
                    if elFilter.lower() in record.lower() and len(elFilter.lower().strip()) == len(record.lower().strip()):
                        count += 1
            if count == len(listFilter):
                is_found = True
                print(el)
        if not is_found:
            print('Таких записей не найдено')

def change_data():
    with open(filename, 'r', encoding = 'utf-8') as file:
        findedString = file.readlines()
        index = 1
        for el in findedString:            
            print(f'{index} {el}', end='')
            index +=1
        numString = int(input('Введите номер строки, которую хотите изменить: '))
        if numString-1 in range(len(findedString)):
            print('Введите новые данные: ')
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            adress = adress_data()
            findedString[numString-1] = f'{name}; {surname}; {phone}; {adress}\n'
            with open(filename, 'w', encoding = 'utf-8') as file:
                file.writelines(findedString)
        else:
            print('Такой строки в файле не существует')
    
def delete_data():
    with open(filename, 'r', encoding = 'utf-8') as file:
        deletedString = file.readlines()
        index = 1
        for el in deletedString:            
            print(f'{index} {el}', end='')
            index +=1
        numString = int(input('\nВведите номер строки, которую хотите удалить: '))
    if numString-1 in range(len(deletedString)):
        with open(filename, 'w', encoding = 'utf-8') as file:        
            del deletedString[numString-1]
            file.writelines(deletedString)
    else:
        print('Такой строки в файле не существует')
