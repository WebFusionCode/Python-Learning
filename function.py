'''
[Fuction]
1) Built in function.
==>In order to use those type function we dont need to import any module.
2) Function define in module.
==>In order to use those type function we need to import any module.
3) User define function.
==>Function is a block of code wich perform a specific task it runs only when it is called .
'''
#How to create a function
##>>>def function_name():
##>>>     pass

'''def demo ():
    a=10
    b=20
    print(a+b)
    print('Here is your answer')

def display ():
    a=22
    b=47
    print(a*b)

display()
demo()'''

#Types of user define function.
'''1) Arguement
==> A varialbe wich is present in function call statement is called as arguements.
2) Parameter
==> A varaiable which is present in function header part is known as parameter.'''
#1)Function with no arguement and no return value.
#2)Function with arguement and no return.
#3)Function with no arguement but return.
#4)Function with arguement and with return.


#Example
#1)Function with no arguement and no return.
'''def show():
    a=10
    b=20
    c=a+b
    print(f"The addition of {a} and {b} is =", c)

show()'''

#2)Function with arguement and no return.
'''def show_1(a,b):
    c=a+b
    print(c)
a=10
b=20
show_1(a,b)'''

#3)Function with no arguement but return.
'''def show_2():
    a=10
    b=20
    c=a+b
    return c
print(show_2())'''

#4)Function with arguement and with return.
'''def show_3(a,b):
    c=a+b
    return c
a=10
b=20
print(show_3(a,b))'''



#Types of return value  user define function.
##Types of arguement
'''1)Positional arguement
2)Default arguement
3)Keyword arguement/Named arguement
4)Args arguement/kwargs arguement'''

##1)Positional arguement
##Simple interest calculation
##SI=(PxRxT)/100
##def simple_i(p,r,t):
##    print('Principle is',p)
##    print('Rate is', r)
##    print('Total is',t)
##    si=p*r*t/100
##    print(si)
##p=5000
##r=5
##t=1000
##simple_i(p,r,t)

##def simple_i(p,r,t):
##    print('Principle is',p)
##    print('Rate is', r)
##    print('Total is',t)
##    si=p*r*t/100
##    print(si)
##p=5000
##r=5
##t=1000
##simple_i(6000,10,2000)

##2) Default Arguement
'''Default values indicate that the function arguement will take value if no argument.'''

'''def simple_i(p,r,t=8): #Default values should be in last in the header parameter arguement.
    print('Principle is',p)
    print('Rate is', r)
    print('Total is',t)
    si=p*r*t/100
    print(si)
p=5000
r=5
##t=1000
simple_i(p,r)'''

##3)Keyword arguement/Named arguement
'''Keyword arguement or named argument are values that , when passed into a function, are identifiable
by specific parameter names.'''
'''def simple_i(t,p,r):
    print('Principle is',p)
    print('Rate is', r)
    print('Total is',t)
    si=p*r*t/100
    print(si)

simple_i(p=5000,r=20,t=5) '''# we are calling setting or giving the values in the caling argument itself so in header we can write in any matter
##it will take the value according to that

##4)Args arguement/kwargs arguement
'''The args stands for argument that are passed to the function whereas kwargs stands for keywords arguments which are passed along with
the value into the function'''

##def sum(*num): ##    *num is your local variable act as a tuple represented by single *. 
##    sum=0
##    for i in num:
##        sum = sum+i
##    print(sum)
##
##
####sum(10)
####sum(10,20)
##sum(10,20,30)


'''num={'num1':10,'num2':20,'num3':30} #How to add a dictionary if values is given by using th variabe
sum=0
for i in num:
    sum=sum+num[i]
print(sum)'''

'''def sum(**num): ##    *num is your local variable act as a dictionary represented by single **. 
    sum=0
    for i in num:
        sum = sum+num[i]
    print(sum)


##sum(10)
##sum(10,20)
sum(num1=10,num2=20,num3=30)''' 



    





        
