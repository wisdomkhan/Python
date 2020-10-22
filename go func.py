p, dd = 'yes', {}


def take_input():
    global name
    global p
    global go
    name = input('\nWhat is your name?\n')
    go = input("\nWhat's your dream destination?\n")
    dd[name] = go
    p = input('\nIs there anyone else who wants to take the poll?(yes/no)\n')


while p != 'no':
    take_input()

for name, go in dd.items():
    print('\n' + name.title() + " would like to go to " + go.title() + '.')
