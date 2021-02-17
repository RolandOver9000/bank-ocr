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


if __name__ == '__main__':
    unittest.main()
