from pprint import pprint

class MyClass:
    "DOCSTR"
    #__doc__ = "this is doc str"        docstr can be edited directly like this too.
    def __init__(self, name, num):      #Must include 'self' argument to initializer.
        self.name = name                #Variable can be defined on a initializer.
        self.num = num

    def myMethod(self, num):
        tmp = 0
        while tmp < num:
            print(self.name + str(self.num))
            tmp += 1
                                                #Looks like python automatically passes instance it self to method's first argument.
    def anotherMethod(whatisthis, anotherarg):  #This line generates warning.
        print(whatisthis)
        print(anotherarg)

class Inherited(MyClass):
    def __init__(self):
        super().__init__('inherited class', 100)    #Calls superclass's initializer
        print('super : ')
        print(super())
        print(type(super()))
        print()

    

mc = MyClass("class name", 10)

print(mc.name + str(mc.num) + mc.__doc__)
help(MyClass) 
pprint(mc.__dict__)                     #Prints variables and values in class

mc.myMethod(5)
mc.anotherMethod('arg')
print()
print()

help(Inherited)                         #Also inherits docstr too.
ic = Inherited()                        #Superclass has two arguments givent to its initializer.
                                        #What happened here is that i didn't defined Inherited class's __init__,
                                        #So python automatically generated superclass's Initializer.
pprint(ic.__dict__)
ic.myMethod(5)

print('👍')                             #Python supports emoji???