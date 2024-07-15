# Your solution to Exercise 36

number_1 = int(input())
number_2 = int(input())

remainder = number_1 % number_2

while remainder != 0:
  number_1 = number_2
  number_2 = remainder
  remainder = number_1 % number_2

print(number_2)
