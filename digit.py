digit=int(input('Eter your number:'))

if(digit<=9):
    print('Its a single digit number')
elif(digit>9 and digit<=99):
    print('Its a double digit number')
elif(digit>99 and digit<=999):
    print('Its a triple digit number')
elif(digit>999 and digit<=9999):
    print('Its a four digit number')
else:
    ('Enter a valid number')
