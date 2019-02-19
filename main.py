from polynomial import Polynomial
import unittest

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
