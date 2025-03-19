import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.rational import rational

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
  
  def __len__(self):
    return(self.dim)
  
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
    raise Exception("Not implimented")
  
  def ortho_proj(self, other):
    return(other.scale(self.dot(other)/other.dot(other)))


class matrix:
  """A custom implimentation of matrices.
  """
  def __init__(self, values: list[list[int | float]]):
    if len(values)==0:
      values=[[]]
      self.rows=0
    else:
      self.rows = len(values)
    self.values = values
    self.columns = len(values[0])
    if any(len(i) != self.columns for i in values):
      raise Exception('DimError: rows do not match in length')

  def __repr__(self):
    return (str(self))

  def __str__(self):
    return ('\n'.join(' '.join(str(j) for j in i) for i in self.values))

  def __getitem__(self, index):
    return (self.values[index])
  
  def __setitem__(self, index, newvalue):
    if isinstance(newvalue, type(self.values[index])) :
      if len(newvalue)==self.columns:
        self.values[index]=newvalue
      else:
        raise Exception('DimError: dimensions mismatched')
    else:
      raise Exception(f'TypeError: matrix can not have row of type {type(newvalue)}')

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
      if other.dim == self.rows:
        return vector(tuple(sum(other[k]*self[k][i] 
                                for k in range(other.dim)) 
                            for i in range(self.rows)))
      else:
        raise Exception( "DimError: dimensions mismatched")
    elif isinstance(other, int|float|rational):
      result=[[self.values[i][j]*other for
                j in range(self.columns)] for i in range(self.rows)]
      return(matrix(result))
    else:
      raise Exception(
          f"TypeError: unsupported operand types for *: '<class 'matrix'>' and '{type(other)}'"
      )
  
  def __mul__(self, other):
    if isinstance(other, vector):
      if self.columns == other.dim:
        return vector(tuple(sum(self[i][k]*other[k]
                                for k in range(other.dim)) 
                            for i in range(self.rows)))
      else:
        raise Exception( "DimError: dimensions mismatched")
    elif isinstance(other, matrix):
      if self.columns==other.rows:
        result=[[sum(self.values[i][k]*other.values[k][j] 
                     for k in range(self.columns)) 
                 for j in range(other.columns)] 
                for i in range(self.rows)]
        return(matrix(result))
      else:
        raise Exception('DimError: dimensions mismatched')
    elif isinstance(other, int|float|rational):
      result=[[self.values[i][j]*other for
                j in range(self.columns)] for i in range(self.rows)]
      return(matrix(result))
    else:
      raise Exception(
          f"TypeError: unsupported operand types for *: '<class 'matrix'>' and '{type(other)}'"
      )
     
  def identity(dimension):
    return(matrix([[int(i==row) 
                    for i in range(dimension)] 
                   for row in range(dimension)]))
  
  def __pow__(self, other):
    if self.columns==self.rows:
      result=matrix.identity(self.columns)
      for power in range(other):
        result*=self
      return(result)
    else:
      raise Exception('DimError: dimensions mismatched')
  
  def transpose(self):
    return(matrix([[self[j][i] 
                    for j in range(self.rows)] 
                   for i in range(self.columns)]))
  
  def determinant(self):
    if self.columns==self.rows:
      if self.rows==0:
        return(1)
      else:
        return(sum((-1)**(j)*self[0][j]*matrix([[self[a][b] 
                                                  for b in range(self.columns) if b!=j] 
                                                  for a in range(1,self.rows)
                                                  ]).determinant() 
                   for j in range(self.columns)))
    else:
      raise Exception('DimError: dimensions mismatched')
  
  def minors(self):
    if self.columns==self.rows:
      return(matrix([[ matrix([[self[a][b] 
                                for b in range(self.columns) if b!=j]
                                for a in range(self.rows) if a!=i]).determinant()
                     for j in range(self.columns)] 
                     for i in range(self.rows)]))
    else:
      raise Exception('DimError: dimensions mismatched')
  
  def cofactors(self):
    if self.columns==self.rows:
      temp=self.minors()
      return(matrix([[(-1)**(i+j)*temp[i][j] 
                      for j in range(temp.columns)]
                      for i in range(temp.rows)]))
    else:
      raise Exception('DimError: dimensions mismatched')
  
  def adjugate(self):
    return(self.cofactors().transpose())
  
  def inverse(self):
    return(self.adjugate() * rational(1,self.determinant()))
  
  def row_switch(self,row_1:int,row_2:int)->None:
    self[row_1],self[row_2] = self[row_2],self[row_1]
  
  def row_multiply(self,row:int, factor:int|float|rational)->None:
    self.values[row]=[factor*i for i in self.values[row]]
  
  def row_addition(self,row_1:int,row_2:int,factor:int|float|rational)->None:
    self.values[row_1]=[self[row_1][i]+self[row_2][i]*factor for i in range(self.columns)]
  
  def column_replace(self, column:int, newvalue):
    if isinstance(newvalue, list|vector):
      if len(newvalue)==self.rows:
        result=matrix([[self[i][j] for j in range(self.columns)] for i in range(self.rows)])
        for i in range(self.rows):
          result[i][column]=newvalue[i]
        return(result)
      else:
        raise Exception('DimError: dimensions mismatched')
    else:
      raise Exception(f'TypeError: matrix can not have column of type {type(newvalue)}')
  
  def ref(self):
    raise Exception('Not implemented')
  
  def rref(self):
    raise Exception('Not implemented')
  
  def cramers(self,b:vector)->vector:
    if isinstance(b, vector):
      if self.columns==b.dim:
        det=self.determinant()
        return(vector(tuple(self.column_replace(i,b).determinant()/det for i in range(self.columns))))
      else:
        raise Exception('DimError: dimensions mismatched')
    else:
      raise Exception(f'TypeError: b must be vector {type(b)} not supported')
  
