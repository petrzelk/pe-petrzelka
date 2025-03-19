class vector:
  """A custom implementation of vectors.
  """
  def __init__(self,values: tuple):
    self.values=values
    self.dim=len(values)
    self.mag=sum(i**2 for i in values)**.5
    #self.dir=0 # Not implimented as this is not needed
    
  def __repr__(self):
    return(f'<{str(self.values)[1:-1]}>')
  
  def __str__(self):
    return(f'<{str(self.values)[1:-1]}>')
  
  def __getitem__(self, key):
    return(self.values[key])
  
  def __add__(self, other):
    if self.dim == other.dim:
      return(vector(tuple(self[i]+other[i] for i in range(self.dim))))
    else:
      raise Exception('DimError: mismatched dimensions')
  
  def __sub__(self, other):
    if self.dim == other.dim:
      return(vector(tuple(self[i]-other[i] for i in range(self.dim))))
    else:
      raise Exception('DimError: mismatched dimensions')
  
  def scale(self, other):
    return(vector(tuple(i*other for i in self.values)))
  
  def dot(self, other):
    if self.dim == other.dim:
      return(sum(self[i]*other[i] for i in range(self.dim)))
    else:
      raise Exception('DimError: mismatched dimensions')
  
  def cross(self, other):
    pass # Not implimented as it is unneeded.
  
  def ortho_proj(self, other):
    return(other.scale(self.dot(other)/other.dot(other)))


class matrix:
  """A custom implimentation of matrices.
  """
  def __init__(self, values: list[list[int | float]]):
    self.values = values
    self.rows = len(values)
    self.columns = len(values[0])
    if any(len(i) != self.columns for i in values):
      raise Exception('DimError: rows do not match in length')

  def __repr__(self):
    return (str(self))

  def __str__(self):
    return ('\n'.join(' '.join(str(j) for j in i) for i in self.values))

  def __getitem__(self, name):
    pass
  
  def __setitem__(self, name):
    pass

  def __add__(self, other):
    if isinstance(other, matrix):
      if self.rows==other.rows and self.columns==other.columns:
        result=[[self.values[i][j]+other.values[i][j] for
                j in range(self.columns)] for i in range(self.rows)]
        return(matrix(result))
      else:
        raise Exception('DimError: dimensions mismatched')
    else:
      raise Exception(
          f"TypeError: unsupported operand types for +: '<class 'matrix'>' and '{type(other)}'"
      )
      
  def __sub__(self, other):
    if isinstance(other, matrix):
      if self.rows==other.rows and self.columns==other.columns:
        result=[[self.values[i][j]-other.values[i][j] for
                j in range(self.columns)] for i in range(self.rows)]
        return(matrix(result))
      else:
        raise Exception('DimError: dimensions mismatched')
    else:
      raise Exception(
          f"TypeError: unsupported operand types for -: '<class 'matrix'>' and '{type(other)}'"
      )
    
  def __rmul__(self,other):
    if isinstance(other, vector):
      pass
    if isinstance(other, int|float):
      result=[[self.values[i][j]*other for
                j in range(self.columns)] for i in range(self.rows)]
      return(matrix(result))
    else:
      raise Exception(
          f"TypeError: unsupported operand types for *: '<class 'matrix'>' and '{type(other)}'"
      )
  
  def __mul__(self, other):
    if isinstance(other, matrix):
      if self.columns==other.rows:
        result=[[sum(self.values[i][k]*other.values[k][j] 
                     for k in range(self.columns)) 
                 for j in range(other.columns)] 
                for i in range(self.rows)]
        return(matrix(result))
      else:
        raise Exception('DimError: dimensions mismatched')
    else:
      raise Exception(
          f"TypeError: unsupported operand types for *: '<class 'matrix'>' and '{type(other)}'"
      )
      
  def __pow__(self, other):
    pass
  
  def transpose(self):
    pass
  
  def determinate(self):
    pass
  
  def inverse(self):
    pass
  
  def ref(self):
    pass
  
  def rref(self):
    pass
  
  
# Test statement
#print((2*matrix([[1,1],[1,2]]))*matrix([[1,2],[3,4]]))