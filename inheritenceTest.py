class Person:
    def __init__(self, name):
        self.name = name
    
    def printThings(self):
        print(self.name)

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.name = name
        self.email = email

    def storeToSuper(self, name):
        print()
        print('super : ' + super().name)
        print('self : ' + self.name)

ep = EmailPerson('personName', 'ADDRESS')

ep.printThings()                            #Works.
#ep.storeToSuper('superName')               Error.
#                                           Dont know what exactly super() means.
ep.printThings()                            #I was understanding it like Java's super keyword, but looks like it is different.