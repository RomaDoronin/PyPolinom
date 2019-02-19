import unittest

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

  # x < y вызывает x.__lt__(y)
  def __lt__(self, other):
    if (type(other) != Polynomial):
      raise TypeError
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
      raise TypeError
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

  # x > y вызывает x.__gt__(y)
  def __gt__(self, other):
    if (type(other) != Polynomial):
      raise TypeError
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
      raise TypeError
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

class PolynomialTest(unittest.TestCase):

  def setUp(self):
    self.pol_1 = Polynomial([1,2,0,-2])
    self.pol_2 = Polynomial([1,2,0,-3])
    self.pol_3 = Polynomial([-3,1])
    self.pol_4 = Polynomial([3,-5,7])
    self.pol_5 = Polynomial([4,0,0,0])

  def test_add(self):
    self.assertEqual(self.pol_1 + 4, Polynomial([1,2,0,2]))
    self.assertEqual(4 + self.pol_1, Polynomial([1,2,0,2]))
    self.assertEqual(0 + self.pol_2, Polynomial([1,2,0,-3]))
    self.assertEqual(self.pol_2 + self.pol_3, Polynomial([1,2,-3,-2]))
    self.assertEqual(self.pol_3 + self.pol_5, Polynomial([4,0,-3,1]))
    with self.assertRaises(TypeError):
      self.pol_3 + '4'
    with self.assertRaises(TypeError):
      "tm" + self.pol_1
        
  def test_sub(self):
    self.assertEqual(self.pol_1 - 4, Polynomial([1,2,0,-6]))
    self.assertEqual(4 - self.pol_1, Polynomial([-1,-2,0,6]))
    self.assertEqual(0 - self.pol_2, Polynomial([-1,-2,0,3]))
    self.assertEqual(self.pol_2 - 0, Polynomial([1,2,0,-3]))
    self.assertEqual(self.pol_2 - self.pol_3, Polynomial([1,2,3,-4]))
    self.assertEqual(self.pol_3 - self.pol_5, Polynomial([-4,0,-3,1]))
    self.assertEqual(self.pol_5 - self.pol_3, Polynomial([4,0,3,-1]))
    with self.assertRaises(TypeError):
      self.pol_3 - '4'
    with self.assertRaises(TypeError):
      "tm" - self.pol_1
        
  def test_mul(self):
    self.assertEqual(self.pol_1 * 4, Polynomial([4,8,0,-8]))
    self.assertEqual(4 * self.pol_1, Polynomial([4,8,0,-8]))
    self.assertEqual(0 * self.pol_2, Polynomial([0,0,0,0]))
    self.assertEqual(self.pol_2 * (-2), Polynomial([-2,-4,0,6]))
    self.assertEqual(self.pol_2 * self.pol_3, Polynomial([-3,-5,2,9,-3]))
    self.assertEqual(self.pol_3 * self.pol_5, Polynomial([-12,4,0,0,0]))
    self.assertEqual(self.pol_5 * self.pol_3, Polynomial([-12,4,0,0,0]))
    with self.assertRaises(TypeError):
      self.pol_3 * '4'
    with self.assertRaises(TypeError):
      "tm" * self.pol_1
        
  def test_more(self):
    self.assertEqual(self.pol_2 < self.pol_1, True)
    self.assertEqual(self.pol_1 < self.pol_2, False)
    self.assertEqual(self.pol_3 < self.pol_4, True)
    self.assertEqual(self.pol_4 < self.pol_3, False)
    self.assertEqual(self.pol_1 < self.pol_5, True)
    self.assertEqual(self.pol_5 < self.pol_1, False)
    self.assertEqual(self.pol_5 < self.pol_5, False)
    self.assertEqual(self.pol_2 < self.pol_2, False)

    self.assertEqual(self.pol_2 <= self.pol_1, True)
    self.assertEqual(self.pol_1 <= self.pol_2, False)
    self.assertEqual(self.pol_3 <= self.pol_4, True)
    self.assertEqual(self.pol_4 <= self.pol_3, False)
    self.assertEqual(self.pol_1 <= self.pol_5, True)
    self.assertEqual(self.pol_5 <= self.pol_1, False)
    self.assertEqual(self.pol_5 <= self.pol_5, True)
    self.assertEqual(self.pol_2 <= self.pol_2, True)

    with self.assertRaises(TypeError):
      self.pol_3 < 4
    with self.assertRaises(TypeError):
      "tm" < self.pol_1

    with self.assertRaises(TypeError):
      self.pol_3 <= 4
    with self.assertRaises(TypeError):
      'C' <= self.pol_1

  def test_less(self):
    self.assertEqual(self.pol_2 > self.pol_1, False)
    self.assertEqual(self.pol_1 > self.pol_2, True)
    self.assertEqual(self.pol_3 > self.pol_4, False)
    self.assertEqual(self.pol_4 > self.pol_3, True)
    self.assertEqual(self.pol_1 > self.pol_5, False)
    self.assertEqual(self.pol_5 > self.pol_1, True)
    self.assertEqual(self.pol_5 > self.pol_5, False)
    self.assertEqual(self.pol_2 > self.pol_2, False)

    self.assertEqual(self.pol_2 >= self.pol_1, False)
    self.assertEqual(self.pol_1 >= self.pol_2, True)
    self.assertEqual(self.pol_3 >= self.pol_4, False)
    self.assertEqual(self.pol_4 >= self.pol_3, True)
    self.assertEqual(self.pol_1 >= self.pol_5, False)
    self.assertEqual(self.pol_5 >= self.pol_1, True)
    self.assertEqual(self.pol_5 >= self.pol_5, True)
    self.assertEqual(self.pol_2 >= self.pol_2, True)

    with self.assertRaises(TypeError):
      self.pol_3 > 4
    with self.assertRaises(TypeError):
      "tm" > self.pol_1

    with self.assertRaises(TypeError):
      self.pol_3 >= 4
    with self.assertRaises(TypeError):
      'C' >= self.pol_1

  def test_equal(self):
    self.assertEqual(self.pol_2 == self.pol_1, False)
    self.assertEqual(self.pol_1 == self.pol_2, False)
    self.assertEqual(self.pol_3 == self.pol_4, False)
    self.assertEqual(self.pol_4 == self.pol_3, False)
    self.assertEqual(self.pol_1 == self.pol_5, False)
    self.assertEqual(self.pol_5 == self.pol_1, False)
    self.assertEqual(self.pol_5 == self.pol_5, True)
    self.assertEqual(self.pol_2 == self.pol_2, True)

    self.assertEqual(self.pol_2 != self.pol_1, True)
    self.assertEqual(self.pol_1 != self.pol_2, True)
    self.assertEqual(self.pol_3 != self.pol_4, True)
    self.assertEqual(self.pol_4 != self.pol_3, True)
    self.assertEqual(self.pol_1 != self.pol_5, True)
    self.assertEqual(self.pol_5 != self.pol_1, True)
    self.assertEqual(self.pol_5 != self.pol_5, False)
    self.assertEqual(self.pol_2 != self.pol_2, False)

    with self.assertRaises(TypeError):
      self.pol_3 == 4
    with self.assertRaises(TypeError):
      "tm" == self.pol_1
    
    with self.assertRaises(TypeError):
      self.pol_3 != 4
    with self.assertRaises(TypeError):
      'C' != self.pol_1
# end class PolynomialTest
	  
# Main
if __name__ == '__main__':
    unittest.main()
	