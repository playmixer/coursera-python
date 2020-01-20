# import unittest

# def factorize(x):
#     """ 
#     Factorize positive integer and return its factors.
#     :type x: int,>=0
#     :rtype: tuple[N],N>0
#     """
    
#     if not x >= 0:
#         raise TypeError
#     if not isinstance(x,int):
#         raise TypeError
#     if x in (0,1):
#         return x,
#     res = []
#     total = x
#     i = 2
#     while total > 1:
#         if total % i == 0:
#             res.append(i)
#             total /= i            
#             i = 2
#         i += 1
#     return tuple(res)


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.cases = ['string', 1.5]
        for x in self.cases:
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)
                
    def test_negative(self):
        self.cases = [-1, -10, -100]
        for x in self.cases:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, x)
                
    def test_zero_and_one_cases(self):
        self.cases = [0, 1]
        self.answer = [(0,), (1,)]
        for x in range(len(self.cases)):
            with self.subTest(x=self.cases[x]):
                self.assertEqual(factorize(self.cases[x]),self.answer[x])
                
    def test_simple_numbers(self):
        self.cases = [3, 13, 29]
        self.answer = [(3,), (13,), (29,)]
        for x in range(len(self.cases)):
            with self.subTest(x=self.cases[x]):
                self.assertEqual(factorize(self.cases[x]), self.answer[x])
                
    def test_two_simple_multipliers(self):
        self.cases = [6, 26, 121]
        self.answer = [(2, 3), (2, 13), (11, 11)]
        for x in range(len(self.cases)):
            with self.subTest(x=self.cases[x]):
                self.assertEqual(factorize(self.cases[x]), self.answer[x])
                
    def test_many_multipliers(self):
        self.cases = [1001, 9699690]
        self.answer = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for i in range(len(self.cases)):
            with self.subTest(x=self.cases[i]):
                self.assertEqual(factorize(self.cases[i]), self.answer[i])
                        
                
                
# if __name__ == "__main__":
#     unittest.main()