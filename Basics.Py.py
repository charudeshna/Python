'''id() :  Will give the memory address of the variable'''
a = 10
b = 20

print(id(a))
print(id(b))

c = 10
print(id(c))

print(id(10))
print(id(b))
print(id(10))

c = a
print(c)
print(id(c))

##########################
'''print() : Inbuilt func which will print the value to the console
print(value1, value2, value3,..., [sep=' '], [end="\n"])
'''

print("hello world","hello world")
print("hello world","hello world", sep="**")
print("hello world","hello world", sep="**",end='##')

##################################################################
'''It is used to represent the data of which type to perform an operation is called data types'''
''' In this we have 2 types '''
''' 1)Single D.T/ Individual D.T   2) Multivalue D.T or Collection D.T'''

'''Individual datatypes are data type where only one value can be assigned to an variable
It is classfied into 2 types 
 1) numeric D.T and boolean D.T 
 
1. integers (int) - it is a numeric D.T where value will be without decimal points
2. float (float) - it is a numeric D.T where value will be with Decimal points
3. complex(complaex() - it is a numeric D.T where value will be in the form of a+bj form where a is real part and bj is imaginary part
  bj imaginary part is must and should.
4. boolen (bool)
'''

'''type() : Will give the datatype of the variable'''

a = -10
print(type(a))

" type casting converting one data type into another "

''' int --> float, complex,boolean --> possible '''

a = 10
print(type(a))
print(float(a))
print(type(a))
print(complex(a))

print(bool(a))

c = 10
print(bool(c))


b = 100
print(float(b))
print('10.0')

'''-----------------------------------------'''

''' float --> int, complex,boolean --> possible '''
a = 10.0
print(int(a))

b = 13.4
print(complex(b))

c = 15.6
print(bool(c))


''' complex --> int, float not possible , boolean --> possible 

a = 14.5 + 3j
print(int(a))  # type error

b = 12.5+2j
print(float(b))  # type error

c = 12.2 + 1j
print(bool(c)) '''

'''boolean --> int, float,complex --> possible '''

a = True
print (a)
print(type(a))
print(int(a))
print(float(a))
print(complex(a))

######################################################################
print(bool(-1))
print (bool(1.0))
print(bool(1+0j))

print(bool(0))
print(bool(int()))

print(bool(0.0))
print(bool(float()))

print(bool(0j))
print(bool(complex()))

print(bool(False))
print(bool(bool()))

'''
1. Default value of int is 0 and int()
2. Default value of float is 0.0 and float()
3. Default value of complex is 0+0j/0j and complex()
4. Default value of boolean is False and bool()
'''

#############################################################
'''dir() : Will give the list of attributes'''
a = 1
b = 2
print(a + b)
print(dir(a))

################################################################
'''isinstance() : It is an inbuilt function. It will check if the value belongs to the 
given datatype or not. If yes, it will give True else False
Syntax : isinstance(value, datatype)
'''
print(isinstance(-7, int))      #True
print(isinstance(89, float))    #False
print(isinstance(2, int, float))        #TypeError
print(isinstance(2, (int, float)))

#######################################



