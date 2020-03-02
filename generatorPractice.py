def myGenerator(start=0, stop=10):
    numlist=[num for num in range(0, 10)]
    loop = 1
    for num in numlist:
        print(str(loop) + 'of exec')
        if num % 2 == 0:
            print('yielded ' + str(num))
            yield num                       #The generator stops at yield and
            print('!!!after yield')         #returns the variable to where it was called
                                            #Codes after yield are executed when next loop starts.
        loop += 1


mygenthing = myGenerator()

for num in mygenthing:
    print('[*]my gen thing : ' + str(num))
    print('[*]NEXT')
    print()