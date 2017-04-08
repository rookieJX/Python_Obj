# !/usr/bin/env python

import types

print '-------Original---------'
def displayNumType(num):
    print num , 'is',
    if isinstance(num,(int,long,float,complex)):
        print 'a number of type :',type(num).__name__
    else:
        print 'not a number at all!!'

displayNumType(9090)
displayNumType(230)
displayNumType(-2932)
displayNumType(-9.0+32j)
displayNumType('dasf')

print '-------Advance---------'

def displayNewNumType(num):
    print num, 'is',
    if type(num) == type(0):
        print 'an integer'
    elif type(num) == type(0L):
        print 'a long'
    elif type(num) == type(0.0):
        print 'a float'
    elif type(num) == type(0+0j):
        print 'a complex number'
    else:
        print 'not a number at all!!'

displayNewNumType(849)
displayNewNumType(28302895420938409280942309)
displayNewNumType(00230240320402000)
displayNewNumType(09.0242)
displayNewNumType(1203+9j)
displayNewNumType('lfsakfjal')

print '-------Impro---------'
def displayProNumType(num):
    print num, 'is',
    if type(num) == types.IntType:
        print 'an integer'
    elif type(num) == types.LongType:
        print 'a long'
    elif type(num) == types.FloatType:
        print 'a float'
    elif type(num) == types.ComplexType:
        print 'a complex number'
    else:
        print 'not a number at all!!'

displayProNumType(849)
displayProNumType(28302895420938409280942309)
displayProNumType(00230240320402000)
displayProNumType(09.0242)
displayProNumType(1203+9j)
displayProNumType('lfsakfjal')

