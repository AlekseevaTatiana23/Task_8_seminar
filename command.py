from logger import input_data, print_data, put_data, delete_data, search_contact

def main_menu():
    play=True
    while play:
        command=int(input('Выберите функцию телефонного справочника:\n'
              '1. Показать все записи\n'
              '2. Записать данные\n'
              '3. Удалить данные\n'
              '4. Изменить данные\n'
              '5. Найти запись\n'
              '6. Выход\n'))
       
        while command < 1 or command > 6:
            print('Неверный ввод. Попробуйте еще раз')
            command = int(input())
            
        if command == 1:
            print_data()
        elif command == 2:
            input_data()
        elif command == 3:
            delete_data()
        elif command == 4:
            put_data()
        elif command == 5:
            search_contact()
        elif command == 6:
            play=False
            print("Всего доброго!")





