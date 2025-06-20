# print character array in python

from array import *
arr1 = array('u',['a','b','c','h'])
for element in arr1:
    print(element)


# print integer array in python

from array import *
arr1 = array('i',[4,6,8,3,9])
for element in arr1:
    print(element)
from array import *
#create array
arr1= array('i',[1,3,5,4,6,7,8])

#two ways to print array: one using values

for i in arr1:
    print(i)

#two ways to print array: one using index
for i in range(len(arr1)):
    print(arr1[i])



# create an array from another array

from array import *

arr1 = array('d', [1.5, 2.5, -3.5, 4])

arr2 = array(arr1.typecode, [a for a in arr1])
print("The arr2 elements are:")
for i in arr2:
    print(i)


# create an array from another array

from array import *
arr1= array('d',[1.5,2.5,-3.5,4])

arr2 = array(arr1.typecode,[a*3 for a in arr1])
print("The arr2 elements are:")
for i in arr2:
    print(i)


# retrieve the element of array using Index

from array import *

arr1 = array('i',[10,20,30,40,50])

n=len(arr1)
print ("the length of array is :" , n)

for i in range(n):
    print(arr1[i], end=' ')



# retrieve the element of array using Index using WHILE loop

from array import *

arr1 = array('i',[10,20,30,40,50])

n=len(arr1)
print ("the length of array is :" , n)
i=0
while i<n:
    print(arr1[i], end=' ')
    i+=1

# SLICE AN ARRAY

from array import *

x = array('i',[10,20,30,40,50])

# 1. create array y with elements from 1st to 3rd from x
y= x[1:4]
print(y)

# 2. create array y with elements from 0th till last element in x
y=x[0:]
print(y)

#create array y with last 4 elements from x

y= x[-4:]
print(y)


# SLICING AN ARRAY

from array import *

x = array('i',[10,20,30,40,50,60,70])

#create array y with last 4th element and with 3 elements towards right

for element in x[2:5]:
    print(element)

# Replae an array elements with other elemEnts i.e UPDATE AN ARRAY

from array import *

x = array('i',[10,20,30,40,50,60,70])

#create array y with last 4th element and with 3 elements towards right

x[1:3]= array('i',[5,7])

for element in x:
    print(element)


# ARRAY methods

from array import *

x = array('i',[10,20,30,40,50])
#append
x.append(30)
x.append(60)
print(x)

#insert
x.insert(1,99)
print(x)

#a.remove(x) - remove first occurence of x in an array a. Raises 'ValueError' if not found
x.remove(20)
print(x)

#pop() - remove last item from array
x.pop()
print(x)

#index()
n=x.index(30)
print(n)

#.tolist()
lst=x.tolist()
print("list :", lst)
print("array :", x)


# ARRAY methods-  write a program to accept marks of a student and find the total marks and percentage of marks.

from array import *

str = input("enter marks : ").split(' ')   #here marks will store as a string
#convert them to array

marks_array1= array('i', [int(i) for i in str])
#to find sum of marks
sum=0
for x in marks_array1:
    print(x)
    sum+=x

print("sum of marks : ",  sum)

#percentage of marks
n=len(marks_array1)
percent= sum/n
print("percentage of marks:", percent)



#PROGRAM TO ENTER THE values in empty array and also ask user which element he wants to search for its INDEX -


from array import *
arr1=array('i',[])
n= int(input("Hey User! how many values you need ?")) #This step is done to know the length of array

for i in range(n):
    x=int(input("enter the next value"))
    arr1.append(x)

print(arr1)

# To find index of search element in array

#ONE WAY: using For Loop-
val=int(input("enter the value to search"))

counter_search=0
for j in arr1:
    if j==val:
        print(counter_search)
        break
    counter_search+=1

#ANOTHER WAY : using built-in function
print(arr1.index(val))



#retrieve the elements from 2D ARRAY using indexing and display using FOR Loop







#retrieve the elements from 3D ARRAY using indexing and display using FOR Loop

from numpy import *

a=[[[1,2,3],[4,5,6]],
   [[7,8,9], [10,11,12]]]

#length of rows = len(a)
# length of columns = len(a[i])

for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k], end=' ')
        print()
    print()



