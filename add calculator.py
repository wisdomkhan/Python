flag = 'YES'
print('Enter NO to shut-down the calculator.')
while flag != 'NO':
    a = (input('Enter a number\t'))
    b = (input('Enter second number\t'))
    try:
        print('SUM = ', float(a) + float(b))
    except (TypeError, ValueError):
        if a == 'NO' or b == 'NO':
            flag = 'NO'
        else:
            print('Please enter numbers and not strings')
