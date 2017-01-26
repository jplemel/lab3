class Person:

    NO_ID = -1

    def __init__(self, name, country, numOfCatches, id=NO_ID):

        self.name = name
        self.country = country
        self.numOfCatches = numOfCatches
        self.id=id


    def set_id(self, id):
        self.id = id

    def __repr__(self):

        '''Optional, return an unambiguous representation of this object, helpful for debugging'''

        return 'Record Holder: id = {} Name = {} Country = {} Number of Catches = {}'.format(self.id, self.name, self.country, self.numOfCatches)

def __str__(self):


        id_str = self.id

        if id == -1:
            id_str = '(no id)'

        template = 'id: {} Name: {} Country: {} Number of Catches: {}'
        return template.format(id_str, self.name, self.country, self.numOfCatches)
