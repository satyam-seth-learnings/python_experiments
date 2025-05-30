from unittest.mock import patch
from requests.exceptions import Timeout
from my_calender import get_holidays
import unittest



class TestCalendar(unittest.TestCase):
    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
