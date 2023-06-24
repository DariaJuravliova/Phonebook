phonebook = []
import csv

def print_result():
    if len(phonebook) == 0:
        print('spisok pust')
    else:
        for contact  in phonebook:
            print(contact)


def search_name(last_name):
    result = []
    for contact in phonebook:
        if contact [0].lower() == last_name.lower():
            result.append(contact)
        if len(result) == 0:
            print ('contact s familiei', last_name.title(), 'ne naiden')
        else:
            print(*result)


def search_number(number):
    result = []
    for contact in phonebook:
        if number  in contact[2]:
            result.append(contact)
        if len(result) == 0:
            print ('contact s nomerom', number, 'ne naiden')
        else:
            print(result)


def add_contact():
    last_name = input ('vvedite familiu: ').title()
    name = input ('vvedite imea: ',).title ()
    number = input ('vvedite nomer telefona: ')
    phonebook.append([last_name, name, number])
    print(*phonebook, sep='\n')
          

def del_contact():
    last_name = input('vvedite familiu: ')
    for contact in phonebook:
        if contact[0].lower == last_name.lower():
            phonebook.remove(contact)
            print('contact udalion')
            return True 
    print  ('contact ne naiden')
    return False


def save_file():
    file_name = input ('vvedite imea faila: ')
    with open(file_name, 'a', encoding= 'utf-8') as file:
        for contact in phonebook:
            file.write (contact[0] + ' ' + 'contact[1]' + ' ' +  'contact[2]' + '\n')

def load_file():       
    with open ('phonebook.csv', 'r', encoding= 'utf-8') as file:
        reader = csv.reader(file, delimiter =',')
        for row in reader :
            phonebook.append(row)
            print(row)


while True:
    print ('1. pokazati vse contacti')
    print ('2. poisk contactov po familii ')
    print ('3. poisk kontactov po nomeru ')
    print ('4. dobaviti contact ')
    print ('5. udaliti contact')
    print ('6.sohraniti spravochnik v fail')
    print ('7. zagruziti spravochnik iz faila')
    print ('8. exit')
    choice  = int (input('viberite punct menu: '))
    if choice == 1:
        print_result()
    elif choice ==2:
        search_name(input ('vvedite familiu: '))
    elif choice == 3:
        search_number( input('vvedite nomer telefona: '))
    elif choice == 4:
        add_contact()
    elif choice == 5:
        del_contact()
    elif choice == 6:
        save_file()
    elif choice == 7:
        load_file()
    elif choice == 8:
        break
    else:
        print('nepravilnii vvod ')
