guestlist=['Picasso','Einstein','Galelio','Bill']
for i in guestlist:
    print(i + ', you are envited to the dinner.')

print('Bill cant make it to the dinner.')
guestlist.remove('Bill')
guestlist.append('Rowling')

print('New guest list is :-', guestlist)
