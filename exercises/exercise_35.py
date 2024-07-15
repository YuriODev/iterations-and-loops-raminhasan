# Your solution to Exercise 35

digits = int(input())
power_of_ten = 10 ** digits

for i in range(power_of_ten -1, 10 ** (digits - 1) - 1, -2):
    print(i, end=" ")
