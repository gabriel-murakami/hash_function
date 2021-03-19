from math import floor

class HashTableSizeTooSmallError(Exception):
  def __init__(self, message="m deve ser maior que zero"):
    self.message = message
    super(HashTableSizeTooSmallError, self).__init__(self.message)

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

  temp = m * ((key * a) % 1)

  return int(floor(temp))
