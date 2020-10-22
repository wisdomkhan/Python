fav_no = {}
k = int(input('Enter limit\n'))

for i in range(k):
    s = input('\nEnter Name:')
    n = input('Enter Fav no:')
    fav_no[s] = n

print('\n', fav_no, '\n')

for s, n in fav_no.items():
    print(s.title() + ' your fav no is ' + n + '.\n')
