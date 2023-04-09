import pandas as pd
import datetime

commands = ["Показать все заметки",
            "Создать новую заметку",
            "Удалить заметку",
            "Изменить заметку",
            "Найти все заметки по дате",
            "Найти заметку по номеру",
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
    data = pd.read_csv('file_note.csv', delimiter = ',', encoding = 'utf-8')
    o.close()
    if (not data.empty):
        print(data)
    else:
        information("Файл пуст ")      
       

def input_error():
    print('Ошибка ввода. Введите корректный пункт меню')

def empty_request():
    print('Искомая заметка не найдена')


def end_program(): 
    print('Программа завершена.')

def create_new_note():
    date_note = def_date()
    header = input('Введите заголовок заметки :')
    note_body = input('Введите текст заметки:')  
    return  date_note, header, note_body 

def def_date(): 
    while True:
        date_d = input("Укажите: 1 - текущая дата, или 2 - ввод произвольной даты ")
        match date_d:
            case '1' :
                d = str(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"))
                return d  
            case '2' :
                d = input_date()
                right = input(f" Введена дата : {d}. Подтвердите корректность ввода (y/n):")
                if (right in 'yYнН'):
                    return d
            case _ :
                print("Повторите ввод даты")

                
def date_corr(d:str):
    return d if len(d) > 1 else ("0" + d)
    

def input_date():
    d =  input ("Введите год (гггг):")[:4] 
    d = d + "." + date_corr(input("Введите месяц (01, 02 ... 12):"))[:2]  
    d = d + "." + date_corr(input("Введите число (01, 02 ... 31):"))[:2]
    return d

def find_note():
    information('Введите дату искомой записи :\n')
    while True:
        d = input_date()
        right = input(f" Введена дата : {d}. Подтвердите корректность ввода (y/n):")
        if (right in 'yYнН'):
            return d


def delete_confirm(note_ind:list, index:int):
    if index == None :
        return False    
    for ind, row in note_ind:
        if ind == index:
            information('Вы действительно хотите удалить заметку' )
            result = input(f' {row[0]} {row[1]} {row[2]} ? (y/n)').lower()
            break
    if result in 'нНYy':
        return True
    else:
        return False

def select_note(message:str):
    note = int(input(message)) + 1
    return note


def change_note(note:list):
    print('Введите новые данные (если изменения не требуютcя, нажмите Enter)')
    date_note = ""
    y_n = input("Изменить дату заметки ? (y/n): ")
    if (y_n in "yYнН") :
        date_note = def_date()
    header = input(f'Введите заголовок заметки ({note[0][1][1]}): ')
    note_body = input(f'Введите текст заметки ({note[0][1][2]}): ')
    return   date_note, header, note_body 
 

def information(text:str):
    print(text)
