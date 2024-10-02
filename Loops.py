#Loop is a block of code or a set of code blocks that runs until the given value is not satisfy
#There are tow types of loop 1)For loop 2)While loop

#In for loop there is a range call parameter it contains three parameter start,stop,step
#The syntax for range using for loop is :-
##for i in range(10):
##    print('Hello, World!',i) #This will print the hello world upto 0to9
##
##for i in range(3,8):
##    print('Bye, World!',i)
##
##for i in range(1,10,3):
##    print('Stay, World',i)

##for i in range(1,11):
##    pass
##print(i)
##
##i=20
##for i in range(1,11):
##    pass
##print(i)

##for i in range(1,4):
##    print(i)
##    print(i)
##    print(i)
##print(i)
##
##for i in range(1,4):
##    print(i)
##    print(i+1)
##    print(i+2)
##print(i)

##for i in range(1,4):
##    print(i)
##    i=i+1
##
##for i in range(1,4):
##    i=i+1
##    print(i)

##For each value of outer loop, inner loop must be terminated
##for i in range(1,4):
##    for j in range(1,4):
##        print(i,j)
##
##for i in range(1,4):
##    print(i)
##    for j in range(1,4):
##        print(i,j)
##    print(j)
##print(i,j)

for i in range(1,4):
    print(i)
    if i==2:
        continue
print(i)

