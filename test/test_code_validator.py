import unittest

import bank_ocr


class TestSum(unittest.TestCase):

    # -----------get_calculated_checksum function tests----------

    def test_get_calculated_checksum_with_valid_code(self):
        """
        Tests code_validator's get_calculated_checksum function with valid decimal code.
        """
        test_code = list("711111111")
        result = bank_ocr.get_calculated_checksum(test_code)
        self.assertEqual(result, 99)

    # -----------is_code_has_unknown_digit function tests----------

    def test_is_code_has_unknown_digit_valid_digits(self):
        """
        Tests code_validator's is_code_has_unknown_digit function with valid digits.
        """
        test_code = "A00000000"
        result = bank_ocr.is_code_has_unknown_digit(test_code)
        self.assertEqual(result, True)

    def test_is_code_has_unknown_digit_with_invalid_digits(self):
        """
        Tests code_validator's is_code_has_unknown_digit function with invalid digits.
        """
        test_code = "?0?00??00"
        result = bank_ocr.is_code_has_unknown_digit(test_code)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
