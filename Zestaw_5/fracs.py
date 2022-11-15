import math

def LCM(a, b):
    absolute = abs(a*b)
    result = absolute / math.gcd(a , b)
    return result

def simplify(frac):
    divisor = math.gcd(frac[0] , frac[1])
    result = [0 , 0]
    result[0] , result[1] = int(frac[0] / divisor) , int(frac[1] / divisor)
    return result

def add_frac(frac1, frac2):
    result = [0, 0]
    denominator = LCM(frac1[1], frac2[1])
    numerator1 = frac1[0] * denominator / frac1[1]
    numerator2 = frac2[0] * denominator / frac2[1]
    result[0] = int(numerator1+numerator2)
    result[1] = int(denominator)
    simplify(result)
    return result

def sub_frac(frac1, frac2):
    result = [0, 0]
    denominator = LCM(frac1[1], frac2[1])
    numerator1 = frac1[0] * denominator / frac1[1]
    numerator2 = frac2[0] * denominator / frac2[1]
    result[0] = int(numerator1-numerator2)
    result[1] = int(denominator)
    simplify(result)
    return result

def mul_frac(frac1, frac2):
    frac = [0, 0]
    frac[0] = int(frac1[0]*frac2[0])
    frac[1] = int(frac1[1]*frac2[1])
    simplify(frac)
    return frac

def div_frac(frac1, frac2):
    frac = [0, 0]
    tmp = [frac2[1] , frac2[0]]
    frac = mul_frac(frac1 , tmp) # Dzielenie = mnożenie przez odwrotność
    return frac

def is_positive(frac):
    if(frac[0]*frac[1] < 0):
        return False
    else:
        return True


def is_zero(frac):
    if(frac[0] == 0):
        return True
    else:
        return False

def cmp_frac(frac1, frac2):
    base = LCM(frac1[1], frac2[1])
    numerator1 = frac1[0] * base / frac1[1]
    numerator2 = frac2[0] * base / frac2[1]
    if(numerator1 > numerator2):
        return 1
    elif(numerator1 == numerator2):
        return 0
    elif(numerator1 < numerator2):
        return -1

def frac2float(frac):
    rs = float(frac[0] / frac[1])
    return rs

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):



    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1,6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(f1 , f3) ,  [-3, 2])

    def test_div_frac(self):
        self.assertEqual(div_frac(f1 , f3) ,  [-1, 6])

    def test_is_positive(self):
        self.assertFalse(is_positive(f1))

    def test_is_zero(self):
        self.assertTrue(is_zero(f5))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(f3,f4), 0)
 
    def test_frac2float(self):
        self.assertEqual(frac2float(f1), -0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy