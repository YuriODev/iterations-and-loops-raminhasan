# Your solution to Exercise 10

pounds = int(input())
kilos = 0

for i in range(1, pounds + 1):
  kilos += 0.453
  print(f'{i}{kilos: .2f}')
