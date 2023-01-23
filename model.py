phone_book = []
path = 'phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)    

def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding = 'UTF-8') as file:
        date = file.readlines()
        for line in date:
            phone_book.append(line.strip().split(';'))

def save_phone_book(flag: int):
    global phone_book
    global path
    if flag == 2:
        date = []
        for line in phone_book:
            date.append(';'.join(line))
        with open(path, 'w', encoding = 'UTF-8') as file:
            date = file.write('\n'.join(date))
      
def search_contact(search: str):
    global phone_book
    search_result = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_result.append(line)
                break
    return search_result

def delete_contact(search: str):
    global phone_book
    search_result = []
    for line in phone_book:
        for field in line:
            if search == field:
                search_result.append(line)
                break      
    return search_result

def delete_operation(delete_contact: list, confirm: str):
    global phone_book
    if confirm == 'да':
        for line in phone_book:
            if line == delete_contact[0]:
                phone_book.remove(line)           

def change_operation(change_contact: list, new_info: list, confirm: str):
    global phone_book
    if confirm == 'да':
        for line in phone_book:
            for i in range(len(line)):
                if line[i] == change_contact[0][i]:
                    line[i] = new_info[i]

def differense_book():
    global phone_book
    global path
    old_book = []
    with open(path, 'r', encoding = 'UTF-8') as file:
        date = file.readlines()
        for line in date:
            old_book.append(line.strip().split(';'))
    res = [line for line in old_book + phone_book if line not in old_book or line not in phone_book]
    if not res:
        return 1
    else:
        return 2
