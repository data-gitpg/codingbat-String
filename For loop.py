#display each character from a string

x='Hello'
for str in x[0:]:
    print (str)

#display odd numbers between 1 and 10
x=1
for i in range(1,11,2):
    print (i)

#display numbers in descending order

for i in range(10,0,-1):
    print(i)

#display the elements of list using For Loop

lst= [10,20.5,'A','America']
for i in lst:
    print(i)

#find the sum of numbers using For loop

lst=[10,20,30,40,50]
sum=0
for i in lst:
    sum=sum+i
print(sum)

#NESTED LOOPS- we can write for loop inside while loop or a for loop inside another for loop.

for i in range(3):
    for j in range(4):
        print ("i=", i ,'\t', "j=", j )

#STAR PYRAMID
'''
*
* *
* * *
* * * *
* * * * *
* * * * * * '''

num = int(input("Enter the number of rows"))
for i in range (1, num+1):
    for j in range (1,i+1):
        print("*",end="")
    print()


#Another way
for i in range(1,7):
    for j in range(1,i+1):
        print('*', end='')
    print()

# Another way

for i in range(1,7):
    print('*'*(i))


#equilateral triangle
n=40
for i in range(1,11):
    print(''* (n-i) + '*' *(i))


#Another way
num= int(input("Enter the number of rows ::"))
for i in range(0,num):
    for j in range (0,num-i-1):
        print(end="")
    for j in range(0,i+1):
        print("*",end="")
    print()

#reverse the digit of a given number
num= input("Enter the number")
print(num[::-1])

#string to check if it is PALINDROME or not

A = input("enter a string")
rev = A[::-1]
print(rev)
print (A)
if rev == A:
    print("string is palindrome")
else:
    print("Not a Palindrome")

