# Your solution to Exercise 11

input = int(input())
numerator = 1
running = True
total = 0

while running:
  if numerator != input:
    denominator = numerator + 1
    total += (numerator / denominator)
    numerator += 1

  else:
    total += (numerator / (numerator + 1))
    running = False
    break

print(f'{total: .2f}')
