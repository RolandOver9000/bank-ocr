import unittest

import bank_ocr


class TestSum(unittest.TestCase):

    # -----------get_calculated_checksum function tests----------

    def test_get_calculated_checksum_with_valid_code(self):
        """
        Tests code_validator's get_calculated_checksum function with valid code.
        """
        test_code = 711111111
        result = bank_ocr.get_calculated_checksum()


if __name__ == '__main__':
    unittest.main()
