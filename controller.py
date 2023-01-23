import view
import model

def start():
    user_choice = 0
    while user_choice != 9:
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book, 0)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book(1)
                view.save_success(2, 0)
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
                view.contact_success()
            case 5:
                change = view.change_contact()
                result = model.delete_contact(change)
                confirm = view.show_contacts(result, 3)
                remane = view.change_info(confirm)
                model.change_operation(result, remane, confirm)
                view.change_success(confirm)
            case 6:
                del_cont = view.delete_contact()
                result = model.delete_contact(del_cont)
                confirm = view.show_contacts(result, 2)
                model.delete_operation(result, confirm)
                view.delete_success(confirm)
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result, 1)
            case 8:
                result = model.differense_book()
                confirm = view.change_in_book(result)
                replace = view.changing_book(confirm)
                model.save_phone_book(replace)
                view.save_success(replace, replace)