# saving each line of file in a list
name = 'C:/Users/HP/Documents/New folder/pyfirst.txt'
with open(name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
# to save each char as a =n element of list use only read() & not readlines()
