import time
start_time = time.time()

n = [i for i in range(1, 11)]
print(n)
print(max(n), min(n), sum(n))

print(time.time() - start_time)
