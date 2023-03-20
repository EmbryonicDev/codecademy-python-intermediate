import unittest
from unittest.mock import patch
import warnings
from monitor import calculate_remaining_time, request_flight_attendant, CustomerRequestWarning


class TestCalculateRemainingTime(unittest.TestCase):
    def test_calculate_remaining_time_with_integer_input(self):
        self.assertEqual(calculate_remaining_time(60), (0, 4))
        self.assertEqual(calculate_remaining_time(120), (0, 8))
        self.assertEqual(calculate_remaining_time(300), (0, 20))

    def test_calculate_remaining_time_with_float_input(self):
        self.assertEqual(calculate_remaining_time(45.5), (0, 3))
        self.assertEqual(calculate_remaining_time(87.25), (0, 5))

    def test_calculate_remaining_time_with_zero_input(self):
        self.assertEqual(calculate_remaining_time(0), (0, 0))


class TestRequestFlightAttendant(unittest.TestCase):
    def test_request_flight_attendant_with_warning(self):
        with warnings.catch_warnings(record=True) as w:
            request_flight_attendant()
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, CustomerRequestWarning))
            self.assertEqual(str(w[-1].message), 'A customer has requested attention!')


if __name__ == '__main__':
    unittest.main()
