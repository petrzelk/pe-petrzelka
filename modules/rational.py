class rational:
  """A custom fraction class"""

  def __init__(self, numerator: int, denominator: int = 1):
    self.num = numerator
    self.den = denominator
    self.reduce()

  def __repr__(self):
    return (f"<{self.num}/{self.den}>")
  
  def __str__(self):
    return (f"{self.num}/{self.den}")
  
  def __float__(self):
    return (self.num / self.den)

  def __int__(self):
    return (self.num // self.den)

  def __radd__(self, other):
    if isinstance(other, int):
      result = rational(self.num + other * self.den, self.den)
    else:
      result = rational(self.num * other.den + other.num * self.den,
                        self.den * other.den)
    result.reduce()
    return (result)

  def __add__(self, other):
    if isinstance(other, int):
      result = rational(self.num + other * self.den, self.den)
    else:
      result = rational(self.num * other.den + other.num * self.den,
                        self.den * other.den)
    result.reduce()
    return (result)

  def __rsub__(self, other):
    if isinstance(other, int):
      result = rational(other * self.den - self.num, self.den)
    else:
      result = rational(self.num * other.den - other.num * self.den,
                        self.den * other.den)
    result.reduce()
    return (result)

  def __sub__(self, other):
    if isinstance(other, int):
      result = rational(self.num - other * self.den, self.den)
    else:
      result = rational(self.num * other.den - other.num * self.den,
                        self.den * other.den)
    result.reduce()
    return (result)

  def __rmul__(self, other):
    if isinstance(other, int):
      result = rational(self.num * other, self.den)
    else:
      result = rational(self.num * other.num, self.den * other.den)
    result.reduce()
    return (result)

  def __mul__(self, other):
    if isinstance(other, int):
      result = rational(self.num * other, self.den)
    else:
      result = rational(self.num * other.num, self.den * other.den)
    result.reduce()
    return (result)

  def __floordiv__(self, other):
    result = self.num * other.den // self.den * other.num
    #result.reduce()
    return (result)

  def __rtruediv__(self, other):
    if isinstance(other, int):
      result = rational(self.den * other, self.num)
    else:
      result = rational(other.num * self.den, other.den * self.num)
    result.reduce()
    return (result)

  def __truediv__(self, other):
    if isinstance(other, int):
      result = rational(self.num, self.den * other)
    else:
      result = rational(self.num * other.den, self.den * other.num)
    result.reduce()
    return (result)

  def __mod__(self, other):
    result = self - rational(self // other) * other
    result.reduce()
    return (result)

  def __pow__(self, other):
    result = rational(self.num**other, self.den**other)
    return (result)

  def __eq__(self, other):
    return (self.num * other.den == other.num * self.den)

  def __ne__(self, other):
    return (self.num * other.den != other.num * self.den)

  def __lt__(self, other):
    return (self.num * other.den < other.num * self.den)

  def __gt__(self, other):
    return (self.num * other.den > other.num * self.den)

  def __le__(self, other):
    return (self.num * other.den <= other.num * self.den)

  def __ge__(self, other):
    return (self.num * other.den >= other.num * self.den)

  def __abs__(self):
    return (rational(abs(self.num), abs(self.den)))

  def reduce(self):

    def gcf(a: int, b: int) -> int:
      while b:
        a, b = b, a % b
      return (a)

    common = gcf(self.num, self.den)
    self.num //= common
    self.den //= common
    if self.den < 0:
      self.den *= -1
      self.num *= -1

  def reciprocal(self):
    result = rational(self.den, self.num)
    return (result)

  def inv(self):
    result = rational(self.den, self.num)
    return (result)

  def add(self, other):
    if isinstance(other, int):
      self.num, self.den = self.num + other * self.den, self.den
    else:
      self.num, self.den = self.num * other.den + other.num * self.den, (
        self.den * other.den)
    self.reduce()

  def subtract(self, other):
    if isinstance(other, int):
      self.num, self.den = self.num - other * self.den, self.den
    else:
      self.num, self.den = self.num * other.den - other.num * self.den, (
        self.den * other.den)
    self.reduce()

  def multiply(self, other):
    if isinstance(other, int):
      self.num, self.den = self.num * other, self.den
    else:
      self.num, self.den = self.num * other.num, self.den * other.den
    self.reduce()

  def divide(self, other):
    if isinstance(other, int):
      self.num, self.den = self.num, self.den * other
    else:
      self.num, self.den = self.num * other.den, self.den * other.num
    self.reduce()
