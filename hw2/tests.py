import json
import unittest
from advert import Advert


class TestAdvert(unittest.TestCase):
    def test_json_to_class(self):
        lesson_str = """{
            "title": "python",
            "price": 0,
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
            }
        }
        """

        lesson = json.loads(lesson_str)
        lesson_ad = Advert(lesson)

        self.assertEqual(lesson_ad.location.address, 'город Москва, Лесная, 7')

    def test_keywords(self):
        corgi_str = """
            {
                "title": "Вельш-корги",
                "price": 1000,
                "class": "dogs",
                "location": {
                    "address": "сельское поселение Ельдигинское, поселок\
                    санатория Тишково, 25"
                }
            }
        """

        corgi_dict = json.loads(corgi_str)
        corgi = Advert(corgi_dict)
        self.assertIn(corgi.class_, 'dogs')

    def test_negative_price(self):
        lesson_str = '{"title": "python", "price": -1}'

        lesson = json.loads(lesson_str)
        self.assertRaises(ValueError, Advert, lesson)

    def test_absent_price(self):
        lesson_str = '{"title": "python"}'

        lesson = json.loads(lesson_str)
        lesson_ad = Advert(lesson)
        self.assertEqual(lesson_ad.price, 0)


if __name__ == '__main__':
    unittest.main()
