def myfunc():
    def innerFunc():
        'this is doc str'
        #print('inner printing :' + __doc__) -> Error

    innerFunc()
    print('===End Inner Func===')

    help(innerFunc)

#help(innerFunc) -> innerFunc not defined!
myfunc()