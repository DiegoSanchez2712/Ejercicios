def staircase(n):
  escalera = n
  for i in range(n):
    space = " " * (n-i)
    stair = "#" * (n+1)
    print(space + stair)
