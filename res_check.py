l1 = ['huda', 'rida', 'kuda', 'asim', 'robert', 'jen', 'sarah']
l2 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for i in range(len(l1)):
    if l1[i] not in l2.keys():
        print(l1[i] + " please take the poll.")
    else:
        print(l1[i] + " thanks for taking the poll.")
