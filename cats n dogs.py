with open('cats.txt', 'w') as f1, open('dogs.txt', 'w') as f2:
    f1.write('moly\nsheens\ndickey')
    f2.write('snooby\npooky\nmooney')
with open('cats.txt') as f1, open('dogs.txt') as f2:
    print(f1.read().rstrip())
    print(f2.read().rstrip())
