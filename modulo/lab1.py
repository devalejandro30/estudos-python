import math

def calcular(x, y, z):
  # w = x * y < z / x or x / y > z* x and z * y < x
  # t = max(x + y, y + z, z + x, round(float(x + y) / 2, 2))
  # r = abs(x * y) + z * y > max(x,y, z)
  # s = round(x / y + z) * (x * y * z / x)
  # u = round(x / y + z) == int(z / y) or float(x) > z
  # n = math.ceil(z / y) * math.floor(x / 2) + abs(x * y) + max(x, y, z)
  # m = (x + y > z) * 10 + int(z / y) + round(x * y, 1) * abs(z)
  # k = min(x, y, z) * -1 < math.ceil(z / x) and x != y
  # a = abs(x) * math.floor(y / z) > x + y % 2
  # d = float(abs(x) + round(y / min(x, y, z) * -1))
  # f = max(x, y) == x and round(z / y) != 0
  # v = float(x) / int(y) + abs(z) <= x * y
  h = int(x / y) == float(z) and abs(z * x) >= y # 15
  print(h)
# mudar os valores
calcular(3, 2.5, -4), 
calcular(2, 3.8, -1)
calcular(5, 2.1, -5)


