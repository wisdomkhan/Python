# adding is at the end of each line to make a complete line
name = 'C:/Users/HP/Documents/New folder/pyfirst.txt'
s = ''

with open(name) as file_object:
    lines = file_object.readlines()

for line in lines:
    s += line.strip() + " "

print(s, len(s))
