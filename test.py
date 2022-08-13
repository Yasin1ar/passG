from unittest import TestCase
from passG import PassGenerator
        
class Pass_generator(TestCase):
    def test(self):
            self.assertEqual(len(PassGenerator.create_pass()), 8)