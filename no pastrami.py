#python 3.7.1
sfin=[]
print ("Pastrami is out of stock")
sord=['pocket', 'submarine', 'pastrami', 'pastrami', 'club', 'open-faced', 'pastrami' ]
while('pastrami' in sord):
  sord.remove('pastrami')

for i in sord:
  print("I made your " +i+ " sandwich.")
  sfin.append(i)

print("______SANDWICHES MADE_______")
for i in sfin:
  print(i)