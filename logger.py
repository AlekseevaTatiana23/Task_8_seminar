
def input_data():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input("Введите отчество: ")
    phone = input('Введите телефон: ')
    
    with open('data.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{patronymic};{phone}\n')
            
 

def print_data():
    with open('data.csv', 'r', encoding='utf-8') as file:
        data_ = [line.strip() for line in file.readlines()]
        if data_:
            print(data_)
        else:
            print("Empty data!\n")
    return data_



def change_line(dataFile, numberRow):
    answer = input(f"Изменить данную запись\n{dataFile[numberRow]}?\nВведите ответ: ")
    while answer != 'да':
        numberRow = int(input('Введите номер записи: ')) - 1

    name = dataFile[numberRow].split(';')[0]
    surname = dataFile[numberRow].split(';')[1]
    patronymic = dataFile[numberRow].split(';')[2]
    phone = dataFile[numberRow].split(';')[3]

    answer = int(input(f"Какие данные Вы хотите поменять?\n"
                       f"1. Имя\n"
                       f"2. Фамилия\n"
                       f"3. Отчество\n"
                       f"4. Номер телефона\n"
                       f"Введите ответ: "))
    while answer < 1 or answer > 4:
        print("Вы ошиблись!\nВведите корректный номер от 1 до 4")
        answer = int(input(f"Какие данные Вы хотите поменять?\n"
                        f"1. Имя\n"
                        f"2. Фамилия\n"
                        f"3. Отчество\n"
                        f"4. Номер телефона\n"
                        f"Введите ответ: "))
    if answer == 1:
        name = name = input('Введите имя: ')
    elif answer == 2:
        surname = input('Введите фамилию: ')
    elif answer == 3:
        patronymic = input("Введите отчество: ")
    elif answer == 4:
        phone = input('Введите телефон: ')

    data_ = dataFile[:numberRow] + [f'{name};{surname};{patronymic};{phone}\n'] + \
                      dataFile[numberRow + 1:]
    if numberRow + 1 == len(dataFile):
            data_ = dataFile[:numberRow] + [f'{name};{surname};{patronymic};{phone}\n']
    with open('data.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_))
    print('Изменения успешно сохранены!')


def put_data():
        print("Какую именно запись по счету Вы хотите изменить?")
        data_=print_data()
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        if number_journal<len(data_):
            change_line(data_, number_journal)
        else:
            print("Выбранной записи не существует!\n")
   

def delete_data():
    print("Какую именно запись по счету Вы хотите удалить?\n")
    data_ = print_data()
    number_line = int(input('Введите номер записи: '))
    if number_line<len(data_):        # проверка, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_[number_line - 1]}\n')
        data_ = data_[:number_line - 1] + data_[number_line + 1:]
        with open('data.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_))
        print('Изменения успешно сохранены!\n')
    else:
            print("Выбранной записи не существует!\n")

