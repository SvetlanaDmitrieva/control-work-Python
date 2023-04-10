import csv
import shutil
import pandas as pd

def add_new_note (new_note:list):  
    string_inp = ''
    string_inp = str(','.join(new_note)).replace(',', ' ')
    return string_inp

def write_new_note(new_note:list):
    with open(r'file_note.csv', mode = 'a', encoding = 'utf-8') as w_f:
        file_writer = csv.writer(w_f, delimiter = ",", dialect = 'excel', lineterminator = '\r')
        file_writer.writerow(new_note)
    sort_exit()


def get_note(index_note:int):
    result = []
    o = open('file_note.csv', mode = 'r')
    file_data = csv.reader(o, delimiter = ",")
    for index,row in enumerate(file_data):
        if index_note == index :
            l_ind_row = (index,row)
            result.append(l_ind_row)
            break
    o.close()
    return result

def get_note_date(date_note:str):
    result = []
    o = open('file_note.csv', mode = 'r')
    file_data = csv.reader(o, delimiter = ",")
    for index,row in enumerate(file_data):
        if date_note in row[0] :
            l_ind_row = (index,row)
            result.append(l_ind_row)
    o.close()
    return result

def open_file():
    try:
        f = open('file_note.csv')
        f.close()
    except FileNotFoundError:
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


def update_note(index:int, new:list):
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
    sort_exit()


def renovationin(old_row:list, new_row:list):
    if (new_row[0] != ''):
        if (len(old_row[0]) > 10 and len(new_row[0]) == 10) :
            old_row[0] = new_row[0] + old_row[0][-9::]
        else:
            old_row[0] = new_row[0]
    old_row[1] = new_row[1] if new_row[1] != '' else old_row[1]
    old_row[2] = new_row[2] if new_row[2] != '' else old_row[2]
    return old_row


def sort_exit():
    with open('file_note.csv', 'r', encoding = 'utf-8') as f:
        readit = csv.reader(f, delimiter = ',')
        head_file = next(readit)
        thedata = list(readit)
    thedata.sort(key = lambda x: (x[0], x[1], x[2]))
    with open('file_note_n.csv', 'w' , newline = '', encoding = 'utf-8') as f:
        writeit = csv.writer(f, delimiter = ',')
        writeit.writerow(head_file)
        writeit.writerows(thedata)
    shutil.copyfile('file_note_n.csv', 'file_note.csv')
