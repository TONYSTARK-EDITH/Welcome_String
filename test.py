import unittest

from wstring import *


class TestWelcomeString(unittest.TestCase):

    def test_normal_case(self):
        with self.assertRaises(CharacterExpectedGotStringException):
            Wstring("Hello", symbol="54")

        with self.assertRaises(EmptyCharacterFoundException):
            Wstring("Hello", symbol="")

    def test_color_case(self):
        Wstring("Default")
        Wstring("Red", color="red")
        Wstring("Green", color="green")
        Wstring("Purple", color="purple")
        Wstring("Blue", color="Blue")
        Wstring("Yellow", color="Yellow")

    def test_symbol_case(self):
        print()
        Wstring("Dollar")
        Wstring("Hash", symbol="#")
        Wstring("Asterisk", symbol="*")
        Wstring("One", symbol="1")


if __name__ == "__main__":
    unittest.main()
