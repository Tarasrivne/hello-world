import unittest
from name_function import get_formated_name

class NamesTestCase(unittest.TestCase):

    #"""Тести для 'nume_function.py"""
    def test_first_last_name(self):
        """Імена типу 'Luk Skywalker' працюють правильно?"""
        formatted_name = get_formated_name('Luk','Skywalker')
        self.assertEqual(formatted_name, 'Luk Skywalker')

if __name__ == '__main__':
    unittest.main()
