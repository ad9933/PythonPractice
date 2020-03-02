
numlist = [i for i in range (0, 10)]

for num in range(0, 5):
    from random import choice       #Useful function. randomly picks one element in list.
    print(choice(numlist))


#import also works out of loop.
print('[*]Out of loop choice ' + str(choice(numlist)))