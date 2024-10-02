##Data Type.
##*Python data type are the classification or categorization og the data items.
##1. String:- String is a sequence of one or more character(it is enclosed with sinle,doubel,triple quote,
##    it is immutable type to datatype so that we cant modified it.)
##2. List
##3. Tuple
##4. Set
##5. Dictionary
##
##*Python type() is used to return the type of the storect data in the object  and variables.
##
##*By default print function print the output in the next line.
##*End argument/paramenter in the print function id used to add any string(End with whitespaces it does
##go to the next line).
##To find the length of a string then we have to use length function print(len())
##To find the index number then use print like this print(name of object([index number]))

##*Slicing
s='python-programming'
##print(s[2:3])  #t,
##print(s[2:3:-1])    #Blank Output
##print(s[-15:-16])  #Blank Output
##print(s[-15:-16:-1]) #hs
print(s[-6:7:-2])
print(s[4:-8])
print(s[9:-10])
print(s[22: :-6])
print(s[2:-22:-1])
print(s[15: :-2])
print(s[-15: :-2])
print(s[7:-1])

##Slicing Formulae in for loop
s=input('Enter a string:')
for i in range(-1,-len(s)-1,-1):
    print(s[i])

