
class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.cases = ['string', 1.5]
        for x in self.cases:
            with self.subTest(case=x):
                self.assertRaises(TypeError, factorize, x)