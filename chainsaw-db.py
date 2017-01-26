#Main program
import sqlite3, ui, datastore

from person import Person

def handle_choice(choice):
     if choice == '1':
        add_new()

     elif choice == '2':
        search_records()

     elif choice == '3':
        update_record()

     elif choice == '4':
        delete_record()

     elif choice == '5':
        show_record()

     elif choice == 'q':
         quit()

     else:
         ui.message('Please enter a valid selection')


def add_new():
    '''Get info from user, add new book'''
    new_person = ui.get_new_record_info()
    person = datastore.add_person(new_person)
    ui.message('Record added: ' + str(person))

def search_records():
    '''Get choice from user and search records for that choice'''
    #ask for id
    p_id = ui.ask_for_person_id()

    records = datastore.search_db(p_id)
    ui.show_list(records)


def update_record():
    ''' Get choice from user, edit datastore, display success/error'''

    p_id = ui.ask_for_book_id()
    new_person = ui.get_new_record_info()

    if datastore.update_record(p_id,new_person):

        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')

#def delete_record():


def show_record():
    '''Fetch and show all records'''
    records = datastore.get_records()
    ui.show_list(records)


def quit():
    '''Perform shutdown tasks'''

    ui.message('Bye!')

def main():

    datastore.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
