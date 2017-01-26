from person import Person

def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Add new Chainsaw Juggling Record Holder
        2. Search for record holder
        3. Update a record
        4. Delete a record
        5. Show all records
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice

def get_new_record_info():

    ''' Get title and author of new book from user '''

    name = input('Enter name of record holder: ')
    country = input('Enter Country of record holder: ')
    numOfCatches = int(input('Enter number of catches (as an integer): '))

    return Person(name, country, numOfCatches)

def message(msg):
    '''Display a message to the user'''
    print(msg)


def show_list(records):
        ''' Format and display a list of person objects'''

        if len(records) == 0:
            print ('* No records *')
            return

        for person in records:
            print(person)

        print('* {} record(s) *'.format(len(records)))

def ask_for_person_id():

    ''' Ask user for person id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')
