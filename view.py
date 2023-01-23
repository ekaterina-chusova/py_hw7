


def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл', 
                'Сoхранить файл', 
                'Новый контакт', 
                'Изменить контакт',
                'Удалить контакт', 
                'Найти контакт', 
                'Выйти из программы']

    print('\nВыберите пункт меню:')

    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    if user_input < 1 or user_input > 8:
        print('Ошибка ввода. Введите число от 1 до 8')
    return user_input 

def show_contacts(phone_book: list, flag: int):
    if len(phone_book) >  0:
        for item in phone_book:
            if flag == 2:
                confirm = input(f'Удалить контакт {item[0]} {item[1]} ({item[2]}) да/нет? ')
                return confirm
            elif flag == 3:
                confirm = input(f'Изменить контакт {item[0]} {item[1]} ({item[2]}) да/нет? ')
                return confirm
            else:
                print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        if flag in range(1, 4):
            print ('Контакты не найдены')
        else:    
            print ('Телефонная книга пустая или не загружена')

def load_success():
    print('Телефонная книга загружена успешно')

def new_contact():
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment

def save_success(flag: int, flag2: int):
    if flag == 2:
        print('Телефонная книга сохранена успешно')
    if flag2 == 2:
        exit()

def contact_success():
    print('Контакт сохранен успешно')

def find_contact():
    search = input('Введите искомое значение: ')    
    return search

def delete_contact():
    delete = input('Введите Имя и Фамилию контакта, который нужно удалить: ')    
    return delete

def delete_success(confirm: str):
    if confirm == 'да':
        print('Запись успешно удалена')
    elif confirm == 'нет':
        print('Удаление записи отменено')
    else:
        print('Ошибка ввода')

def change_contact():
    change = input('Введите Имя и Фамилию контакта, который нужно изменить: ')    
    return change

def change_info(confirm: str):
    if confirm == 'да':
        list = []
        name = input('Измените имя и фамилию контакта: ')
        phone = input('Введите новый номер телефона: ')
        comment = input('Введите новый комментарий к контакту: ')
        list = [name, phone, comment]
        return list

def change_success(confirm: str):
    if confirm == 'да':
        print('Запись успешно изменена')
    elif confirm == 'нет':
        print('Изменение записи отменено')
    else:
        print('Ошибка ввода')

def change_in_book(result: int):
    if result == 2:
        confirm = input('В телефонную книгу были внесены изменения. Сохранить изменения (да/нет)? ')
        return confirm
    else:
        print('Выход из программы')
        exit()

def changing_book(confirm: str):        
    if confirm == 'да':
        return 2
    elif confirm == 'нет':
        print('Выход из программы')
        exit()
    else:
        print('Ошибка ввода') 
    