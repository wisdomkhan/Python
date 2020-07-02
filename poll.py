#python 3.7.1
respo={}
polling='yes'
while polling == 'yes':
 name=input("What is your name? ")
 place=input("Where would you like to go? ")
 respo[name]=place
 check=input("Anyone else? ")
 if check != 'yes':
   polling = 'no'
print("THANKS FOR POLLING")
print("_____RESULTS_____")
for name, place in respo.items():
  print(name + " would like to go to " + place + ".")