
name = ['Inni', 'Bruno', 'March']
Inni = {
        'Type': 'Cat',
        'Owner': 'Asim'
       }
Bruno = {
        'Type': 'Dog',
        'Owner': 'Jim'
        }
March = {
        'Type': 'Armadillo',
        'Owner': 'Brinx'
        }
Pets = [Inni, Bruno, March]

for (i, j) in zip(name, Pets):
    print(i, ":-\n", j, "\n")
