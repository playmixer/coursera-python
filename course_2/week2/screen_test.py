import unittest
import random
from screen2 import Vec2d, add, mul


class TestScreen(unittest.TestCase):
    def test_add(self):
        self.cases = list((int(random.random()*100), int(random.random()*100)) for i in range(10))
        for i in range(len(self.cases) - 1):
            v1 = self.cases[i]
            v2 = self.cases[i+1]
            with self.subTest(vec=(v1, v2)):
                vec = Vec2d(v1) + Vec2d(v2)
                self.assertEqual(add(v1, v2), vec.int_pair())      
                
    def test_mul(self):
        self.cases = list(((int(random.random()*100), int(random.random()*100)), random.random()) for i in range(10))
        for i in range(len(self.cases) ):
            v1 = self.cases[i][0]
            k = self.cases[i][1]
            with self.subTest(vec=v1, k=k):
                vec = Vec2d(v1) * k
                self.assertEqual(mul(v1, k), vec.int_pair())                
          
        
        
if __name__ == "__main__":
    unittest.main()