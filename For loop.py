#display each character from a string

x='Hello'
for str in x[0:]:
    print (str)

#display odd numbers between 1 and 10
x=1
for i in range(1,11,2):
    print (i)

#find duplicates in a list using loops(without set)

lst= [1,2,3,4,2,5,3,7]
demo_list= [x for x in lst if lst.count(x)>1]
print(demo_list)

#find duplicates in a list using loops(without set) and count also the duplicate elements

lst= [1,2,3,4,2,5,3,7]
new_list =[]
dup_list=[]
count_dup =0
for i in lst:
    if i not in new_list:
        new_list.append(i)
    else:
        dup_list.append(i)
        count_dup+=1

print(new_list)
print(dup_list)
print(count_dup)



print(len(demo_list))


#print even numbers from 1 to 100 using for loop . i am using for - else suite for my learning

for i in range(1,101):
    if i%2==0:
        print(i)
else:
    print("done")


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


# print a pyramid pattern using nested loops

"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

"""
n = int(input("Enter the number of rows"))
for i in range (n):
    for j in range (n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()


# print a pyramid different pattern using nested loops

n = int(input("Enter the number of rows"))
for i in range (n):
    for j in range (n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()




#equilateral triangle

n=40
for i in range(1,11):
    print(' '* (n-i) + '*  ' *(i))



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

#string to check if it is PALINDROME or not using loop.

#Using two pointer technique
#This approach involves using two pointers, one starting from the beginning and the other from the end of the string,
#moving towards the center
#while comparing characters. It is the most efficient because it checks only half the string and
#requires constant space.


s = input("enter a string") # string

i,j = 0, len(s) - 1  # two pointers

is_palindrome = True  # assume palindrome
while i < j:
    if s[i] != s[j]:  # mismatch found
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes")
else:
    print("No")





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



# Break the loop when number is found in list
#-------B R E A K ------------

num= int(input("enter the number"))
list= [2,4,10, 4.5,5,7,9,22,35]
i=0
for i in list:
    if i==num:
        print("found")
        break
    else:
        continue


# skip the number 5 in a loop from 1 to 10 (use continue)
#---------C O N T I N U E ------------------

i=0
for i in range(1,11):
    if i!=5:
        print(i)
    else:
        continue


# loop thru a dictionary and print key-value pairs


s = {"name":"priya", "1":"hello", "num1":"546"}
print("keys \tValues")
for k,v in s.items():

    print('{}  {}'.format(k,v))

#print numbers divisible by 3 and 5 in a range

for i in range(1,21):
    if i%3 ==0 and i%5 ==0:
        print(i)


#Using loop reverse a list without built-in functions

lst= ["hello","hi", 3,25]
num_lst =[]
a =len(lst)
#print(len(lst))
for i in range(a-1,-1,-1):
    num_lst.append(lst[i])
print(num_lst)


#write  a loop to remove all vowels from a string

str =input("enter the string")
vow = 'aeiou'
a=len(str)
new_list=[]
for i in str:
    if i not in vow:
        new_list.append(i)
print(new_list)



# Using a loop to convert a list of strings to a uppercase :


str = ["apple", "banana", "cherry"]
new_str=[]

for i in str:
    if i.islower():
        new_str.append(i.upper())
print(new_str)


# generate a list of square numbers using a loop

lst = [1,2,3,5,6]
new_lst=[]
for i in lst:
    a=i*i
    new_lst.append(a)
print(new_lst)

# Loop through a string and print only consonants


str = input("enter a string")
vow ='aeiou'
# here i am using new string as empty instead of new list .
new_string= ""
for i in str:
    if i not in vow:
        new_string += i
print(new_string)
       # new_list.append(i)




