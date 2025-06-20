#sum of a list of numbers using while loop

list=[10,20,30,40,50]
sum=0
i=0
while i<len(list):
    sum = sum+list[i]
    i=i+1
print(sum)

# Note the difference between while and for loop here:


#find the sum of numbers using For loop

lst=[10,20,30,40,50]
sum=0
for i in lst:
    sum=sum+i
print(sum)


#print even numbers from 1 to 100 using for loop . i am using for - else suite for my le

num=1
while num<=100:
    if num % 2==0:
        print(num)
    num+=1
else:
    print("Done")



#print multiplication table of a number 5

x=5
i=1
while i<=10:
    print ('{} * {} = {}'.format(x,i, x*i))
    i+=1



