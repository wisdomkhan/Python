n = int(input())
budget = []
revenue = []
for i in range(n):
    budget.append(float(input()))
    budget.sort()
for j in range(0, len(budget)):
    revenue.append(budget[j] * (len(budget) - j))
print(max(revenue))
