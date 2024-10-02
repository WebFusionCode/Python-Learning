n=int(input('Enter any number:'))
f=1
count=0
while(f<=n):
    if  f%n==0:
        count=count+1
    f=f+1
if(count==2):
    print(f'{n} is a Prime Number')
else:
    print(f'{n} is a Composite Number')
