#List Comprehension represent the creation of new list from iterable object.
#Example:-
'''new_list=[expression-for item-in object-if_else statement]'''

#A)Without comprehension
'''a=[0,1,2,3,4,5,6,7,8,9]
b=[]
for i in a:
    b.append(i+1)
print(b)'''

#B)With Conprehension
'''a=[0,1,2,3,4,5,6,7,8,9]
b=[i+1 for i in a]
print(b)'''

#C)Like this way also
'''b=[i+1 for i in range(10)]
print(b)'''


#Print even number till 21
'''even=[]
for i in range(21):
    if i%2==0:
        print(i)
        continue
    else:
        print'''


#Print modulus of 2 and 3
'''TT=[i for i in range(21) if i%2==0 and i%3==0]
print(TT)'''

#Create a square of first 10 integer
'''SQ=[i*i for i in range(1,11)]
print(SQ):

SQ=[]
for i in range(1,11):
    SQ.append(i*i)
print(SQ)'''

#Print the name startswith nd endswith
'''grammer=['rajesh','somesh','saurabh','ankita','ramesh','nagesh']
for i in grammer:
    if i.startswith('r'):
        print(i)'''

'''grammer=['rajesh','somesh','saurabh','ankita','ramesh','nagesh']
for i in grammer:
    if i.endswith('h'):
        print(i)'''

'''grammer=['rajesh','somesh','saurabh','ankita','ramesh','nagesh']
for grammer in grammer:
    if grammer[0]=='h':
        print(i)'''

#Retrive a given number wether it is a primr number is not
u=int(input('Enter the number:'))
n=1
count=0
while(n<=u):
    if u%n==0:
        count=count+1
    n=n+1
if(count==2):
    print(f'{u} is a prime number')
else:
    print(f'{u} is not a prime number')
        


