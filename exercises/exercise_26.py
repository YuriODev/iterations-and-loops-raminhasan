# Your solution to Exercise 26

target_number = int(input())


counter = 0
for number in range(100,1000):
  total = 0
  
  while number > 0:
    total += number % 10
    number //= 10

  if total == target_number :
    counter += 1

print(counter)