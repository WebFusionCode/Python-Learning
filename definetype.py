a=10
print(a)
print(type(a))
##We can fetch the type of the object by using (type())
print(id(a))
##We can fecth the id or location of the saved object in the class by using (id())

a=12
print(a)
print(type(a))
print(id(a))

b='Harsh'
print(b)
print(type(b))
print(id(b))

a='Harry'
print(a)
print(type(a))
print(id(a))

a=[11,12]
print(a)
print(type(a))
print(id(a))

a=30
a=40
print(a)
print(type(a))
print(id(a))
##The output will be always the latest one in this case a is 40 will be printed





##Here we can write the string or anything using all these ways
a='Harsh'
print(a)

b="Harsh"
print(b)

c="""Harsh"""
print(c)

d='''Harsh'''
print(d)


##This is the normal addition 
a=10
b=20
print(a+b)

##This is the edition with some text output
a=10
b=20
print('Additiono of the numbers is',a+b)

a=10
b=20
print('Additiono of a and b numbers is',a+b)

##In this code the f stands for format that if we write a and b in the text igt will show
##the addition of 10 and 20 is like this its will show what ever you are defining the object.
a=10
b=20
print(f'Additiono of {a} and {b} numbers is',a+b)




##Taking the value from the user we use input function


##In these case the number will be added as a string because input function takes the value by default as a string
a=input('Enter the first number:')
b=input('Enter the second number')
print(f'Addition of {a} and {b} is:',a+b)

##To the value as a integer we use int before the input to define that the users value is integer as shown in the below code
a=int(input('Enter the first number:'))
b=int(input('Enter the second number'))
print(f'Addition of {a} and {b} is:',a+b)
