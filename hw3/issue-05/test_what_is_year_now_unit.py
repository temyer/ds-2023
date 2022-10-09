import json
import unittest
from unittest.mock import MagicMock, patch

from what_is_year_now import what_is_year_now


def get_mocked_urlopen_response(data: object, status_code: int):
    mm = MagicMock()
    mm.getcode.return_value = status_code
    mm.read.return_value = json.dumps(data)
    mm.__enter__.return_value = mm

    return mm


class TestWhatIsYearNow(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_what_is_year_now_status_code_200(self, mock_urlopen):
        for content, status_code in [
            ({
                'currentDateTime': '2019-03-01',
            }, 200),
            ({
                'currentDateTime': '01.03.2019',
            }, 200),
        ]:
            mm = get_mocked_urlopen_response(content, status_code)
            mock_urlopen.return_value = mm

            year = what_is_year_now()

            self.assertEqual(year, 2019)

    @patch('urllib.request.urlopen')
    def test_what_is_year_now_wrong_date_format(self, mock_urlopen):
        content = {
            'currentDateTime': '01/03/2019',
        }

        status_code = 200

        mm = get_mocked_urlopen_response(content, status_code)
        mock_urlopen.return_value = mm

        self.assertRaises(ValueError, what_is_year_now)
