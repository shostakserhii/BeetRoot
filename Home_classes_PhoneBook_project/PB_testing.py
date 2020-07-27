import unittest
import mypy
from typing import Any, List, Dict, Optional
from PB import User, validation_name, validation_num, validation_listing, validation_with_optional_value_return, new_user, delete

class TestUser(unittest.TestCase):
    def test_phone_is_int_success(self) -> None:
        expected_phone: int = 1231234234
        test_user: User = User('A', 'B', expected_phone, 'C', 'D')
        actual_phone: int = test_user.phone
        self.assertEqual(actual_phone,expected_phone)

    def test_str_phone_is_integer_sucess(self) -> None:
        expected_phone: str = "1231234234"
        test_user: User = User('A', 'B', expected_phone, 'C', 'D')
        actual_phone: str = test_user.phone
        self.assertEqual(actual_phone,expected_phone)

    def test_User_variables_are_str_sucess(self) -> None:
        expected_first_name: str = 'A'
        expected_second_name: str = 'B'
        expected_phone: str = '123'
        expected_city: str = 'C'
        expected_full_name: str = 'A B'
        test_user = User(expected_first_name,
                         expected_second_name,
                         expected_phone,
                         expected_city)

        self.assertEqual(expected_first_name, test_user.first_name)
        self.assertEqual(expected_second_name, test_user.second_name)
        self.assertEqual(expected_phone, test_user.phone)
        self.assertEqual(expected_city, test_user.city)
        self.assertEqual(expected_full_name, test_user.full_name)

    def test_convert(self) -> None:
        expected_first_name: str = 'A'
        expected_second_name: str = 'B'
        expected_phone: str = '123'
        expected_city: str = 'C'
        expected_result: Dict = {
                        'first_name': expected_first_name,
                        'second_name': expected_second_name,
                        'phone': expected_phone,
                        'city': expected_city,
                        'full_name': expected_first_name + " " + expected_second_name
                         }
        test_user: User = User(expected_first_name,
                         expected_second_name,
                         expected_phone,
                         expected_city)
        test_user: Dict = test_user.convert()
        self.assertEqual(expected_result, test_user)


class Test_Validation_num(unittest.TestCase):
    def test_val_num_success(self) -> None:
        expected_result: bool = True
        test: str = '123'
        actual_result: bool = validation_num(test)
        self.assertEqual(actual_result, expected_result)


class Test_Validation_name(unittest.TestCase):
    def test_val_name_success(self) -> None:
        expected_result: bool = True
        test: str = 'Aaa'
        actual_result: bool = validation_name(test)
        self.assertEqual(actual_result, expected_result)


class Test_validation_with_optional_value_return(unittest.TestCase):
    def test_validation_with_optional_value_return_sucess(self) -> None:
        expected_value: str = 'Aaa'
        expected_value2: str = '123'
        actual_value: Optional[str] = validation_with_optional_value_return(expected_value, validation_listing[0])
        actual_value2: Optional[str] = validation_with_optional_value_return(expected_value2, 'phone')
        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_value2, actual_value2)

class Test_Body_functions(unittest.TestCase):
    def test_new_user_sucess(self) -> None:
        expected_fname: str = ("A")
        expected_sname: str = ("B")
        expected_phone: str = "123"
        expected_city: str = ("R")
        expected_full_name: str = "A B"

        test_user: User = new_user(expected_fname,
                             expected_sname,
                             expected_phone,
                             expected_city,
                             expected_full_name
                            ) 

        self.assertEqual(test_user.first_name, expected_fname)
        self.assertEqual(test_user.second_name, expected_sname)
        self.assertEqual(test_user.phone, expected_phone)
        self.assertEqual(test_user.city, expected_city)
        self.assertEqual(test_user.full_name, expected_full_name)

    def test_delete_success(self) -> None:
        phonebook: List[Any] = []
        user: User = User('a', 'b', '1', 'r', 'a b')
        phonebook.append(user)
        expected_result: List[Any] = []
        delete('1', phonebook)
        print(f"in testing after delete{phonebook}")
        self.assertEqual(expected_result, phonebook)


if __name__ == '__main__':
    unittest.main()