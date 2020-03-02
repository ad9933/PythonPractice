def eventHandler(isEventHappened, funcToUse):
    if isEventHappened:
        print(funcToUse(10, 20))

eventHandler(True, lambda a, b : 'event!' + str(a + b))   #return only.
                                        #lambda (args) : (value to return)
                                        #Java allows String + int caculation, but Python does not.