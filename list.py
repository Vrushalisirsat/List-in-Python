# LIST - list is a collection of elements of different datatypes.

#Syntax :- 1) list.obj = [val1,val2,...]
#          2) list_obj = list(array/tuple/list/set/dictionary/string)


'''
#Example :-

# __main__
x=[10,20,30]
print("x =",x)
print("Data Types of x =",type(x))
#end of __main__



# Accesing list Elements :-   Syntax -  list_obj_name[index]

# Example-

#__main__

x=[10,50,90]

print("Forward Indexes :")
print("x[0] = ",x[0])
print("x[1] = ",x[1])
print("x[2] = ",x[2])

print("Reverse Indexes :")
print("x[-1] = ",x[-1])
print("x[-2] = ",x[-2])
print("x[-3] = ",x[-3])


# Note :- List is mutable

#Example

#__main__

l=[44,55,66]
l.append(99)
l[0] = 88
del l[1]
print("list =",l)
#end of __main__


#Note - Creating list by using 2nd syantax

#Example-1 :

from array import *
#__main__
a=array("i",[32,45,69])
x=list(a)
print("a =",a)
print("x =",x)
#end of __main__

#Example-2 :

from array import *
#__main__
s="JACK"
x=list(s)
print("x =",x)
#end of __main__




#Example-3:

from array import *
#__main__

d={"A":65 , "B":66 , "C":67 , "D":68}
x= list(d)
print("x =",x)

y=list(d.values())
print("y =",y)
# __main__



# Retrieving list Element by using for-in loop -

#Example :-

#__main__

x=[10,20,30,40,50]
for v in x:
    print("v =",v)
#end of loop
#end of __main__




# NOTE :- list is a collection of elements of different data types.

from array import *
#__main__

x=[10,20,[45,67],array("i",[3,4,5]),{2,3,4},"JACK",(50,90),{"A":65,"B":66}]

for i in range(0,len(x)):
    print("x[i] =",x[i])
#end of loop

print("x[0] =",x[1][0])

#end of __main__
'''

# isinstance() function :-

from array import *
from collections.abc import *

#__main__

x=[10,1.1,array("i",[25,12]) , [2.2,3.3] , "JACK" , {"A":65 , "B":66 , "C":67} , {80,90} , (5.5,6.6)]

for p in x:
    if isinstance(p , Iterable):
        for y in p:
            print(y,end=" ")
        #end of inner loop
        print()
    else:
        print("p =" , p)
    #end of if
#end of loop
#end of __main__








