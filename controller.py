import view
import model
import text


def starts():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_succesful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_succesful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contacts()
                model.add_contact(new)
                view.print_message(text.add_succesful(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                if result!= {}:
                    id_cnt = view.change_contact()
                    change_ct = view.change_ct()
                    model.change_contact(id_cnt, change_ct)
                    view.print_message(text.change_finish)
            
            case 7:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                if result!= {}:
                    id_cnt = view.remove_contact()
                    if id_cnt != None:
                        model.remove_contact(id_cnt)
                        view.print_message(text.remove_finish)
                    else:
                        view.print_message(text.remove_repeal)
            case 8:
                break

