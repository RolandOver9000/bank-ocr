import unittest

import bank_ocr


class TestSum(unittest.TestCase):

    # -----------is_digit_valid function tests----------

    def test_is_digit_valid_with_valid_digit(self):
        """
        Tests code_fixer's is_digit_valid function with valid digit.
        """
        test_code = "   " \
                    "  |" \
                    "  |"

        result = bank_ocr.is_digit_valid(test_code)
        self.assertEqual(result, True, "The digit should be valid.")

    def test_is_digit_valid_with_invalid_digit(self):
        """
        Tests code_fixer's is_digit_valid function with valid digit.
        """
        test_code = " _ " \
                    "| |" \
                    "  |"

        result = bank_ocr.is_digit_valid(test_code)
        self.assertEqual(result, False, "The digit should be invalid.")

    # -----------try_to_fix function tests----------

    def test_try_to_fix_digit_with_fixable_decimal_digit(self):
        """
        Tests code_fixer's try_to_fix_digit function with fixable decimal digit.
        """
        test_digit = "   " \
                     "   " \
                     "  |"
        result = bank_ocr.try_to_fix_digit(test_digit)
        self.assertEqual(result, ['1'], "The result should be '1' in a list.")

    def test_try_to_fix_digit_with_fixable_hexadecimal_digit(self):
        """
        Tests code_fixer's try_to_fix_digit function with fixable hexadecimal digit.
        """
        test_digit = " _ " \
                     "|  " \
                     " _ "
        result = bank_ocr.try_to_fix_digit(test_digit)
        self.assertEqual(result, ['C'], "The result should be 'C' in a list.")

    def test_try_to_fix_digit_with_completely_wrong_digit(self):
        """
        Tests code_fixer's try_to_fix_digit function with fixable decimal digit.
        """
        test_digit = "   " \
                     "  |" \
                     "|_|"
        result = bank_ocr.try_to_fix_digit(test_digit)
        self.assertEqual(result, [], "The result should be an empty list.")

    # -----------get_digits_from_code_by_index function tests----------

    def test_get_digits_from_code_by_index_with_all_indexes(self):
        """
        Tests code_fixer's get_digits_from_code_by_index function with all indexes.
        """
        test_code = " _  _  _  _  _  _  _  _  _ " \
                    "|_|  ||  |_ |_ |_|| || ||  " \
                    "| |  ||_ |_ |  | ||_||_||_ "
        test_code_digit_length = 9
        test_code_digits_by_index = {
            0: " _ "
               "|_|"
               "| |",
            1: " _ "
               "  |"
               "  |",
            2: " _ "
               "|  "
               "|_ ",
            3: " _ "
               "|_ "
               "|_ ",
            4: " _ "
               "|_ "
               "|  ",
            5: " _ "
               "|_|"
               "| |",
            6: " _ "
               "| |"
               "|_|",
            7: " _ "
               "| |"
               "|_|",
            8: " _ "
               "|  "
               "|_ ",
        }
        result = bank_ocr.get_digits_from_code_by_index(test_code, range(test_code_digit_length))
        self.assertEqual(result, test_code_digits_by_index)

    def test_get_digits_from_code_by_index_with_specific_indexes(self):
        """
        Tests code_fixer's get_digits_from_code_by_index function with specific indexes.
        """
        test_code = " _  _  _  _  _  _  _  _  _ " \
                    "|_|  ||  |_ |_ |_|| || ||  " \
                    "| |  ||_ |_ |  | ||_||_||_ "
        test_code_digits_by_index = {
            1: " _ "
               "  |"
               "  |",
            5: " _ "
               "|_|"
               "| |",
            7: " _ "
               "| |"
               "|_|",
            8: " _ "
               "|  "
               "|_ ",
        }
        test_index_list = [1, 5, 7, 8]
        result = bank_ocr.get_digits_from_code_by_index(test_code, test_index_list)
        self.assertEqual(result, test_code_digits_by_index)

    def test_get_digits_from_code_by_index_with_one_index(self):
        """
        Tests code_fixer's get_digits_from_code_by_index function with one index.
        """
        test_code = " _  _  _  _  _  _  _  _  _ " \
                    "|_|  ||  |_ |_ |_|| || ||  " \
                    "| |  ||_ |_ |  | ||_||_||_ "
        test_code_digits_by_index = {
            7: " _ "
               "| |"
               "|_|"
        }
        test_index_list = [7]
        result = bank_ocr.get_digits_from_code_by_index(test_code, test_index_list)
        self.assertEqual(result, test_code_digits_by_index)


if __name__ == '__main__':
    unittest.main()
