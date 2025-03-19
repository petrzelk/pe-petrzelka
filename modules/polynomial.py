from rational import rational as rational


class polynomial:
  """A custom polynomial class
  Form of p(x)=a+bx+cx**2+...
  """

  def __init__(self, coeffiecients: list):
    self.coefficients = coeffiecients
    self.reduce()
    self.length = len(self.coefficients)

  def __repr__(self):
    result = '<p(x)='
    for i in range(self.length):
      if self.coefficients[i] != 0:
        if self.coefficients[i] != 1 or i == 0:
          result += str(self.coefficients[i])
        if i >= 1:
          result += 'x'
        if i >= 2:
          result += '**' + str(i)
        if i != self.length - 1:
          result += '+'
    if result[-1] == '+':
      result = result[:-1]
    if result == 'p(x)=':
      result = 'p(x)=0'
    return (result+">")
  
  def __str__(self):
    result = 'p(x)='
    for i in range(self.length):
      if self.coefficients[i] != 0:
        if self.coefficients[i] != 1 or i == 0:
          result += str(self.coefficients[i])
        if i >= 1:
          result += 'x'
        if i >= 2:
          result += '**' + str(i)
        if i != self.length - 1:
          result += '+'
    if result[-1] == '+':
      result = result[:-1]
    if result == 'p(x)=':
      result = 'p(x)=0'
    return (result)

  def __add__(self, other):
    result = self.coefficients + [0] * (other.length - self.length)
    for i in range(other.length):
      result[i] += other.coefficients[i]
    return (polynomial(result))

  def __sub__(self, other):
    result = [0] * (other.length - self.length) + self.coefficients
    print(result)
    for i in range(other.length):
      result[-i - 1] -= other.coefficients[-i - 1]
    return (polynomial(result))

  def __rmul__(self, other):
    if isinstance(other, int):
      result = [i * other for i in self.coefficients]
    else:
      result = [0] * (self.length - 1) * (other.length - 1)
      for i in range(self.length):
        for j in range(other.length):
          result[i + j] += self.coefficients[i] * self.coefficients[j]
    return (polynomial(result))

  def __mul__(self, other):
    if isinstance(other, int):
      result = [i * other for i in self.coefficients]
    else:
      result = [0] * (self.length + other.length - 1)
      for i in range(self.length):
        for j in range(other.length):
          result[i + j] += self.coefficients[i] * other.coefficients[j]
    return (polynomial(result))

  def __floordiv__(self, other):
    if isinstance(other, int):
      result = [rational(i, other) for i in self.coefficients]
    else:
      dividend = self.coefficients.copy()
      divisor = other.coefficients
      result = []
      while len(dividend) >= len(divisor):
        if dividend[0] % divisor[0] == 0:
          result.append(dividend[0] // divisor[0])
        else:
          result.append(rational(dividend[0], divisor[0]))
        for i in range(len(divisor)):
          dividend[i] -= result[-1] * divisor[i]
        del dividend[0]
    return (polynomial(result))

  def __truediv__(self, other):
    if isinstance(other, int):
      result = [rational(i, other) for i in self.coefficients]
      dividend = [0]
    else:
      dividend = self.coefficients.copy()
      divisor = other.coefficients
      result = []
      while len(dividend) >= len(divisor):
        result.append(dividend[0] / divisor[0])
        for i in range(len(divisor)):
          dividend[i] -= result[-1] * divisor[i]
        del dividend[0]
    if all(i == 0 for i in dividend):
      return (polynomial(result))
    else:
      raise Exception("DivError: result not a polynomial")

  def __mod__(self, other):
    if isinstance(other, int):
      dividend = [0]
    else:
      dividend = self.coefficients.copy()
      divisor = other.coefficients
      result = []
      while len(dividend) >= len(divisor):
        result.append(dividend[0] / divisor[0])
        for i in range(len(divisor)):
          dividend[i] -= result[-1] * divisor[i]
        del dividend[0]
    return (polynomial(dividend))

  def reduce(self):
    while self.coefficients[-1] == 0 and len(self.coefficients) > 1:
      del self.coefficients[-1]

  def evaluate(self,n):
    result=self.coefficients[-1]
    for num in self.coefficients[-2::-1]:
      result*=n
      result+=num
    return(result)