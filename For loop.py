#display each character from a string

x='Hello'
for str in x[0:]:
    print (str)

#display odd numbers between 1 and 10
x=1
for i in range(1,11,2):
    print (i)

#check prime number - which has only  two factors 1 and itself
num= int(input("enter a number"))
for i in range(2,num):
    if num%i==0:
        print(num,"is not prime")
        break
else:
    print(num, "is prime")

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

#multiplication table
num=int(input("enter a number"))
for i in range(1,21):
    print(num*i)

#count the number of digits in a number
num=int(input("enter a number"))
count=0
while num>0:
    count=count+1
    num=num//10
print("count is :", count)

#count the vowels in a given sentence

#ONE WAY USING LIST
sentence= input("enter the sentence")
list1 =["a","e","i","o","u"]
count=0
for char in sentence:
    if char in list1:
        count=count+1
print(count)

#ANOTHER WAY :
sentence= input("enter the sentence")
vowels='aeiouAEIOU'
count=0
for char in sentence:
    if char in vowels:
        count=count+1
print(count)

#ARMSTRONG NUMBER CHECK
#A positive integer is called an Armstrong number of order n if
#abcd... = a^n + b^n + c^n + d^n + ...

#In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself.
#153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153"""

n=int(input("enter the number\n"))
sum=0
order=len(str(n))
copy_n =n
while n>0:
    digit=n%10
    sum= sum+digit**order
    n=n//10
if sum==copy_n:
    print(f"{copy_n} is an armstrong number")
else:
    print(f"{copy_n} is NOT an armstrong number")
