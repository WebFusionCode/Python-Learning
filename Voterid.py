age=int(input('Enter Your age:'))
##voter_id=input('Enter your voter id:')
if(age>=18):
    voter_id=input('Enter Your Voter id:')
    if(voter_id=='Yes' and voter_id=='YES'):
        print('You are eligible for vote')
    else:
        print('Get your voter id')
else:
    print('You are not eligible')
     
