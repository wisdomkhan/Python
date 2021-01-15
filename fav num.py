import json
try:
    with open('favNum.json') as f1:
        n = json.load(f1)
except FileNotFoundError:
    n = input('Enter your favourite number\t')
    with open('favNum.json', 'w') as f1:
        json.dump(n, f1)
else:
    print("Your fav no is " + n)
