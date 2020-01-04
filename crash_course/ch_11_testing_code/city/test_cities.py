import unittest
from city_functions import get_formatted_city_name

class TestCityNames(unittest.TestCase):
    """Test City functions"""

    def test_city_country(self):
        formatted_city_name = get_formatted_city_name('santiago', 'chile')
        self.assertEqual(formatted_city_name, "Santiago, Chile")

    def test_city_population(self):
        formatted_city_name = get_formatted_city_name('santiago', 'chile',
                '5000000')
        self.assertEqual(formatted_city_name, 'Santiago, Chile - population \
5000000')

if __name__ == '__main__':
    unittest.main()
