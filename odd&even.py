odd = [i for i in range(1, 21, 2)]
print(odd)
even = [i for i in range(2, 21, 2)]
print(even)
add = 0
for i in range(0, 10):
    add = add + odd[i] + even[i]
print(add)

List = [i for i in range(1, 21)]
print(sum(List))