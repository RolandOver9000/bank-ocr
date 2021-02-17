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

    # -----------convert_code_to_decimal function tests----------

    def test_convert_code_to_decimal_with_only_hexadecimal_digits(self):
        """
        Tests code_validator's convert_code_to_decimal function with only hexadecimal digits.
        """
        test_code = "BBBBCCACC"
        result = bank_ocr.convert_code_to_decimal(test_code)
        test_result = [11, 11, 11, 11, 12, 12, 10, 12, 12]
        self.assertEqual(result, test_result)

    def test_convert_code_to_decimal_with_mixed_hexadecimal_digits(self):
        """
        Tests code_validator's convert_code_to_decimal function with mixed hexadecimal digits.
        """
        test_code = "B9BB7CA1C"
        result = bank_ocr.convert_code_to_decimal(test_code)
        test_result = [11, 9, 11, 11, 7, 12, 10, 1, 12]
        self.assertEqual(result, test_result)

    # -----------is_code_valid_checksum function tests----------

    def test_is_code_valid_checksum_with_valid_hexadecimal_code(self):
        """
        Tests code_validator's is_code_valid_checksum function with valid hexadecimal code.
        """
        test_code = "71111112A"
        result = bank_ocr.is_code_valid_checksum(test_code)
        self.assertEqual(result, True)

    def test_is_code_valid_checksum_with_valid_decimal_code(self):
        """
        Tests code_validator's is_code_valid_checksum function with valid decimal code.
        """
        test_code = "000000051"
        result = bank_ocr.is_code_valid_checksum(test_code)
        self.assertEqual(result, True)

    def test_is_code_valid_checksum_with_invalid_hexadecimal_code(self):
        """
        Tests code_validator's is_code_valid_checksum function with invalid hexadecimal code.
        """
        test_code = "BDCEFA000"
        result = bank_ocr.is_code_valid_checksum(test_code)
        self.assertEqual(result, False)

    def test_is_code_valid_checksum_with_invalid_decimal_code(self):
        """
        Tests code_validator's is_code_valid_checksum function with invalid decimal code.
        """
        test_code = "490867713"
        result = bank_ocr.is_code_valid_checksum(test_code)
        self.assertEqual(result, False)

    # -----------get_validation_status function tests----------

    def test_get_validation_status_with_valid_code(self):
        """
        Tests code_validator's get_validation_status with valid code.
        """
        test_code = "000000051"
        result = bank_ocr.get_validation_status(test_code)
        self.assertEqual(result, "")

    def test_get_validation_status_with_invalid_code_checksum(self):
        """
        Tests code_validator's get_validation_status with invalid code checksum.
        """
        test_code = "490867713"
        result = bank_ocr.get_validation_status(test_code)
        self.assertEqual(result, "ERR")

    def test_get_validation_status_with_invalid_code_digit(self):
        """
        Tests code_validator's get_validation_status with invalid code digit.
        """
        test_code = "49086?713"
        result = bank_ocr.get_validation_status(test_code)
        self.assertEqual(result, "ILL")

    def test_get_validation_status_with_multiple_invalid_code_digit(self):
        """
        Tests code_validator's get_validation_status with multiple invalid code digit.
        """
        test_code = "?90????13"
        result = bank_ocr.get_validation_status(test_code)
        self.assertEqual(result, "ILL")

    # -----------is_code_contain_multiple_bad_digits function tests----------

    def test_is_code_contain_multiple_bad_digits_with_no_bad_digit(self):
        """
        Tests code_validator's is_code_contain_multiple_bad_digits with no bad digit.
        """
        test_code = "190123413"
        result = bank_ocr.is_code_contain_multiple_bad_digits(test_code)
        self.assertEqual(result, False)

    def test_is_code_contain_multiple_bad_digits_with_one_bad_digit(self):
        """
        Tests code_validator's is_code_contain_multiple_bad_digits with one bad digit.
        """
        test_code = "190123?13"
        result = bank_ocr.is_code_contain_multiple_bad_digits(test_code)
        self.assertEqual(result, False)

    def test_is_code_contain_multiple_bad_digits_with_two_bad_digits(self):
        """
        Tests code_validator's is_code_contain_multiple_bad_digits with two bad digits.
        """
        test_code = "1?0123?13"
        result = bank_ocr.is_code_contain_multiple_bad_digits(test_code)
        self.assertEqual(result, True)

    def test_is_code_contain_multiple_bad_digits_with_many_bad_digits(self):
        """
        Tests code_validator's is_code_contain_multiple_bad_digits with one bad digits.
        """
        test_code = "?9?1?3?13"
        result = bank_ocr.is_code_contain_multiple_bad_digits(test_code)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
