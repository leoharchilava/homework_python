d = {}
def validate_number (p):
    if len(p) != 16 :
        return  False
    if p[0:3] != '+7-':
        return False
    if not (p[6] == '-'  and p[10]  == '-'  and p[13]  == '-'):
        return False


    actual_phone = p[3:6] + p[7:10] + p[11:13] + p[14:]

    digits = '0123456789'
    for ch in actual_phone:
        if not ch in digits:
           return False
    return True


def add_to_book(name,phone):
    d[name] = phone


while True:
    name = str(input('Введите имя: '))
    if name == 'q':
         print(d)
         break 
    phone = str(input('Введите номер: '))
    if phone == 'q':
        print()
        break
    if validate_number(phone):
        print('Number is okay, adding to book..')
        add_to_book(name,phone)
        print('New phone added')
    else:
        print('Number is incorrect, please give another')
    print (d)













