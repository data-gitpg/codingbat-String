#print("Hello World")

# find second largest number in a list using a loop

lst = [2,5,3,7,56,34,67,33]

lst.sort()
print(lst)

print("first largest number is", lst[-1])
print("second largest number is", lst[-2])


#second method - find second largest number in a list using a loop

lst = [2,5,3,7,56,34,67,33]

lst.remove(max(lst))  #remove largest number from list
print(lst)  # print list without maximum number
print("second largest number is  ", max(lst))



#Swap two numbers
a,b = [int(x) for x in input("enter two numbers").split(',')]
temp=a
a=b
b=temp

print(a,b)

# Sum of two numbers - input in same line

a,b = [int(x) for x in input("enter two numbers").split()]
print ("the sum of a and b is", a+b)

# sum of  two numbers separated by commas and print sum

a,b = [int(x) for x in input("enter two numbers separated by commas").split(',')]
print ("the sum of a and b is", a+b)

#sum of two numbers using command line arguments

import sys

a= int(sys.srgv[1])
b= int(sys.argv[2])
c= a+b
print (c)

#sum of even numbers using command line arguments
import sys


args=sys.argv[1:]
print(args)
sum=0
for a in args:
    x= int (a)
    if x%2==0:
        sum+=x

print("sum of evens are: " , sum)



#here its above output . go to command prompt cmd . python test.py 5 6 o/p: 11


# swap two variables without using third variable
a1=5
b1=6
a1=a1+b1
b1=a1-b1
a1=a1+b1

print(a)
print(b)

#Check even or odd
num= int(input("enter a number"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

# find largest of three numbers

a,b,c = [int(x) for x in input("enter three numbers").split(',')]

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print (b)
elif c>a and c>b:
    print (c)

#Another way using max()
print(max(a,b,c))


#leap year check

year= int(input("enter the year"))
if year%100==0 and year%400==0:
    print(year ,"is a leap year")
elif year%4==0 and year%100!=0:
    print("{} is a leap year".format(year))
else:
    print(year, "is not a leap year")



#check prime number - which has only  two factors 1 and itself
num= int(input("enter a number"))
for i in range(2,num):
    if num%i==0:
        print(num,"is not prime")
        break
else:
    print(num, "is prime")

# generate fibonacci series
num= int(input("enter the number"))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    c= a+b
    a=b
    b=c
    print(c)

#factorial of number using loop and recursion
num= int(input("enter a number"))
fact=1
for i in range (1,num+1):
    fact=fact*i
print(fact)

#check palindrome (number or string)

word= input("enter a string")
reverse_string = word[::-1]
if reverse_string==word:
    print("Palindrome")
else:
    print("Not Palindrome")

#sum of digits of a number

num=int(input("enter a number"))
sum=0
while num>0:
    digit=num%10
    sum= sum+digit
    num=num//10
print("sum is", sum)

#string to check if it is PALINDROME or not

A = input("enter a string")
rev = A[::-1]
print(rev)
print (A)
if rev == A:
    print("string is palindrome")
else:
    print("Not a Palindrome")