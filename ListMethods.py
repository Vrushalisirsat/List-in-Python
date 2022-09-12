# List Methods

# 1) list_obj.append(value/iterable) - it will add the given value or iterable in the end of list

'''

# Example :

#__main__

x=[10,20,30]
x.append(80)
print("x =",x)

#end of __main__



# 2) list_obj.insert(index,value/iterable) - it will insert the given element at the specified index.


# Example-1 :

#__main__
x=[10,20,30]
x.insert(1,90)
print("x = ",x)
#end of __main__



# Example-2 :

#__main__
x=[10,20,30]
x.insert(-2,90)
print("x = ",x)
#end of __main__




# Example-3 :

#__main__
x=[10,20,30]
x.insert(5,90)
print("x = ",x)
#end of __main__





# Example-3 :

#__main__
x=[10,20,30]
x.insert(-5,90)
print("x = ",x)
#end of __main__



# 3) list_obj.extend(array/list/tuple/string/set/dictionary) - it will add all the elements from the given iterable at the end of current list object.

# Example-1 :

from array import *
#__main__
x=[10,20,30]
a=array("i",[40,50])
t=(50,80,60)
x.extend(a)
x.extend(t)
print("x = ",x)
#end of __main__


# Example-2:

#__main__
x=[10,20,30]
d={"A":65 , "B":66}
s="JACK"
x.extend(d)
x.extend(d.values())
x.extend(s)
print("x = ",x)
#end of __main__



# 4) var=list_obj.count(element) :- it will count and return total number of occurances of given element in the list

#__main__
x=[10,20,30,40,30,20]
c=x.count(20.0)
print("c =",c)
#end of __main__


# 4) var=list_obj.index(element[,start_index[,end_index]]) :-

# Example-1 :

#__main__
try:
  x=[10,20,30,40,30,20]
  i=x.index(50)
  print("found at index : ",i)
except ValueError:
    print("Not Found")
#end of try
#end of __main__

# Example-2 :

#__main__

x=[10,20,30,40,30,20]
i=x.index(20.0)
print("found at index : ",i)

#end of __main__


# Example-3 :

#__main__
x=[10,20,30,40,30,20.0]
i=x.index(20.0,2)
print("found at index : ",i)
#end of __main__


# Example-4:

#__main__
try:
   x=[10,20,30,40,30,20.0]
   i=x.index(20.0,2,5)
   print("found at index : ",i)
except ValueError:
    print("Not found")
#end of __main__



# 4) list_obj.sort([reverse=True / False]) :- it will sort the current list in ascending or in decending order

# Example-1 : Ascending order

#__main__
x=[40,2.2,10,1.2]
x.sort()
print("x =",x)
# end of __main__


# Example-2 : descending order

#__main__
x=[40,2.2,10,1.2]
x.sort(reverse = True)
print("x =",x)
# end of __main__



# Example-3 : working for iterables

#__main__
x=[(10,20,30) , (10,40) , (5,30,10,90)]
x.sort()
print("x =",x)
# end of __main__



# 7) list_obj.reverse() :- it will reverse the content of the list.

#__main__
x=[50,30,10,40]
x.reverse()
print("x =",x)
#end of __main__


# 8) var=list_obj.pop([index) :- it will delete the last or element having specified index from the list and  return deleted element.

# Example-1 :-

#__main__
x=[50,30,10,40,50]
y=x.pop()
print("Deleted Element =",y)
print("x =",x)
#end of __main__



# Example-1 :-

#__main__
x=[50,30,10,40,50]
y=x.pop(1)
print("Deleted Element =",y)
print("x =",x)
#end of __main__


# 9) list_obj.remove(element) :- it will remove the first occurances of specified element from the list.

#__main__
x=[10,20,30,40,20,20.0,50]
x.remove(20.0)
print("x = ",x)


# 10) list_obj.clear() :- it will remove/clear all the element from the list.

#__main__
x=[10,20,30]
x.clear()
print("x = ",x)
# end of main

'''

# 11) new_list_obj = list_obj.copy() :- It will return a separate copy of the current list.

# __main
x=[10,20,30,40]
y=x.copy()

print("x =",x)
print("ID of x=",id(x))

print("y =",y)
print("ID of y=",id(y))
# end of __main__







