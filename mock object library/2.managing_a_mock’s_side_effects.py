# Example-3 Managing a Mock’s Side Effects
import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    # def log_request(self, url):
    #     # Log a fake request for test output purposes
    #     print(f'Making a request to {url}.')
    #     print('Request received!')

    #     # Create a new Mock to imitate a Response
    #     response_mock = Mock()
    #     response_mock.status_code = 200
    #     response_mock.json.return_value = {
    #         '12/25': 'Christmas',
    #         '7/4': 'Independence Day',
    #     }
    #     return response_mock

    # def test_get_holidays_logging(self):
    #     # Test a successful, logged request
    #     requests.get.side_effect = self.log_request
    #     assert get_holidays()['12/25'] == 'Christmas'

    def test_get_holidays_retry(self):
        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        # Set the side effect of .get()
        requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()
        # Now retry, expecting a successful response
        assert get_holidays()['12/25'] == 'Christmas'
        # Finally, assert .get() was called twice
        print(requests.get.call_count, '++'*12)
        assert requests.get.call_count == 2


if __name__ == '__main__':
    unittest.main()
