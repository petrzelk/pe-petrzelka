class ring():
  """A custom psuado-mathematical ring class """

  def __init__(self, values:list ):
    self.values = values
    self.len=len(values)

  def __getitem__(self, key):
    if isinstance(key, int):
      return(self.values[key%self.len])
    elif isinstance(key, slice):
      if key.start!=None and key.stop!=None and key.step!=None:
        return([self.values[i%self.len] for i in range(key.start,key.stop,key.step)])
      elif key.start!=None and key.stop!=None:
        return([self.values[i%self.len] for i in range(key.start,key.stop)])
      else:
        # Behavior for no start/end not implimented.
        raise Exception( "IndexError: no start and ending given")
    else:
      raise Exception( "IndexError: indices not supported" )

  def __setitem__(self, key, newvalue):
    self.values[key%self.len]=newvalue

  def __contains__(self, item):
    return item in self.values