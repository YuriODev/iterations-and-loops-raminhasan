# Your solution to Exercise 16

steps = int(input())
line_length = steps - 1

for i in range(steps):
  print(' ' * (line_length - i), end="")
  print('#' * (i + 1))
