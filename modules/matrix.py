class vector:
  def __init__(self,values: tuple):
    self.values=values
  def __repr__(self):
    return(f'0v{str(self.values).replace(' ',',')}')
  def __str__(self):
    return(f'({str(self.values).replace(' ', ', ')})')
  def 

class matrix:

  def __init__(self, values: list[list[int | float]]):
    self.values = values
    self.rows = len(values)
    self.columns = len(values[0])
    if any(i != self.columns for i in values):
      raise Exception('DimError: rows do not match in length')

  def __repr__(self):
    return (str(self))

  def __str__(self):
    return ('\n'.join(' '.join(str(j) for j in i) for i in self.values))

  def __add__(self, other):
    if isinstance(other, matrix):
      if self.rows==other.rows and self.columns==other.columns:
        result=[[self.values[i][j]+other.values[i][j] for
                j in range(self.columns)] for i in range(self.rows)]
        return(result)
      else:
        raise Exception('DimError: dimnsions mismatched')
    else:
      raise Exception(
          f"TypeError: unsupported operand types for +: 'matrix' and '{type(other)}'"
      )
  def __rmul__(self,other):
    pass
  
  def __mul__(self,other):
    pass