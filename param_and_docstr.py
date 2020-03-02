def myfunc(argthing, CONSTANT='CONST'):
    'doc thing'
    __doc__ = 'this is doc'     #Local Variable, Does nothing.

    print('argthing : ' + argthing)
    print('const : ' + CONSTANT)

myfunc('123', CONSTANT='changed')

help(myfunc)

print(myfunc.__doc__)

