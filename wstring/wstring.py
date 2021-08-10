"""
A welcoming library which prints the passed string into patterns in the output
"""
import argparse
import sys

from termcolor import cprint

from .Exceptions import *


def main():
    """
    This method is used for the command line arguments  it can will be executed when accessing
    it through the terminal / cmd / powershell

    usage: wstring [-h] -S [STRING [STRING ...]] [-s SYMBOL] [-l LENGTH] [-H HEIGHT] [-c COLOR]
    Welcome string to print the given string in pattern
    optional arguments:
    -h, --help            show this help message and exit
    -S [STRING [STRING ...]], --string [STRING [STRING ...]] String to be printed as pattern
    -s SYMBOL, --symbol SYMBOL A character to be used to print the given string as a pattern
    -l LENGTH, --length LENGTH Length of the pattern
    -H HEIGHT, --height HEIGHT Height of the pattern
    -c COLOR, --color COLOR Color the pattern should be printed

    :return:  None
    """
    parser = argparse.ArgumentParser(prog="wstring", description="Welcome string to print the given string in pattern")
    parser.add_argument("-S", "--string", type=str, nargs="*", help="String to be printed as pattern", required=True)
    parser.add_argument("-s", "--symbol", type=str, nargs=1,
                        help="A character to be used to print the given string as a pattern", default="$",
                        required=False)
    parser.add_argument("-l", "--length", type=int, nargs=1, help="Length of the pattern", default=[7], required=False)
    parser.add_argument("-H", "--height", nargs=1, type=int, help="Height of the pattern", default=[7], required=False)
    parser.add_argument("-c", "--color", nargs=1, type=str, help="Color the pattern should be printed",
                        default="default", required=False)
    args = parser.parse_args()
    string = " ".join(args.string)
    symbol = args.symbol[0]
    length = args.length[0]
    height = args.height[0]
    color = args.color[0]
    Wstring(string, length=length, height=height, symbol=symbol, color=color)


