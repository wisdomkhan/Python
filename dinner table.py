c, f = 20, 0
while f < c:
    n = int(input('\nHow many people are there in dinner group?\n'))
    if n <= (c-f):
        print("\nWelcome! Let me show you your table.")
        f = f + n
    elif n >= (c-f) & (c-f) != 0:
        print("\nOops! There's room only for", (c-f), '.')
        ch = input("\nWould you like to accept the available no. of seats?\n")
        if ch.upper() == 'YES':
            print('\nWelcome! Let me show you your table.')
            break
        else:
            print('Thanks for visiting.')
            continue
if f == c:
    print('HOUSEFULL')
