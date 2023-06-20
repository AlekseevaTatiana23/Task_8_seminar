data_=[]
last_id=0

def input_data():
    global last_id
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input("Введите отчество: ")
    phone = input('Введите телефон: ')
    array = ['name', 'surname', 'patronymic', 'phone']
    if not exist_contact(0, " ".join(array)):
        last_id+=1
        array.insert(0, str(last_id))
        with open('data.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{patronymic};{phone}\n')
            print("Изменения успешно внесены!\n")
    else:
        print("Данные уже существуют!")
  

def print_data():
    global data_, last_id
    with open('data.csv', 'r', encoding='utf-8') as file:
        data_ = [line.strip() for line in file.readlines()]
        if data_:
            last_id = int(data_[-1].split()[0])
            print(data_, sep="\n")
        else:
            print("Empty data!\n")
    return data_



def change_line(dataFile, numberRow):
    answer = input(f"Изменить данную запись\n{dataFile[numberRow]}?\nВведите ответ: ")
    while answer != 'да':
        numberRow = int(input('Введите номер записи: ')) - 1
    if exist_contact(numberRow, ""):
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

    else:
        print("Данные некорректны!")


def put_data():
        global data
        print("Какую именно запись по счету Вы хотите изменить?")
        print_data(data_)
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        if number_journal<len(data_):
            change_line(data_, number_journal)
        else:
            print("Выбранной записи не существует!\n")
 

def delete_data():
    global data_
    data_=print_data()
    number_line = int(input('Введите номер записи: '))
    if exist_contact(number_line, ""):       # проверка, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_[number_line - 1]}\n')
        data_ = data_[:number_line - 1] + data_[number_line + 1:]
        with open('data.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_))
        print('Изменения успешно сохранены!\n')
    else:
        print("Выбранной записи не существует!\n")


   
def search_contact():
    search_data = exist_contact(0, input("Введите данные: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Данные не корректны!")


def exist_contact(rec_id, data):
        if rec_id:
         candidates = [i for i in data_ if rec_id in i.split()[0]]
        else:
            candidates = [i for i in data_ if data in i]
        return candidates
