import model 
import view

def start():
    choice = ''
    set_notes = []
    while True:
        choice = view.main_menu()
        match choice:
            case 1 :
                model.open_file()
                view.information('\nФайл заметок успешно открыт\n')
            case 2:
                view.show_notes()
            case 3:
                new_note = list(view.create_new_note())
                new_note_input = model.add_new_note(new_note)
                view.information_data(new_note_input)
                view.information('Подтвердите ввод (1- записать, 2- отмена ввода) :')
                yes_now = int(input(">"))
                if(yes_now == 1):
                    model.write_new_note(new_note)
                    view.information(f'\n Заметка \n{new_note_input}, \
                                     \n успешно создана\n')
            case 4:
                del_note = view.select_note('Введите номер удаляемой заметки: ')
                note_ind = model.get_note(del_note)
                if note_ind != []:
                    # index = 0
                    # if len(note_ind) > 1:
                    #     index = view.number_index(note_ind)
                    # else:
                    index = int(note_ind[0][0])
                    if not index :
                            break
                    confirm = view.delete_confirm(note_ind,index)
                    if confirm :
                        model.delete_note(index)
                        view.information(f'\nЗаметка с индексом {index - 1} успешно удалена\n')
                else:
                    view.empty_request()
            case 5 :
                note = view.select_note('Введите номер изменяемой заметки: ')
                note_ind = model.get_note(note)
                if note_ind != [] :
                    # index = 0
                    # if len(note_ind) > 1:
                    #     index = view.number_index(note_ind)
                    # else:
                    index = int(note_ind[0][0])
                    if not index :
                            break
                    updated_note= view.change_note()
                    model.update_note(index, list(updated_note))
                    view.information(f'\n Заметка с индексом {index -1} успешно изменена\n')
                else:
                    view.empty_request()
            case 6 :
                find = view.find_note()
                set_notes = model.get_note_date(find)
                if len(set_notes) < 1:
                    view.information('Указанная заметка не найдена')
            case 7 :
                view.end_program()
                model.sort_exit()
                break
            case _ :
                view.input_error()