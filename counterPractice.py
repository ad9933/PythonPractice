from collections import defaultdict     #Also belongs to 'collections'
from collections import Counter
from collections import OrderedDict     #This dictionary keeps it's elements aligned while others does not.

from pprint import pprint

mystr = 'mystring'

mylist = [1, 1, 'mystring', 'mystring', mystr] 

listcounter = Counter(mylist)   #Counter counts each element's duplication in given list.
print(listcounter)
print(type(listcounter))        #type it returns is not a dictionary object.

print('mystring' == mystr)      #Python's '==' operation is same as that of 
                                #Java's Object.equals() method


pprint(listcounter)             #Pretty-prints python object.