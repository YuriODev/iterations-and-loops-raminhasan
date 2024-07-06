# Your solution to Exercise 8

n = int(input())

for i in range(n):
  num = i + 1
  if num % 2 == 1:
    continue

  else:
    print(num, end=" ")
    
