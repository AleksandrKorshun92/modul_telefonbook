import json
phone_book ={}
path = 'phones.json'

def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book = json.load(file)
        return True
    except:
        return False

def save_file():
    try:
        with open(path,'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
        return False


def search(word: str) -> dict[int:dict[str,str]]:
    result = {}
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[i] = contact
    return result


def check_id():
    if phone_book:
        return max(list(map(int, phone_book))) + 1
    return 1

def add_contact(new:dict[str,str]):
    contact = {check_id(): new}
    phone_book.update(contact)

def change_contact(id_cnt, change_ct):
    phone_book[id_cnt] = change_ct
    

def remove_contact(id_cnt):
        phone_book.pop(id_cnt)