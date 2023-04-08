import csv
import shutil
import pandas as pd

def add_new_note (new_note:list):  
    string_inp = ''
    string_inp = str(','.join(new_note)).replace(',', ' ')
    return string_inp

def write_new_note(new_note:list):
    # with open(r'phone_guide.csv', mode='a',encoding='cp1251') as w_f:
    with open(r'file_note.csv', mode = 'a', encoding = 'utf-8') as w_f:
        file_writer = csv.writer(w_f, delimiter = ",", dialect = 'excel', lineterminator = '\r')
        print(f'Строка ввода : {new_note[0]} {new_note[1]} {new_note[2]})')
        file_writer.writerow(new_note)
    sort_exit()

# def get_note(last_name:str):
#     coln = 0
#     result = []
#     o = open('file_note.csv', mode = 'r')
#     file_data = csv.reader(o, delimiter = ",")
#     for index,row in enumerate(file_data):
#         if row[coln] == last_name:
#             print(f'Индекс :{index} : {str(row)}')
#             l_ind_row = (index,row)
#             result.append(l_ind_row)
#     o.close()
#     return result

def get_note(index_note:str):
    # coln = 0
    result = []
    o = open('file_note.csv', mode = 'r')
    file_data = csv.reader(o, delimiter = ",")
    for index,row in enumerate(file_data):
        # if row[coln] == last_name:
        if index_note == index :
            print(f'№ заметки:{index - 1} :{row[0]} {row[1]} {row[2]}')
            l_ind_row = (index,row)
            result.append(l_ind_row)
    o.close()
    return result

def get_note_date(date_note:str):
    # coln = 0
    result = []
    o = open('file_note.csv', mode = 'r')
    file_data = csv.reader(o, delimiter = ",")
    for index,row in enumerate(file_data):
        # if row[coln] == last_name:
        if date_note == row[0] :
            print(f'№ заметки:{index-1}: {str(row[0])} {str(row[1])} {str(row[2])}')
            l_ind_row = (index,row)
            result.append(l_ind_row)
    o.close()
    return result

def open_file():
    try:
        f = open('file_note.csv')
        f.close()
    except FileNotFoundError:
        # with open('phone_guide.csv', mode='a',encoding='cp1251') as w_f:
        with open('file_note.csv', mode = 'a', encoding = 'utf-8') as w_f: 
            names = ["Дата","Заголовок","Заметка"]
            file_writer = csv.writer(w_f, delimiter = ",", 
                        lineterminator = "\r")
            file_writer.writerow(names)


def delete_note(index):
    with open('file_note.csv', 'r', newline = '') as source, open('file_note_n.csv', 'w', newline = '') as dest:
        reader = csv.reader(source, delimiter = ',')
        writer = csv.writer(dest, delimiter = ',')
        for line, row in enumerate(reader):
            if line == index:
                 continue 
            writer.writerow(row)  
    shutil.copyfile('file_note_n.csv', 'file_note.csv')

def update_note(index:int, new :list):
    with open('file_note.csv','r' ,newline = '') as source, open('file_note_n.csv', 'w', newline = '') as dest:
        reader = csv.reader(source, delimiter = ',')
        writer = csv.writer(dest, delimiter = ',')
        for line, row in enumerate(reader):
            if line == index:
                ren_new = renovationin(row, new)
                writer.writerow(ren_new) 
            else:
                writer.writerow(row)  
    shutil.copyfile('file_note_n.csv', 'file_note.csv')
    

def renovationin(row, new):
    row[0] = new[0] if new[0] != '' else row[0]
    row[1] = new[1] if new[1] != '' else row[1]
    row[2] = new[2] if new[2] != '' else row[2]
    # row[3] = new[3] if new[3] != '' else row[3]
    # row[4] = new[4] if new[4] != '' else row[4]
    return row

def sort_exit():
    # with open('phone_guide.csv', 'r',encoding='cp1251') as f:
    with open('file_note.csv', 'r', encoding = 'utf-8') as f:
        readit = csv.reader(f, delimiter = ',')
        head_file = next(readit)
        thedata = list(readit)
    thedata.sort(key = lambda x: (x[0], x[1], x[2]))
    # with open('phone_guide_n.csv', 'w',newline='',encoding='cp1251') as f:
    with open('file_note_n.csv', 'w' , newline = '', encoding = 'utf-8') as f:
        writeit = csv.writer(f, delimiter = ',')
        writeit.writerow(head_file)
        writeit.writerows(thedata)
    shutil.copyfile('file_note_n.csv', 'file_note.csv')
        # csvData = pd.read_csv("phone_guide.csv")
        # csvData.sort_values([csvData.columns[0], csvData.columns[1], csvData.columns[2]], 
        #             axis=0,
        #             ascending=[True, True, True], 
        #             inplace=True)
