'''
1) Tuple is also collection of same or different datatype of element.
2) Tuple is your immutable type of data type so we cannot modify it.
3) It is eclosed with in round braces (pranthises).
4) Tubple is a collection of different data items.
5) More than one value stored in single variable is called tuple describe by comma.
'''
a=(1,2,3,4)
print(type(a))

b=()
print(type(b)) #This is an empty string.

t1=(1,2,3,4,5)
t2=(6,7,8,9,10)
t3=t1+t2
print(t3) #Concatination of 2 tuple.

t1=(1,2,3)
print(t1*3) #Replication of t1 tuple.

t1=(1,2,3,4,4,5,6,7,7,8)
print(t1.count(4)) #Counting the repeated number or elements in the tuple.
