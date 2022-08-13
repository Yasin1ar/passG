import unittest
from unittest import TestCase
from passG import PassGenerator

class Test_pass_generator(TestCase):

    def test_len(self):
            self.assertEqual(len(PassGenerator.create_pass()), 8)

    def test_raise_error(self):
            self.assertRaises(AssertionError, PassGenerator.create_pass(), )


if __name__ == '__main__':
    for i in range(5):
        unittest.main()
