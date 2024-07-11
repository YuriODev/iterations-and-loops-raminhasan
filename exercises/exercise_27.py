# Your solution to Exercise 27

target = int(input())
denom = 1
pi = 1

while denom <= target:
  pi = 4 / denom
  denom += 2

print(pi)
