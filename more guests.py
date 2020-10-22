guestlist=['Picasso','Einstein','Galelio','Bill']
for i in guestlist:
    print(i + ', you are envited to the dinner.')

print('\nHey, I just found a bigger dinner table. I am inviting more guests.\n')

guestlist.insert(0,'Donald')
guestlist.insert(2,'Dumbledore')
guestlist.append('Sunny Leone')

for i in guestlist:
    print(i + ', you are envited to the dinner.')