class Wstring:
    def __init__(self, string, length=7, height=7, symbol="$", color="default"):
        """
        This is to create a instance of the Wstring with parameters

        example:
        from wstring import wstring
        wstring("Hello")

        from wstring import Wstring
        Wstring("Welcome", length=5, height=5, symbol='$', color='red')

        :param string: The value you want to print as patterns
        :param length:  The value of the patterns length default will be 7
        :param height: The value of the patterns height default will be 7
        :param symbol: The symbol of the pattern default will be dollar ($)
        :param color:  The color of the pattern will print default will be `default of the IDLE/CMD/powershell/Terminal`
        """

        if len(symbol.strip()) > 1:
            raise CharacterExpectedGotStringException(f"Argument symbol expected character got {symbol}")
        if symbol.strip() == "" or symbol.strip() == " ":
            raise EmptyCharacterFoundException(f"Argument symbol expected a valid character but got empty character")

        self.word = []  # Initialising the word list in order to print the letters in the order of the string
        self.height = height  # Height of the pattern
        self.length = length  # Length of the pattern
        self.symbol = symbol  # Symbol of the pattern
        self.color = color.lower()  # Color of the pattern
        self.space = [[" " for _ in range(self.length)] for _ in range(self.height)]  # Space for the pattern

        if sys.platform == 'win32':
            from colorama import init  # for windows powershell and cmd
            init()

        try:
            # This will only work in IDLE, it won't work from a command prompt
            self.shell_connect = sys.stdout.shell  # check if idle or terminal

            self.colormap = {"red": ("COMMENT", "Red"),
                             "yellow": ("KEYWORD", "Light Red"),
                             "green": ("STRING", "Green"),
                             "blue": ("stdout", "Blue"),
                             "purple": ("BUILTIN", "Purple"),  # magenta
                             "default": ("SYNC", "Black")}

        except AttributeError:
            # This will only work linux terminal,win powershell, cmd
            self.colormap = {"red": "red",
                             "yellow": "yellow",
                             "green": "green",
                             "blue": "blue",
                             "purple": "magenta",
                             "default": "white"}
        except Exception as a:
            self.__printincolor(" ".join(a.args), clr='red')
        if self.color not in self.colormap:
            self.color = 'default'
        for i in list(string):
            self.__check(i.lower())
        column = 0
        for i in range(self.height):
            for k in range(len(self.word)):
                self.__printincolor("".join(self.word[k][column]), clr=self.color, end="  ")
            column += 1
            self.__printincolor("", clr=self.color, end='\n')
        print()

    def __generate_A(self):
        self.A = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height // 2 or j == self.length - 1:
                    self.A[i][j] = self.symbol

    def __generate_B(self):
        self.B = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or ((i == 0 or i == self.height - 1 or i == self.height // 2) and j < self.length - 1) or (
                        (i + 1) % 2 == 0 and j == self.length - 1 and i != self.height // 2):
                    self.B[i][j] = self.symbol

    def __generate_C(self):
        self.C = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height - 1:
                    self.C[i][j] = self.symbol

    def __generate_D(self):
        self.D = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or (
                        i == 0 or i == self.height - 1) and j < self.length - 1 or \
                        self.height - 1 > i > 0 and j == self.length - 1:
                    self.D[i][j] = self.symbol

    def __generate_E(self):
        self.E = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height // 2 or i == self.height - 1:
                    self.E[i][j] = self.symbol

    def __generate_F(self):
        self.F = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height // 2:
                    self.F[i][j] = self.symbol

    def __generate_G(self):
        self.G = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or (i == self.height // 2 and j >= self.length // 2) or i == self.height - 1 or (
                        i >= self.height // 2 and j == self.length - 1):
                    self.G[i][j] = self.symbol

    def __generate_H(self):
        self.H = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or j == self.length - 1 or i == self.height // 2:
                    self.H[i][j] = self.symbol

    def __generate_I(self):
        self.alp_I = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == self.height - 1 or i == 0 or j == self.length // 2:
                    self.alp_I[i][j] = self.symbol

    def __generate_J(self):
        self.J = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if (i == self.height - 1 and j < self.length // 2) or i == 0 or j == self.length // 2 or (
                        i == self.height - 2 and j == 0):
                    self.J[i][j] = self.symbol

    def __generate_K(self):
        self.K = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or (i == self.height // 2 and j < self.length // 2) or (
                        i < self.height // 2 and j == self.length - 1 - i) or (self.height // 2 < i == j):
                    self.K[i][j] = self.symbol

    def __generate_L(self):
        self.L = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == self.height - 1 or j == 0:
                    self.L[i][j] = self.symbol

    def __generate_M(self):
        self.M = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length - 1 or j == 0 or (i == self.height // 2 and j == i) or (
                        i < self.height // 2 and (j == i or j == self.length - 1 - i)):
                    self.M[i][j] = self.symbol

    def __generate_N(self):
        self.N = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length - 1 or j == 0 or j == i:
                    self.N[i][j] = self.symbol

    def __generate_O(self):
        self.alp_O = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.height - 1 or j == 0 or i == 0 or i == self.length - 1:
                    self.alp_O[i][j] = self.symbol

    def __generate_P(self):
        self.P = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == 0 or (i <= self.height // 2 and j == self.height - 1) or (i == self.height // 2):
                    self.P[i][j] = self.symbol

    def __generate_Q(self):
        self.Q = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if ((0 < i < self.height - 2) and (j == 0 or j == self.length - 1)) or (
                        (i == 0 or i == self.length - 2) and (j > 0 and j != self.length - 1)) or (
                        self.height // 2 <= i == j):
                    self.Q[i][j] = self.symbol

    def __generate_R(self):
        self.R = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == 0 or i <= self.height // 2 and j == self.height - 1 or \
                        i == self.height // 2 or self.height // 2 < i == j:
                    self.R[i][j] = self.symbol

    def __generate_S(self):
        self.S = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if (i == 0 and j > 0) or (i == self.height - 1 and j < self.length - 1) or (
                        j == 0 and (i < self.height // 2 and i != 0)) or (
                        i > self.height // 2 and i != self.height - 1 and j == self.height - 1) or (
                        i == self.height // 2 and (0 < j < self.length - 1)):
                    self.S[i][j] = self.symbol

    def __generate_T(self):
        self.T = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == self.length // 2:
                    self.T[i][j] = self.symbol

    def __generate_U(self):
        self.U = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if (i == self.height - 1 and (j != 0 and j != self.length - 1)) or (
                        (j == 0 or j == self.length - 1) and i < self.height - 1):
                    self.U[i][j] = self.symbol

    def __generate_V(self):
        self.V = [[" " for _ in range(self.length)] for _ in range(self.height)]
        t = 1
        for i in range(self.height):
            for j in range(self.length):
                if ((j == 0 or j == self.length - 1) and i <= self.height // 2) or (
                        i > self.height // 2 and (j == t or j == self.length - 1 - t)):
                    self.V[i][j] = self.symbol
                if i > self.height // 2 and j == self.length - 1 - t:
                    t += 1
                    break

    def __generate_W(self):
        self.W = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length - 1 or j == 0 or (i == self.height // 2 and j == i) or (
                        i > self.height // 2 and (j == i or j == self.length - 1 - i)):
                    self.W[i][j] = self.symbol

    def __generate_X(self):
        self.X = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == j or j == self.length - 1 - i:
                    self.X[i][j] = self.symbol

    def __generate_Y(self):
        self.Y = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if ((i == j or j == self.length - 1 - i) and i <= self.height // 2) or (
                        j == self.length // 2 and i > self.height // 2):
                    self.Y[i][j] = self.symbol

    def __generate_Z(self):
        self.Z = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if (i == 0 and j < self.length - 1) or (i == self.height - 1 and j > 0) or (
                        (i > 0 or i < self.height - 1) and j == self.length - 1 - i):
                    self.Z[i][j] = self.symbol

    def __generate_0(self):
        self.num_0 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.length - 1:
                    self.num_0[i][j] = self.symbol

    def __generate_1(self):
        self.num_1 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length // 2 or i == self.height - 1 or (
                        i == 1 and j == i) or (
                        i == self.height // 2 - 1 and j == 0):
                    self.num_1[i][j] = self.symbol

    def __generate_2(self):
        self.num_2 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.height - 1 or (j == self.length - 1 and i <= self.height // 2) or (
                        j == 0 and i > self.height // 2) or (i == self.height // 2):
                    self.num_2[i][j] = self.symbol

    def __generate_3(self):
        self.num_3 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.length - 1 or j == self.length - 1 or i == self.length // 2:
                    self.num_3[i][j] = self.symbol

    def __generate_4(self):
        self.num_4 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length - 2 or i == self.height - 2 or (
                        i != 0 and i < self.height - 2 and j == self.length - 2 - i):
                    self.num_4[i][j] = self.symbol

    def __generate_5(self):
        self.num_5 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.height - 1 or (j == self.length - 1 and i > self.height // 2) or (
                        j == 0 and i <= self.height // 2) or i == self.height // 2:
                    self.num_5[i][j] = self.symbol

    def __generate_6(self):
        self.num_6 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height - 1 or (
                        j == self.length - 1 and i > self.height // 2) or i == self.height // 2:
                    self.num_6[i][j] = self.symbol

    def __generate_7(self):
        self.num_7 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == self.length - 1 - i:
                    self.num_7[i][j] = self.symbol

    def __generate_8(self):
        self.num_8 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.height - 1 or i == self.height // 2 or j == 0 or j == self.length - 1:
                    self.num_8[i][j] = self.symbol

    def __generate_9(self):
        self.num_9 = [[" " for _ in range(self.length)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == self.length - 1 or (
                        j == 0 and i <= self.height // 2) or (i == self.height // 2):
                    self.num_9[i][j] = self.symbol

    def __check(self, i):
        """
        Check method will check the letter passed to it and append the respective letter's/number's nested list to
        the word's list


        :param i: Character to be evaluated
        :return: None
        """
        if i == " ":
            self.word.append(self.space)
        elif i == "a":
            if not hasattr(self, "A"):
                self.__generate_A()
            self.word.append(self.A)
        elif i == "b":
            if not hasattr(self, "B"):
                self.__generate_B()
            self.word.append(self.B)
        elif i == "c":
            if not hasattr(self, "C"):
                self.__generate_C()
            self.word.append(self.C)
        elif i == "d":
            if not hasattr(self, "D"):
                self.__generate_D()
            self.word.append(self.D)
        elif i == "e":
            if not hasattr(self, "E"):
                self.__generate_E()
            self.word.append(self.E)
        elif i == "f":
            if not hasattr(self, "F"):
                self.__generate_F()
            self.word.append(self.F)
        elif i == "g":
            if not hasattr(self, "G"):
                self.__generate_G()
            self.word.append(self.G)
        elif i == "h":
            if not hasattr(self, "H"):
                self.__generate_H()
            self.word.append(self.H)
        elif i == "i":
            if not hasattr(self, "alp_I"):
                self.__generate_I()
            self.word.append(self.alp_I)
        elif i == "j":
            if not hasattr(self, "J"):
                self.__generate_J()
            self.word.append(self.J)
        elif i == "k":
            if not hasattr(self, "K"):
                self.__generate_K()
            self.word.append(self.K)
        elif i == "l":
            if not hasattr(self, "L"):
                self.__generate_L()
            self.word.append(self.L)
        elif i == "m":
            if not hasattr(self, "M"):
                self.__generate_M()
            self.word.append(self.M)
        elif i == "n":
            if not hasattr(self, "N"):
                self.__generate_N()
            self.word.append(self.N)
        elif i == "o":
            if not hasattr(self, "alp_O"):
                self.__generate_O()
            self.word.append(self.alp_O)
        elif i == "p":
            if not hasattr(self, "P"):
                self.__generate_P()
            self.word.append(self.P)
        elif i == "q":
            if not hasattr(self, "Q"):
                self.__generate_Q()
            self.word.append(self.Q)
        elif i == "r":
            if not hasattr(self, "R"):
                self.__generate_R()
            self.word.append(self.R)
        elif i == "s":
            if not hasattr(self, "S"):
                self.__generate_S()
            self.word.append(self.S)
        elif i == "t":
            if not hasattr(self, "T"):
                self.__generate_T()
            self.word.append(self.T)
        elif i == "u":
            if not hasattr(self, "U"):
                self.__generate_U()
            self.word.append(self.U)
        elif i == "v":
            if not hasattr(self, "V"):
                self.__generate_V()
            self.word.append(self.V)
        elif i == "w":
            if not hasattr(self, "W"):
                self.__generate_W()
            self.word.append(self.W)
        elif i == "x":
            if not hasattr(self, "X"):
                self.__generate_X()
            self.word.append(self.X)
        elif i == "y":
            if not hasattr(self, "Y"):
                self.__generate_Y()
            self.word.append(self.Y)
        elif i == "z":
            if not hasattr(self, "Z"):
                self.__generate_Z()
            self.word.append(self.Z)
        elif i == '1':
            if not hasattr(self, "num_1"):
                self.__generate_1()
            self.word.append(self.num_1)
        elif i == '0':
            if not hasattr(self, "num_0"):
                self.__generate_0()
            self.word.append(self.num_0)
        elif i == '2':
            if not hasattr(self, "num_2"):
                self.__generate_2()
            self.word.append(self.num_2)

        elif i == '3':
            if not hasattr(self, "num_3"):
                self.__generate_3()
            self.word.append(self.num_3)
        elif i == '4':
            if not hasattr(self, "num_4"):
                self.__generate_4()
            self.word.append(self.num_4)
        elif i == '5':
            if not hasattr(self, "num_5"):
                self.__generate_5()
            self.word.append(self.num_5)
        elif i == '6':
            if not hasattr(self, "num_6"):
                self.__generate_6()
            self.word.append(self.num_6)
        elif i == '7':
            if not hasattr(self, "num_7"):
                self.__generate_7()
            self.word.append(self.num_7)
        elif i == '8':
            if not hasattr(self, "num_8"):
                self.__generate_8()
            self.word.append(self.num_8)
        elif i == '9':
            if not hasattr(self, "num_9"):
                self.__generate_9()
            self.word.append(self.num_9)

    def __printincolor(self, text, clr, end=' '):
        """
        A method which is used to override the print function
        to print in colors
        :param text: Value to be printed
        :param clr:  Color in which the text should be printed
        :param end:  The end value for the parameter in print
        :return: None
        """
        try:
            # This shell will be IDLE shell
            self.shell_connect.write(text + end, self.colormap[clr][0])
        except AttributeError:
            # This will work for other terminals like linux terminal, powershell, cmd etc.,
            cprint(text, self.colormap[clr], attrs=['bold'], file=sys.stderr, end=end)
        except Exception as e:
            # It will print if any other exception occurs
            cprint(" ".join(e.args), attrs=['blink'], file=sys.stderr, end=end)

    def __repr__(self):
        return ""
