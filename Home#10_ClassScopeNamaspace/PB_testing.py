import unittest
from PB import User, validation_name, validation_num, validation_listing, validation_with_optional_value_return, delete

class TestUser(unittest.TestCase):
    def test_phone_is_int_success(self):
        expected_phone = 1231234234
        test_user = User('A', 'B', expected_phone, 'C', 'D')
        actual_phone = test_user.phone
        self.assertEqual(actual_phone,expected_phone)

    def test_str_phone_is_integer_sucess(self):
        expected_phone = "1231234234"
        test_user = User('A', 'B', expected_phone, 'C', 'D')
        actual_phone = test_user.phone
        self.assertEqual(actual_phone,expected_phone)

    def test_User_variables_are_str_sucess(self):
        expected_first_name = 'A'
        expected_second_name = 'B'
        expected_phone = '123'
        expected_city = 'C'
        expected_full_name = 'A B'
        test_user = User(expected_first_name,
                         expected_second_name,
                         expected_phone,
                         expected_city)

        self.assertEqual(expected_first_name, test_user.first_name)
        self.assertEqual(expected_second_name, test_user.second_name)
        self.assertEqual(expected_phone, test_user.phone)
        self.assertEqual(expected_city, test_user.city)
        self.assertEqual(expected_full_name, test_user.full_name)

    def test_convert(self):
        expected_first_name = 'A'
        expected_second_name = 'B'
        expected_phone = '123'
        expected_city = 'C'
        expected_result = {
                        'first_name': expected_first_name,
                        'second_name': expected_second_name,
                        'phone': expected_phone,
                        'city': expected_city,
                        'full_name': expected_first_name + " " + expected_second_name
                         }
        test_user = User(expected_first_name,
                         expected_second_name,
                         expected_phone,
                         expected_city)
        test_user = test_user.convert()
        self.assertEqual(expected_result, test_user)


class Test_Validation_num(unittest.TestCase):
    def test_val_num_success(self):
        expected_result = True
        test = '123'
        actual_result = validation_num(test)
        self.assertEqual(actual_result, expected_result)


class Test_Validation_name(unittest.TestCase):
    def test_val_name_success(self):
        expected_result = True
        test = 'Aaa'
        actual_result = validation_name(test)
        self.assertEqual(actual_result, expected_result)


class Test_validation_with_optional_value_return(unittest.TestCase):
    def test_validation_with_optional_value_return_sucess(self):
        expected_value = 'Aaa'
        expected_value2 = '123'
        actual_value = validation_with_optional_value_return(expected_value, validation_listing[0])
        actual_value2 = validation_with_optional_value_return(expected_value2, 'phone')
        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_value2, actual_value2)

class Test_Body_functions(unittest.TestCase):
    def test_new_user_sucess(self):
        expected_fname = ("a").capitalize()
        expected_sname = ("b").capitalize()
        expected_phone = "123"
        expected_city = ("r").capitalize()
        expected_full_name = "A B"

        test_user = User(expected_fname,
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

    def test_delete(self):
        
        testing_user = User('a', 'b', '1', 'r')
        phonebook = list(testing_user)
        expected_result = list()
        delete('1')
        self.assertEqual(expected_result, phonebook)




if __name__ == '__main__':
    unittest.main()
