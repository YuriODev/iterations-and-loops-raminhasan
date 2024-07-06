# Your solution to Exercise 9

start = int(input())
stop = int(input())
multiple = int(input())

running = True

while running:
  num = start

  if num % multiple == 0:
    print(num, end=" ")

  else:
    pass
  start += 1

  if num == stop:
    running = False
    break
