from Py2Corona.Consts import Constantes
import unittest

class TestConstants(unittest.TestCase):
    
    def test_operators_override(self):
        ctest = Constantes('some_string_to_test')
        self.assertEqual(ctest + '1', ctest + 1)


if __name__ == '__main__':
    unittest.main()