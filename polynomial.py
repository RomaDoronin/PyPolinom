class Polynomial:
  def __init__(self, varSet):
    self.varSet = varSet

  # print
  def __str__(self):
    strRes = ""
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
      raise Exception("Invalid argument type")

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
      raise Exception("Invalid argument type")    

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
      raise Exception("Invalid argument type") 
    
  def __rsub__(self, other):
    self = self * (-1)
    return self.__add__(other)

  # x < y вызывает x.__lt__(y)
  def __lt__(self, other):
    if (type(other) != Polynomial):
      raise Exception("Invalid argument type")
    else:
      if (len(self.varSet) != len(other.varSet)):
        return len(self.varSet) < len(other.varSet)
      else:
        for i in range(len(self.varSet)):
          if self.varSet[i] == other.varSet[i]:
            continue
          else:
            return self.varSet[i] < other.varSet[i]
        return False

  def __rlt__(self, other):
    self.__gt__(other)
  
  # x ≤ y вызывает x.__le__(y)
  def __le__(self, other):
    if (type(other) != Polynomial):
      raise Exception("Invalid argument type")
    else:
      if (len(self.varSet) != len(other.varSet)):
        return len(self.varSet) < len(other.varSet)
      else:
        for i in range(len(self.varSet)):
          if self.varSet[i] == other.varSet[i]:
            continue
          else:
            return self.varSet[i] <= other.varSet[i]
        return True

  def __rle__(self, other):
    self.__ge__(other)

  # x == y вызывает x.__eq__(y)
  def __eq__(self, other):
    if (type(other) != Polynomial):
      raise Exception("Invalid argument type")
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
      raise Exception("Invalid argument type")
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

  # x > y вызывает x.__gt__(y)
  def __gt__(self, other):
    if (type(other) != Polynomial):
      raise Exception("Invalid argument type")
    else:
      if (len(self.varSet) != len(other.varSet)):
        return len(self.varSet) > len(other.varSet)
      else:
        for i in range(len(self.varSet)):
          if self.varSet[i] == other.varSet[i]:
            continue
          else:
            return self.varSet[i] > other.varSet[i]
        return False

  def __rgt__(self, other):
    self.__lt__(other)

  # x ≥ y вызывает x.__ge__(y)
  def __ge__(self, other):
    if (type(other) != Polynomial):
      raise Exception("Invalid argument type")
    else:
      if (len(self.varSet) != len(other.varSet)):
        return len(self.varSet) > len(other.varSet)
      else:
        for i in range(len(self.varSet)):
          if self.varSet[i] == other.varSet[i]:
            continue
          else:
            return self.varSet[i] >= other.varSet[i]
        return True

  def __rge__(self, other):
    self.__le__(other)

# end class Polynomial

def TEST_F(num, test, refer):
  if (type(test) != type(refer)):
    raise Exception("Different types of arguments")
  else:
    if (test == refer):
      print("Test " + str(num) + " : [ OK ]")
    else:
      print("Test " + str(num) + " : [ FAILED ] " + str(test))

def TEST_EX(num, val1, op, val2, excp):
  try:
    if (op == "+"):
      val1 + val2
    elif (op == "-"):
      val1 - val2
    elif (op == "*"):
      val1 * val2
    elif (op == "<"):
      val1 < val2
    elif (op == "<="):
      val1 <= val2
    elif (op == "=="):
      val1 == val2
    elif (op == "!="):
      val1 != val2
    elif (op == ">="):
      val1 >= val2
    elif (op == ">"):
      val1 > val2
  except Exception as e:
    if (str(e) == excp):
      print("Test " + str(num) + " : [ OK ]")
    else:
      print("Test " + str(num) + " : [ FAILED ] " + str(test))

# Main
pol_1 = Polynomial([1,2,0,-2])
pol_2 = Polynomial([1,2,0,-3])
pol_3 = Polynomial([-3,1])
pol_4 = Polynomial([3,-5,7])
pol_5 = Polynomial([4,0,0,0])

print("--------------------------------- [+]")
TEST_F(1.1, pol_1 + 4, Polynomial([1,2,0,2]))
TEST_F(1.2, 4 + pol_1, Polynomial([1,2,0,2]))
TEST_F(1.3, 0 + pol_2, Polynomial([1,2,0,-3]))
TEST_F(1.4, pol_2 + pol_3, Polynomial([1,2,-3,-2]))
TEST_F(1.5, pol_3 + pol_5, Polynomial([4,0,-3,1]))
TEST_EX(1.6, pol_3, "+", '4', "Invalid argument type")
TEST_EX(1.7, "tm", "+", pol_1, "Invalid argument type")

print("--------------------------------- [-]")
TEST_F(2.1, pol_1 - 4, Polynomial([1,2,0,-6]))
TEST_F(2.2, 4 - pol_1, Polynomial([-1,-2,0,6]))
TEST_F(2.3, 0 - pol_2, Polynomial([-1,-2,0,3]))
TEST_F(2.3, pol_2 - 0, Polynomial([1,2,0,-3]))
TEST_F(2.4, pol_2 - pol_3, Polynomial([1,2,3,-4]))
TEST_F(2.5, pol_3 - pol_5, Polynomial([-4,0,-3,1]))
TEST_F(2.6, pol_5 - pol_3, Polynomial([4,0,3,-1]))
TEST_EX(2.7, pol_3, "-", '4', "Invalid argument type")
TEST_EX(2.8, "tm", "-", pol_1, "Invalid argument type")

