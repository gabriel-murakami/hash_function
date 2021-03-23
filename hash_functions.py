from math import floor

class HashTableSizeTooSmallError(Exception):
  def __init__(self, message="m deve ser maior que zero"):
    self.message = message
    super(HashTableSizeTooSmallError, self).__init__(self.message)

class ConstantOutOfRangeError(Exception):
  def __init__(self, message="Constante A deve satisfazer 0<A<1"):
    self.message = message
    super(ConstantOutOfRangeError, self).__init__(self.message)

def div_method(key, m):
  key = int(key)
  m = int(m)

  if m <= 0:
    raise HashTableSizeTooSmallError

  return key % m

def multi_method(key, m, a):
  m = int(m)

  if m <= 0:
    raise HashTableSizeTooSmallError

  if a <= 0 or a >= 1:
    raise ConstantOutOfRangeError

  temp = m * ((key * a) % 1)

  return int(floor(temp))
