import pandas as pd
import datetime

commands = ['Открыть файл заметок',
            "Показать все заметки",
            "Создать новую заметку",
            "Удалить заметку",
            "Изменить заметку",
            "Найти заметку",
            "Завершить работу с заметками "]
def main_menu() :
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    choice = ''
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 8:
                return choice
        except ValueError:
            print('Введите корректное значение :')


def show_notes():
    o = open('file_note.csv', mode = 'r')
    o.close()
    # data = pd.read_csv('phone_guide.csv',delimiter=',',encoding='cp1251')
    data = pd.read_csv('file_note.csv', delimiter = ',', encoding = 'utf-8')
    if (not data.empty):
        print(data)
    else:
        information("Файл пуст ")
        
# str(','.join(new_note))

def number_index(note_ind:list):
    list_index = []
    for  index, row in note_ind:
        list_index.append(index)
    count = 0
    while True:
        if count == 3: 
            return None
        row_index = (int(input('Введите индекс искомой заметки :'))) 
        if row_index in list_index:
            return row_index
        else:
            print(f'Введен некорректный индекс{row_index}')
            count += 1
       

def input_error():
    print('Ошибка ввода. Введите корректный пункт меню')

def empty_request():
    print('Искомая заметка не найдена')

# def show_find_contact(contact_dic):
#     for  index, row in contact_dic:
#         print(f' Индекс = {index}, контакт : {row}')

def end_program(): 
    print('До свидания. Программа завершена.')

def create_new_note():
    date_note = def_date()
    # last_name = input('Введите фамилию :')

    header = input('Введите заголовок заметки :')
    note_body = input('Введите текст заметки:')
    # phone = input('Введите телефон:')
    # comment = input('Введите адрес:')
    return  date_note, header, note_body  #, phone, comment

def def_date(): 
    while True:
        date_d = input("Укажите: 1 - текущая дата, или 2 - ввод произвольной даты ")
        match date_d:
            case '1' :
                d = datetime.date.today()
                return str(d.year) + "/" + date_corr(str(d.month)) + "/" + date_corr(str(d.day))
            case '2' :
                # d = input ("Введите год (гггг):")        
                # d = d + input ("Введите месяц (01, 02 ... 12):")  
                # d = d + input ("Введите число (01, 02 ... 31):") 
                d = input_date()
                right = input(f" Введена дата : {d}. Подтвердите корректность ввода (y/n):")
                if (right in 'yYнН'):
                    return d
            case _ :
                print("Повторите ввод даты")

                
def date_corr(d:str):
    if len(d) == 1 : d = "0" + d
    # print(" Введено : " + d)
        # return  ('0' + d)
    return d

def input_date():
    d = input ("Введите год (гггг):")        
    d = d + "/" + date_corr(input("Введите месяц (01, 02 ... 12):"))  
    d = d + "/" + date_corr(input("Введите число (01, 02 ... 31):"))
    # right = input(" Введена дата " + {d} + ". Подтвердите корректность ввода (y/n):")
    #             if (right in 'yYнН'):
    return d

def find_note():
    information_data('Введите дату искомой записи :\n')
    while True:
        d = input_date()
        right = input(f" Введена дата : {d}. Подтвердите корректность ввода (y/n):")
        if (right in 'yYнН'):
            return d
    #             if (right in 'yYнН'):
    # return find


# def delete_contact():
#     delete = input('Введите удаляемый контакт')
#     return delete


def delete_confirm(note_ind:list,index:int):
    if index == None :
        return False    
    for ind, row in note_ind:
        if ind == index:
            information('Вы действительно хотите удалить заметку' )
            result = input(f' {row[0]} {row[1]} {row[2]} ? (y/n)').lower()
                        #   ' {row[0]} {row[1]} {row[2]} ? (y/n)').lower()
            break
    if result in 'нНYy':
        return True
    else:
        return False

def select_note(message:str):
    note = int(input(message)) + 1
    return note


def change_note():
    print('Введите новые данные (если изменения не требуютcя, нажмите Enter')
    date_note = ""
    y_n = input("Изменить дату заметки ? (y/n): ")
    if (y_n in "yYнН") :
        date_note = def_date()
    # last_name = input('Введите фамилию :')

    header = input('Введите заголовок заметки: ')
    note_body = input('Введите текст заметки: ')
    # phone = input('Введите телефон:')
    # comment = input('Введите адрес:')
    return   date_note, header, note_body  #, phone, comment
 

def information(text:str):
    print(text)

def information_data(text:str):
    print(f'Введены данные : {text}')

