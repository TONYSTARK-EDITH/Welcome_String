import unittest

from wstring import wString
from Exceptions import *

class TestWelcomeString(unittest.TestCase):
        
    def test_normal_case(self):
        with self.assertRaises(CharacterExpectedGotStringException):
            wString("Hello",symbol="54")

        with self.assertRaises(EmptyCharacterFoundException):
            wString("Hello",symbol="")

    def test_color_case(self):
        wString("Default")
        wString("Red",color="red")
        wString("Green",color="green")
        wString("Purple",color="purple")
        wString("Blue",color="Blue")
        wString("Yellow",color="Yellow")

    def test_symbol_case(self):
        print()
        wString("Dollar")
        wString("Hash",symbol="#")
        wString("Asterick",symbol="*")
        wString("One",symbol="1")

if __name__ == "__main__":
    unittest.main()