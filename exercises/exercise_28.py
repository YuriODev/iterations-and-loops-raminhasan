# Your solution to Exercise 28

first_num = int(input())
multiplier = int(input())
total = first_num

for _ in range(multiplier):
  total += first_num

total -= first_num

print(total)