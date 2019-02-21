class Polynomial:
  def __init__(self, varSet):
    if (type(varSet) != list):
      raise TypeError
    else:
      removeZeros = False
      initList = []
      for var in varSet:
        if (type(var) != int):
          raise TypeError
        if (var != 0):
          removeZeros = True
        if (removeZeros):
          initList.append(var)
      self.varSet = initList

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
    if (type(other) == int):
      res = []
      for i in self.varSet:
        res.append(i * other)
      return Polynomial(res)
    elif (type(other) == Polynomial):
      pol = Polynomial([])
      count = 0
      for i in range(len(other.varSet) - 1, -1, -1):
        rPol = (self * other.varSet[i])
        for j in range(count):
          rPol.varSet.append(0)
        count = count + 1
        pol = pol + rPol
      return pol
    else:
      raise TypeError

  def __rmul__(self, other):
    return self.__mul__(other)

  # +
  def __add__(self, other):
    if (type(other) == int):
      res = self.varSet.copy()
      res[-1] += other
      return Polynomial(res)
    elif (type(other) == Polynomial):
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
    return self.__add__(other)
 
  # -
  def __sub__(self, other):
    if (type(other) == int):
      res = self.varSet.copy()
      res[-1] -= other
      return Polynomial(res)
    elif (type(other) == Polynomial):
      return self.__add__(other * (-1))
    else:
      raise TypeError 
    
  def __rsub__(self, other):
    self = self * (-1)
    return self.__add__(other)

  # x == y вызывает x.__eq__(y)
  def __eq__(self, other):
    if (type(other) != Polynomial):
      raise TypeError
    else:
      if (len(self.varSet) != len(other.varSet)):
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
    if (type(other) != Polynomial):
      raise TypeError
    else:
      if (len(self.varSet) != len(other.varSet)):
        return True
      else:
        for i in range(len(self.varSet)):
          if self.varSet[i] == other.varSet[i]:
            continue
          else:
            return True
        return False

  def __rne__(self, other):
    self.__ne__(other)
# end class Polynomial
