a = (input('Enter a number\t'))
b = (input('Enter second number\t'))
try:
    print(float(a) + float(b))
except TypeError:
    print('Please enter numbers and not strings')
