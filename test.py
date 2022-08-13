import unittest
from unittest import TestCase
from passG import PassGenerator

class Test_pass_generator(TestCase):

    def test_len(self):
        for i in range(50):
            self.assertEqual(len(PassGenerator.create_pass()), 8)

    def test_type(self):
        self.assertEqual(type(PassGenerator.create_pass()),str)



if __name__ == '__main__':
    unittest.main()
