"""
A welcoming library which prints the passed string into patterns in the output
"""
import sys
from termcolor import cprint
from .Exceptions import *

class wString:
    def __init__(self, String, length=7, height=7, symbol="$", color="default"):
        # Initialising the word list in order to print the letters in the order of the string
        if len(symbol.strip()) > 1:
            raise CharacterExpectedGotStringException(f"Argument symbol expected character got {symbol}")
        if symbol.strip() == "" or symbol.strip() == " ":
            raise EmptyCharacterFoundException(f"Argument symbol expected a valid character but got empty character")
        self.word = []
        l = 0
        self.height = height
        self.length = length
        self.symbol = symbol
        self.color = color.lower()
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



        except AttributeError as e:
            # This will only work linux terminal,win powershell, cmd
            self.colormap = {"red": "red",
                             "yellow": "yellow",
                             "green": "green",
                             "blue": "blue",
                             "purple": "magenta",
                             "default": "white"}
        except Exception as a:
            self.printInColor(a, clr='r')
        if self.color not in self.colormap:
            self.color = 'default'
        for i in list(String):
            self.check(i.lower())
        for i in range(self.height):
            for k in range(len(self.word)):
                self.printInColor("".join(self.word[k][l]), clr=self.color, end="  ")
            l += 1
            self.printInColor("", clr=self.color, end='\n')
        print()

    def printA(self):
        self.a = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height // 2 or j == self.length - 1:
                    self.a[i][j] = self.symbol

    def printB(self):
        self.b = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or ((i == 0 or i == self.height - 1 or i == self.height // 2) and j < self.length - 1) or (
                        (i + 1) % 2 == 0 and j == self.length - 1 and i != self.height // 2):
                    self.b[i][j] = self.symbol
        pass

    def printC(self):
        self.c = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height - 1:
                    self.c[i][j] = self.symbol

    def printD(self):
        self.d = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or ((i == 0 or i == self.height - 1) and j < self.length - 1) or (
                        (i < self.height - 1 and i > 0) and j == self.length - 1):
                    self.d[i][j] = self.symbol

    def printE(self):
        self.e = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height // 2 or i == self.height - 1:
                    self.e[i][j] = self.symbol
        pass

    def printF(self):
        self.f = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height // 2:
                    self.f[i][j] = self.symbol
        pass

    def printG(self):
        self.g = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or (i == self.height // 2 and j >= self.length // 2) or i == self.height - 1 or (
                        i >= self.height // 2 and j == self.length - 1):
                    self.g[i][j] = self.symbol
        pass

    def printH(self):
        self.h = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or j == self.length - 1 or i == self.height // 2:
                    self.h[i][j] = self.symbol
        pass

    def printI(self):
        self.i = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == self.height - 1 or i == 0 or j == self.length // 2:
                    self.i[i][j] = self.symbol
        pass

    def printJ(self):
        self.j = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if (i == self.height - 1 and j < self.length // 2) or i == 0 or j == self.length // 2 or (
                        i == self.height - 2 and j == 0):
                    self.j[i][j] = self.symbol
        pass

    def printK(self):
        self.k = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or (i == self.height // 2 and j < self.length // 2) or (
                        i < self.height // 2 and j == self.length - 1 - i) or (self.height // 2 < i == j):
                    self.k[i][j] = self.symbol
        pass

    def printL(self):
        self.l = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == self.height - 1 or j == 0:
                    self.l[i][j] = self.symbol

        pass

    def printM(self):
        self.m = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length - 1 or j == 0 or (i == self.height // 2 and j == i) or (
                        i < self.height // 2 and (j == i or j == self.length - 1 - i)):
                    self.m[i][j] = self.symbol

        pass

    def printN(self):
        self.n = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length - 1 or j == 0 or j == i:
                    self.n[i][j] = self.symbol
        pass

    def printO(self):
        self.o = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.height - 1 or j == 0 or i == 0 or i == self.length - 1:
                    self.o[i][j] = self.symbol
        pass

    def printP(self):
        self.p = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == 0 or (i <= self.height // 2 and j == self.height - 1) or (i == self.height // 2):
                    self.p[i][j] = self.symbol
        pass

    def printQ(self):
        self.q = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if ((0 < i < self.height - 2) and (j == 0 or j == self.length - 1)) or (
                        (i == 0 or i == self.length - 2) and (j > 0 and j != self.length - 1)) or (
                        self.height // 2 <= i == j):
                    self.q[i][j] = self.symbol
        pass

    def printR(self):
        self.r = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == 0 or (i <= self.height // 2 and j == self.height - 1) or (i == self.height // 2) or (
                        i > self.height // 2 and j == i):
                    self.r[i][j] = self.symbol
        pass

    def printS(self):
        self.s = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if (i == 0 and j > 0) or (i == self.height - 1 and j < self.length - 1) or (
                        j == 0 and (i < self.height // 2 and i != 0)) or (
                        i > self.height // 2 and i != self.height - 1 and j == self.height - 1) or (
                        i == self.height // 2 and (0 < j < self.length - 1)):
                    self.s[i][j] = self.symbol
        pass

    def printT(self):
        self.t = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == self.length // 2:
                    self.t[i][j] = self.symbol
        pass

    def printU(self):
        self.u = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if (i == self.height - 1 and (j != 0 and j != self.length - 1)) or (
                        (j == 0 or j == self.length - 1) and i < self.height - 1):
                    self.u[i][j] = self.symbol
        pass

    def printV(self):
        self.v = [[" " for i in range(self.length)] for i in range(self.height)]
        t = 1
        for i in range(self.height):
            for j in range(self.length):
                if ((j == 0 or j == self.length - 1) and i <= self.height // 2) or (
                        i > self.height // 2 and (j == t or j == self.length - 1 - t)):
                    self.v[i][j] = self.symbol
                if i > self.height // 2 and j == self.length - 1 - t:
                    t += 1
                    break
        pass

    def printW(self):
        self.w = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length - 1 or j == 0 or (i == self.height // 2 and j == i) or (
                        i > self.height // 2 and (j == i or j == self.length - 1 - i)):
                    self.w[i][j] = self.symbol
        pass

    def printX(self):
        self.x = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == j or j == self.length - 1 - i:
                    self.x[i][j] = self.symbol
        pass

    def printY(self):
        self.y = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if ((i == j or j == self.length - 1 - i) and i <= self.height // 2) or (
                        j == self.length // 2 and i > self.height // 2):
                    self.y[i][j] = self.symbol
        pass

    def printZ(self):
        self.z = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if (i == 0 and j < self.length - 1) or (i == self.height - 1 and j > 0) or (
                        (i > 0 or i < self.height - 1) and j == self.length - 1 - i):
                    self.z[i][j] = self.symbol
        pass

    def printSpace(self):
        self.space = [[" " for i in range(self.length)] for i in range(self.height)]

    def print0(self):
        self.num_0 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.length - 1:
                    self.num_0[i][j] = self.symbol

    def print1(self):
        self.num_1 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length // 2 or i == self.height - 1 or (
                        i == 1 and j == i) or (
                        i == self.height // 2 - 1 and j == 0):
                    self.num_1[i][j] = self.symbol

    def print2(self):
        self.num_2 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.height - 1 or (j == self.length - 1 and i <= self.height // 2) or (
                        j == 0 and i > self.height // 2) or (i == self.height // 2):
                    self.num_2[i][j] = self.symbol

    def print3(self):
        self.num_3 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.length - 1 or j == self.length - 1 or i == self.length // 2:
                    self.num_3[i][j] = self.symbol

    def print4(self):
        self.num_4 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == self.length - 2 or i == self.height - 2 or (
                        i != 0 and i < self.height - 2 and j == self.length - 2 - i):
                    self.num_4[i][j] = self.symbol

    def print5(self):
        self.num_5 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.height - 1 or (j == self.length - 1 and i > self.height // 2) or (
                        j == 0 and i <= self.height // 2) or i == self.height // 2:
                    self.num_5[i][j] = self.symbol

    def print6(self):
        self.num_6 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if j == 0 or i == 0 or i == self.height - 1 or (
                        j == self.length - 1 and i > self.height // 2) or i == self.height // 2:
                    self.num_6[i][j] = self.symbol

    def print7(self):
        self.num_7 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == self.length - 1 - i:
                    self.num_7[i][j] = self.symbol

    def print8(self):
        self.num_8 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or i == self.height - 1 or i == self.height // 2 or j == 0 or j == self.length - 1:
                    self.num_8[i][j] = self.symbol

    def print9(self):
        self.num_9 = [[" " for i in range(self.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if i == 0 or j == self.length - 1 or (
                        j == 0 and i <= self.height // 2) or (i == self.height // 2):
                    self.num_9[i][j] = self.symbol

    # Check method will check the letter passed to it and append the respective letter's/number's nested list to the
    # list word
    def check(self, i):
        if i == " ":
            self.printSpace()
            self.word.append(self.space)
        elif i == "a":
            self.printA()
            self.word.append(self.a)
        elif i == "b":
            self.printB()
            self.word.append(self.b)
        elif i == "c":
            self.printC()
            self.word.append(self.c)
        elif i == "d":
            self.printD()
            self.word.append(self.d)
        elif i == "e":
            self.printE()
            self.word.append(self.e)
        elif i == "f":
            self.printF()
            self.word.append(self.f)
        elif i == "g":
            self.printG()
            self.word.append(self.g)
        elif i == "h":
            self.printH()
            self.word.append(self.h)
        elif i == "i":
            self.printI()
            self.word.append(self.i)
        elif i == "j":
            self.printJ()
            self.word.append(self.j)
        elif i == "k":
            self.printK()
            self.word.append(self.k)
        elif i == "l":
            self.printL()
            self.word.append(self.l)
        elif i == "m":
            self.printM()
            self.word.append(self.m)
        elif i == "n":
            self.printN()
            self.word.append(self.n)
        elif i == "o":
            self.printO()
            self.word.append(self.o)
        elif i == "p":
            self.printP()
            self.word.append(self.p)
        elif i == "q":
            self.printQ()
            self.word.append(self.q)
        elif i == "r":
            self.printR()
            self.word.append(self.r)
        elif i == "s":
            self.printS()
            self.word.append(self.s)
        elif i == "t":
            self.printT()
            self.word.append(self.t)
        elif i == "u":
            self.printU()
            self.word.append(self.u)
        elif i == "v":
            self.printV()
            self.word.append(self.v)
        elif i == "w":
            self.printW()
            self.word.append(self.w)
        elif i == "x":
            self.printX()
            self.word.append(self.x)
        elif i == "y":
            self.printY()
            self.word.append(self.y)
        elif i == "z":
            self.printZ()
            self.word.append(self.z)
        elif i == '1':
            self.print1()
            self.word.append(self.num_1)
        elif i == '0':
            self.print0()
            self.word.append(self.num_0)
        elif i == '2':
            self.print2()
            self.word.append(self.num_2)

        elif i == '3':
            self.print3()
            self.word.append(self.num_3)
        elif i == '4':
            self.print4()
            self.word.append(self.num_4)
        elif i == '5':
            self.print5()
            self.word.append(self.num_5)
        elif i == '6':
            self.print6()
            self.word.append(self.num_6)
        elif i == '7':
            self.print7()
            self.word.append(self.num_7)
        elif i == '8':
            self.print8()
            self.word.append(self.num_8)
        elif i == '9':
            self.print9()
            self.word.append(self.num_9)

    def printInColor(self, text, clr, end=' '):
        try:
            self.shell_connect.write(text + end, self.colormap[clr][0])
        except Exception as a:
            cprint(text, self.colormap[clr], attrs=['bold'], file=sys.stderr, end=end)


    def __repr__(self):
        return ""