print("--------------------------------- [*]")
TEST_F(3.1, pol_1 * 4, Polynomial([4,8,0,-8]))
TEST_F(3.2, 4 * pol_1, Polynomial([4,8,0,-8]))
TEST_F(3.3, 0 * pol_2, Polynomial([0,0,0,0]))
TEST_F(3.3, pol_2 * (-2), Polynomial([-2,-4,0,6]))
TEST_F(3.4, pol_2 * pol_3, Polynomial([-3,-5,2,9,-3]))
TEST_F(3.5, pol_3 * pol_5, Polynomial([-12,4,0,0,0]))
TEST_F(3.6, pol_5 * pol_3, Polynomial([-12,4,0,0,0]))
TEST_EX(3.7, pol_3, "*", '4', "Invalid argument type")
TEST_EX(3.8, "tm", "*", pol_1, "Invalid argument type")

print("--------------------------------- [<]")
TEST_F(4.1, pol_2 < pol_1, True)
TEST_F(4.2, pol_1 < pol_2, False)
TEST_F(4.3, pol_3 < pol_4, True)
TEST_F(4.4, pol_4 < pol_3, False)
TEST_F(4.5, pol_1 < pol_5, True)
TEST_F(4.6, pol_5 < pol_1, False)
TEST_F(4.7, pol_5 < pol_5, False)
TEST_F(4.8, pol_2 < pol_2, False)
TEST_EX(4.9, pol_3, "<", '4', "Invalid argument type")
TEST_EX(4.10, 4, "<", pol_1, "Invalid argument type")

print("--------------------------------- [<=]")
TEST_F(4.1, pol_2 <= pol_1, True)
TEST_F(4.2, pol_1 <= pol_2, False)
TEST_F(4.3, pol_3 <= pol_4, True)
TEST_F(4.4, pol_4 <= pol_3, False)
TEST_F(4.5, pol_1 <= pol_5, True)
TEST_F(4.6, pol_5 <= pol_1, False)
TEST_F(4.7, pol_5 <= pol_5, True)
TEST_F(4.8, pol_2 <= pol_2, True)
TEST_EX(4.9, pol_3, "<=", '4', "Invalid argument type")
TEST_EX(4.1, 4, "<=", pol_1, "Invalid argument type")

print("--------------------------------- [>]")
TEST_F(4.1, pol_2 > pol_1, False)
TEST_F(4.2, pol_1 > pol_2, True)
TEST_F(4.3, pol_3 > pol_4, False)
TEST_F(4.4, pol_4 > pol_3, True)
TEST_F(4.5, pol_1 > pol_5, False)
TEST_F(4.6, pol_5 > pol_1, True)
TEST_F(4.7, pol_5 > pol_5, False)
TEST_F(4.8, pol_2 > pol_2, False)
TEST_EX(4.9, pol_3, ">", '4', "Invalid argument type")
TEST_EX(4.10, 4, ">", pol_1, "Invalid argument type")

print("--------------------------------- [>=]")
TEST_F(4.1, pol_2 >= pol_1, False)
TEST_F(4.2, pol_1 >= pol_2, True)
TEST_F(4.3, pol_3 >= pol_4, False)
TEST_F(4.4, pol_4 >= pol_3, True)
TEST_F(4.5, pol_1 >= pol_5, False)
TEST_F(4.6, pol_5 >= pol_1, True)
TEST_F(4.7, pol_5 >= pol_5, True)
TEST_F(4.8, pol_2 >= pol_2, True)
TEST_EX(4.9, pol_3, ">=", '4', "Invalid argument type")
TEST_EX(4.10, 4, ">=", pol_1, "Invalid argument type")

print("--------------------------------- [==]")
TEST_F(4.1, pol_2 == pol_1, False)
TEST_F(4.2, pol_1 == pol_2, False)
TEST_F(4.3, pol_3 == pol_4, False)
TEST_F(4.4, pol_4 == pol_3, False)
TEST_F(4.5, pol_1 == pol_5, False)
TEST_F(4.6, pol_5 == pol_1, False)
TEST_F(4.7, pol_5 == pol_5, True)
TEST_F(4.8, pol_2 == pol_2, True)
TEST_EX(4.9, pol_3, "==", '4', "Invalid argument type")
TEST_EX(4.10, 4, "==", pol_1, "Invalid argument type")

print("--------------------------------- [!=]")
TEST_F(4.1, pol_2 != pol_1, True)
TEST_F(4.2, pol_1 != pol_2, True)
TEST_F(4.3, pol_3 != pol_4, True)
TEST_F(4.4, pol_4 != pol_3, True)
TEST_F(4.5, pol_1 != pol_5, True)
TEST_F(4.6, pol_5 != pol_1, True)
TEST_F(4.7, pol_5 != pol_5, False)
TEST_F(4.8, pol_2 != pol_2, False)
TEST_EX(4.9, pol_3, "!=", '4', "Invalid argument type")
TEST_EX(4.10, 4, "!=", pol_1, "Invalid argument type")