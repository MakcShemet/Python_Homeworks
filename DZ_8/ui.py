from logger import input_data, print_data, filter_data, change_data, delete_data

def interface():
    print('''Выберите режим работы с программой
                1 - запись данных
                2 - вывод данных
                3 - поиск данных
                4 - изменение данных
                5 - удаление данных
                ''')
    comand = int(input('Введите номер команды: '))
    while(comand < 1 or comand > 5):
        int(input('Введите корректный номер команды: '))
    if comand == 1:
        input_data()
    elif comand == 2:
        print_data()
    elif comand == 3:
        print('Введите параметры поиска через ";": ')
        filterString = input()
        filter_data(filterString)
    elif comand == 4:
        change_data()
    elif comand == 5:
        delete_data()