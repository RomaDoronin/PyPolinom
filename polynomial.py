class Polynomial:
  def __init__(self, varSet):
    if len(varSet) == 0:
      raise ValueError
    if not isinstance(varSet, (list, tuple)):
      raise ValueError
    if not all(map(lambda x: isinstance(x, int), varSet)):
      raise ValueError

    removeZeros = False
    initList = []
    for var in varSet:
      if (var != 0):
        removeZeros = True
      if (removeZeros):
        initList.append(var)
    self.varSet = initList

  # len
  def __len__(self):
    return len(self.varSet)

  # print
  def __str__(self):
    strRes = ""

    if (len(self.varSet)):
      count = len(self.varSet) - 1
      for i in self.varSet:
        if (i != 0):
          if (i > 0 and count != len(self.varSet) - 1):
            strRes += "+"

          if (i == -1 and count != 0):
            strRes += "-"
          elif (i == 1 and count != 0):
            pass
          else:
            strRes += str(i)

          if (count == 1):
            strRes += "x"
          elif (count != 0):
            strRes += "x^" + str(count)

        count -= 1
    else:
       strRes += "0"

    return strRes

  # *
  def __mul__(self, other):
    varSet = []
    if isinstance(other, int):
      assert other != 0
      for i in range(len(self)):
        varSet.append(self.varSet[i] * other)
      return Polynomial(varSet)
    elif isinstance(other, Polynomial):
      varSet = [0] * (len(self) + len(other) - 1)
      for i, x1 in enumerate(self.varSet):
        for j, x2 in enumerate(other.varSet):
          varSet[i + j] += x1 * x2
      return Polynomial(varSet)
    else:
      raise TypeError

  def __rmul__(self, other):
    return self * other

  # +
  def __add__(self, other):
    if isinstance(other, int):
      res = self.varSet.copy()
      res[-1] += other
      return Polynomial(res)
    elif isinstance(other, Polynomial):
      l1 = self.varSet.copy()
      l1.reverse()

      l2 = other.varSet.copy()
      l2.reverse()

      minLen = min(len(l1), len(l2))
      res = []

      for i in range(max(len(l1), len(l2))):
        if (minLen == len(l1) and i >= minLen):
          res.append(l2[i])
        elif (minLen == len(l2) and i >= minLen):
          res.append(l1[i])
        else:
          res.append(l1[i] + l2[i])
      res.reverse()
      return Polynomial(res)
    else:
      raise TypeError

  def __radd__(self, other):
    return self + other
 
  # -
  def __sub__(self, other):
    if isinstance(other, (Polynomial, int)):
      return self + (-1 * other)
    else:
      raise TypeError 
    
  def __rsub__(self, other):
    self = self * (-1)
    return self.__add__(other)

  # x == y вызывает x.__eq__(y)
  def __eq__(self, other):
    if not isinstance(other, Polynomial):
      raise TypeError
    else:
      if len(self) != len(other):
        return False
      else:
        for i in range(len(self.varSet)):
          if self.varSet[i] == other.varSet[i]:
            continue
          else:
            return False
        return True

  def __req__(self, other):
    self.__eq__(other)

  # x != y вызывает x.__ne__(y)
  def __ne__(self, other):
    return not (self == other)

  def __rne__(self, other):
    self.__ne__(other)

  def __repr__(self):
    return "Polynomial({})".format(repr(self.varSet))
# end class Polynomial
