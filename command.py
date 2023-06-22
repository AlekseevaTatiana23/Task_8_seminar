from logger import input_data, print_data, put_data, delete_data

def main_menu():
    play=True
    while play:
        data_=print()
        command=int(input('Выберите функцию телефонного справочника:\n'
              '1. Показать все записи\n'
              '2. Записать данные\n'
              '3. Удалить данные\n'
              '4. Изменить данные\n'
              '5. Выход\n'))
       
        while command < 1 or command > 5:
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
            play=False
            print("Всего доброго!")





