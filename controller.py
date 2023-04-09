import model 
import view

def start():
    model.open_file()
    choice = ''
    set_notes = []
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                view.show_notes()
            case 2:
                new_note = list(view.create_new_note())
                new_note_input = model.add_new_note(new_note)
                view.information(f'Введены данные : {new_note_input}')
                view.information('Подтвердите ввод (1- записать, 2- отмена ввода) :')
                yes_now = int(input(">"))
                if(yes_now == 1):
                    model.write_new_note(new_note)
                    view.information(f' Заметка \n{new_note_input}, \
                                     \n успешно создана')
            case 3:
                del_note = view.select_note('Введите номер удаляемой заметки: ')
                note_ind = model.get_note(del_note)
                if note_ind != []:
                    index = int(note_ind[0][0])
                    confirm = view.delete_confirm(note_ind,index)
                    if confirm :
                        model.delete_note(index)
                        view.information(f'\nЗаметка с индексом {index - 1} успешно удалена\n')
                else:
                    view.empty_request()
            case 4 :
                note = view.select_note('Введите номер изменяемой заметки: ')
                note_ind = model.get_note(note)
                if note_ind != [] :
                    index = int(note_ind[0][0])
                    updated_note = view.change_note(note_ind)
                    model.update_note(index, list(updated_note))
                    view.information(f'Заметка с индексом {index - 1} успешно изменена\n')
                else:
                    view.empty_request()
            case 5 :
                find = view.find_note()
                set_notes = model.get_note_date(find)
                if len(set_notes) < 1:
                    view.information('Заметки по дате не найдены')
                else:
                    for item in set_notes:
                        view.information(f'№ заметки:{item[0] - 1} :{item[1][0]} {item[1][1]} {item[1][2]}')
            case 6 :
                find = view.select_note('Введите номер искомой заметки: ')
                note_i = model.get_note(find)
                if len(note_i) < 1:
                    view.information('Заметка по номеру не найдена')
                else:
                    view.information(f'№ заметки:{note_i[0][0] - 1} :{note_i[0][1][0]} {note_i[0][1][1]} {note_i[0][1][2]}')                
            case 7 :
                view.end_program()
                model.sort_exit()
                break
            case _ :
                view.input_error()