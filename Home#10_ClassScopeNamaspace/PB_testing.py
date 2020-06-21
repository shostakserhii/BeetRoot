import unittest
from PB import User


class TestUser(unittest.TestCase):
    def test_phone_is_int_success(self):
        expected_phone = 1231234234
        test_user = User('A', 'B', expected_phone, 'C', 'D')
        actual_phone = test_user.phone
        self.assertEqual(actual_phone,expected_phone)