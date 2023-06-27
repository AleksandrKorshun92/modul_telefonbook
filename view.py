import text

def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}.{text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0<int(select)<int(len(text.main_menu)):
            return int(select)
        print(text.input_error)

def show_contacts(book: dict[int:dict[str,str]], message):
    if book:
        max_name = []
        max_phone = []
        max_comment = []
        for cnt in book.values():
            max_name.append(len(cnt.get('name')))
            max_phone.append(len(cnt.get('phone')))
            max_comment.append(len(cnt.get('comment')))
        size_name = max(max_name)
        size_phone = max(max_phone)
        size_comment = max(max_comment)
        print('\n'+'='*(size_name + size_phone + size_comment +7))
        for index, contact in book.items():
            print(f'{index:>3}. {contact.get("name"):<{size_name+1}} {contact.get("phone"):<{size_phone+1}} {contact.get("comment"):<{size_comment+1}}')
        print('=' * (size_name + size_phone + size_comment + 7) + '\n')
    else:
        print(message)

def print_message(message: str):
    print('\n'+'='*len(message))
    print(message)
    print('='*len(message)+'\n')

def add_contacts():
    new = {}
    for key, value in text.new_contact.items():
        new[key] = input(value)
    return new


def search_word() ->str:
    return input(text.search_word)

def remove_contact():
        a = input(text.remove_contact)
        b = int(input(text.remove_danger))
        if b == 1:
            return a     

def change_contact():
    return input(text.change)

def change_ct():
    new = {}
    for key, value in text.new_contact.items():
        new[key] = input(value)
    return new

