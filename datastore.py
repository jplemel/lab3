import sqlite3

from person import Person

DB_NAME = 'chainsaw_record_holders.db'
TABLE = 'recordHolders'
ID = 'p_id'
NAME = 'name'
COUNTRY = 'country'
NUMOFCATCHES = 'numOfCatches'

def setup():
    '''Connect to database, creates book table if it doesn't exist.'''
    conn = sqlite3.connect(DB_NAME)
    createsql = 'CREATE TABLE IF NOT EXISTS {} ( {} INTEGER PRIMARY KEY, {} TEXT, {} TEXT, {} INTEGER )'.format(TABLE, ID, NAME, COUNTRY, NUMOFCATCHES)
    conn.execute(createsql)    # Creates an intermediate cursor object
    conn.commit()
    conn.close()

def add_person(person):
    ''' Add to db, set id, return Person'''

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    sql_template = 'INSERT INTO {}({}, {}, {}) VALUES (?, ?, ?)'.format(TABLE, NAME, COUNTRY, NUMOFCATCHES) # Autoincrement

    print(person.name)
    print(person.country)
    print(person.numOfCatches)

    sql_values = (person.name, person.country, person.numOfCatches)
    cur.execute(sql_template, sql_values)

    person_id = cur.lastrowid
    person.set_id(person_id)

    conn.commit()
    conn.close()

    return person

def update_record(p_id,new_person):
    '''Update book with given person_id'''

    record_update = new_person.name, new_person.country, new_person.numOfCatches

    sql = 'UPDATE {} SET {} = ?,?,? WHERE {} = ?'.format(TABLE, NAME, COUNTRY, NUMOFCATCHES, ID )

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(sql, (record_update, p_id))
    conn.commit()
    conn.close()

    return cur.rowcount > 0 # return True if rows were changed.

def get_records():

    ''' Return person from DB. With no arguments, returns everything. '''

    records = []

    sql = 'SELECT * FROM {}'.format(TABLE)


    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # This type of row can be accessed by column name
    cur = conn.cursor()
    rows = cur.execute(sql)

    for row in rows:

        person = Person(row[NAME], row[COUNTRY], row[NUMOFCATCHES], row[ID])
        records.append(person)

    conn.close()

    return records

def search_db(p_id):

    records = []

    sql = 'SELECT * FROM {} WHERE {} = ?'.format(TABLE,ID)

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    rows = cur.execute(sql,(p_id,))

    for row in rows:

        person = Person(row[NAME], row[COUNTRY], row[NUMOFCATCHES], row[ID])
        records.append(person)

    conn.close()

    return records
