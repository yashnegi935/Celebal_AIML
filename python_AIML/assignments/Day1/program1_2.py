import time

start = time.perf_counter()

a = 10
b = 20
total = a + b

end = time.perf_counter()

print(f"Sum is {total}")
print(f"Time taken: {end - start} seconds")