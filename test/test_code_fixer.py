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


if __name__ == '__main__':
    unittest.main()
