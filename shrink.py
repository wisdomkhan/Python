guestlist=['Picasso','Einstein','Galelio','Bill']
for i in guestlist:
    print(i + ', you are envited to the dinner.')

print('\nHey, I just found a bigger dinner table. I am inviting more guests.\n')

guestlist.insert(0,'Donald')
guestlist.insert(2,'Dumbledore')
guestlist.append('Sunny Leone')

for i in guestlist:
    print(i + ', you are envited to the dinner.')
print('OOPS! my table couldnt arrive on time. I am sorry to inform that i can invite only 2 people')

while len(guestlist)!=2:
    out = guestlist.pop()
    print('I am sorry ' + out + ' I am unable to host your dinner.')

for i in guestlist:
    print(i + ', you are invited to the dinner.')

print(guestlist)

del guestlist[0]
del guestlist[0]

print(guestlist)