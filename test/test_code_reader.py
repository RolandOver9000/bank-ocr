import unittest

import bank_ocr


class TestSum(unittest.TestCase):

    # -----------process_string_code function tests----------

    def test_process_string_code_with_decimal(self):
        """
        Tests code_reader's process_string_code function with decimal number.
        """
        test_code = "                           " \
                    "  |  |  |  |  |  |  |  |  |" \
                    "  |  |  |  |  |  |  |  |  |"

        result = bank_ocr.process_string_code(test_code)
        self.assertEqual(result, "111111111", "The processed code should be 111111111")

    def test_process_string_code_with_hexadecimal(self):
        """
        Tests code_reader's process_string_code function with hexadecimal number.
        """
        test_code = " _  _  _  _  _  _  _  _  _ " \
                    "|_||_||  |_ |_ |_||  |  |  " \
                    "| || ||_ |_ |  | ||_ |_ |_ "

        result = bank_ocr.process_string_code(test_code)
        self.assertEqual(result, "AACEFACCC", "The processed code should be AACEFACCC")

    def test_process_string_code_with_hexadecimal_and_decimal(self):
        """
        Tests code_reader's process_string_code function with hexadecimal and decimal number.
        """
        test_code = " _  _  _  _  _  _  _  _  _ " \
                    "|_|  ||  |_ |_ |_|| || ||  " \
                    "| |  ||_ |_ |  | ||_||_||_ "
        result = bank_ocr.process_string_code(test_code)
        self.assertEqual(result, "A7CEFA00C", "The processed code should be A7CEFA00C")

    def test_process_string_code_with_decimal_digit_error(self):
        """
        Tests code_reader's process_string_code function with wrong decimal number.
        """
        test_code = " _  _  _  _  _  _  _  _  _ " \
                    "|_  _ |_ |_ |_ |_ |_ |_ |_ " \
                    " _| _| _| _|  | _| _| _| _ "
        result = bank_ocr.process_string_code(test_code)
        self.assertEqual(result, "5?55?555?", "The processed code should be 5?55?555?")

    def test_process_string_code_with_hexadecimal_digit_error(self):
        """
        Tests code_reader's process_string_code function with wrong hexadecimal number.
        """
        test_code = "    _  _  _  _  _  _  _  _ " \
                    "|_||_||  |_ |  |_|   |  |  " \
                    "| |  ||_ |_ |  | ||_ |_ |_ "
        result = bank_ocr.process_string_code(test_code)
        self.assertEqual(result, "??CE?A?CC", "The processed code should be ??CE?A?CC")

    def test_process_string_code_with_hexadecimal_and_decimal_digit_error(self):
        """
        Tests code_reader's process_string_code function with wrong hexadecimal and wrong decimal number.
        """
        test_code = " _  _  _  _  _     _  _  _ " \
                    "|_|   |  |_ |_ |_|| |  ||  " \
                    "|    ||_ |_ |  | ||_||_||_ "
        result = bank_ocr.process_string_code(test_code)
        self.assertEqual(result, "??CEF?0?C", "The processed code should be ??CEF?0?C")

    # ----------read_from_dummy_file function tests----------

    def test_read_from_dummy_file(self):
        """
        Tests code_reader's read_from_dummy_file function.
        """
        test_file_source = "test/test_data/test_dummy_data.txt"
        test_result ="                   _  _  _ " \
                     "  |  |  |  |  |  ||_ |_ |_|" \
                     "  |  |  |  |  |  ||_ |  | |"
        result = bank_ocr.read_from_dummy_file(test_file_source)
        self.assertEqual(result, [test_result])


if __name__ == '__main__':
    unittest.main()
