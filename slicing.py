##*Slicing
##s='python-programming'
####print(s[2:3])  #t,
####print(s[2:3:-1])    #Blank Output
####print(s[-15:-16])  #Blank Output
####print(s[-15:-16:-1]) #hs
##print(s[-6:7:-2])
##print(s[4:-8])
##print(s[9:-10])
##print(s[22: :-6])
##print(s[2:-22:-1])
##print(s[15: :-2])
##print(s[-15: :-2])
##print(s[7:-1])
##
####Slicing Formulae in for loop
##s=input('Enter a string:')
##for i in range(-1,-len(s)-1,-1):
##    print(s[i])

x='Hello, World!'
##print(x[-1])
##print(x[-2])
##print(x[-3])
##print(x[-4])
##print(x[-5])
##print(x[-6])
print(x[0:5])
print(x[:14])
print(x[7:])
print(x[:])
print(x[: : -1])
print(x[14:7:-1])
print(x[: : 2])
print(x[: : -2])


a='Harsh'
b=x[2:6]
c=x[7:9]
z=a+' '+b+ ' '+c
print(z)
