    '''
1) Dictionary is ordered collection of key-value pairs.
2) Dictionary is mutable type of data type we can modify it.
3) In Dictionary key should be unique and immutable and value can be of anytype
'''
d1={'1':'One','2':'Two'}
print(d1)
print(type(d1)) #Example of a ductionary

d1={}
print(d1) #Empty dictionary.

d1={(10):'Harsh','Class':['Pyhton']}
print(d1)

family={'dad':60,'mom':57,'brother':30,'Sister':26,'me':21}
for i in family:
    print(i)
'''print(family)
print(type(family)) #To fetch the normal dictionary datatype.
print(family.keys()) #To fetch the unique key of the dictionary.
print(family.values()) #To fecth the values of the paired keys.
print(family.items()) #To fetch all the items present in th dictionary.
print(family.get('mom')) #To fetch a specific value from dictionary.
print('uncle' in  family) # To chech that this key is exist or not it shows in true or false using in operator.
print(family.get('uncle','Does not exist in the given dictionary')) #To fetch the key in the dictionary if it doent exist then print the second sentence.
#To add one more key value pairs we use square brackets
family['uncle']=77
print(family)

#This is used to update the value in the current dictionary.
family['uncle']=80
print(family)

#This is used to update or add multiple value in the dictionary buy making one more dictionary data type. 
family2={'grandfather':90,'grandmother':86}
family.update(family2)
print(family)

#This is used to assign the same dictionary to another variable
pariwar=family
print(pariwar)
print(family)
#Here in this case the id will b same as of family that we only had showed that pariwar is equal to family
##if anyone of them get deleted then all data from sec assigned will also deleted due to both id are same
##print(id(pariwar))
##print(id(family))
##pariwar.clear()
##print(pariwar)
##print(family) #This will show empty string.

#
pariwar=family.copy()
print(pariwar)
#


d={'A': [1,2,3, {'B': [4,5,6, {'C': [7,8,9,{'D':[10,11,12, {'E': [13,14,15,'Hello']}]}]}]}]}
print(d ['A'] [3] ['B'] [3] ['C'] [3] ['D'] [3] ['E'] [3])'''

