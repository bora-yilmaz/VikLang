import sys
import os

cwd = "/Users/borayilmaz/Desktop/deneme4"

f = input(">>>")

filename = f if f else "main.vl"


def flen(name):
    with open(f"{str(cwd)}/{name}") as lfile:
        return len(lfile.read())


def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


class Memory:
    def __init__(self):
        self.r = ["00000000"] * 32

    def sto(self, b, v):
        self.r[b] = v

    def loa(self, b):
        return self.r[b]


class CPU:
    def __init__(self):
        self.r = ["00000000"] * 16
        self.m = Memory()
        self.c = [0, 0, 0]

    def stringify(self, v, s):
        return str(hex(int(v)))[2:].rjust(s, "0")[-8:]

    def add(self, dest, op1, op2):
        self.r[dest] = self.stringify(op1 + op2, 8)

    def sub(self, dest, op1, op2):
        self.r[dest] = self.stringify(op1 - op2, 8)

    def mul(self, dest, op1, op2):
        self.r[dest] = self.stringify(op1 * op2, 8)

    def div(self, dest, op1, op2):
        self.r[dest] = self.stringify(op1 / op2, 8)

    def sto(self, r, b):
        self.m.sto(b, self.r[r])

    def loa(self, r, b):
        self.r[r] = self.m.loa(b)

    def lfc(self, fn, r, lc):
        with open(f"{str(cwd)}/{fn}") as lfile:
            if os.stat(f"{str(cwd)}/{fn}").st_size != 0:
                txt = lfile.read()
                self.r[r] = self.stringify(ord(txt[lc]), 8)

    def sfc(self, fn, r, lc):
        with open(f"{str(cwd)}/{fn}", "r") as lfile:
            text = replacer(lfile.read(), chr(int(self.r[r], 16)), lc)
        with open(f"{str(cwd)}/{fn}", "w") as lfile:
            lfile.write(text)

    def showregisters(self, regs=(i for i in range(16))):
        for i, reg in enumerate(self.r):
            if i in regs:
                print(i, ": ", reg)


def runcommand(lcommand, cl):
    global mycpu

    nl = cl + 1

    com = lcommand.split(" ")
    lst = []
    for i, c in enumerate(com):
        if c[0] == "r" and ((i != 0 and com[0] != "lfc" and com[0] != "sfc") or (i > 1 and com[0] == "lfc" or com[0] == "sfc")):
            c = str(int(mycpu.r[int(c[1:])], 16))
        elif c[-4:] == "/len":
            c = str(flen(c[:-4]))


        if i == 0:
            lst.append(c)
        elif i == 1 and com[0] != "sfc" and com[0] != "lfc" and com[0] != "out":
            lst.append(int(c))
        elif i > 1 or (com[0] == "out" and i > 0) or (com[0] == "sfc" and i > 0) or (com[0] == "lfc" and i > 0):
            lst.append(c)

    cc = lst[0]
    if cc == "add":
        mycpu.add(lst[1], int(lst[2]), int(lst[3]))
    elif cc == "sub":
        mycpu.sub(lst[1], int(lst[2]), int(lst[3]))
    elif cc == "mul":
        mycpu.mul(lst[1], int(lst[2]), int(lst[3]))
    elif cc == "div":
        mycpu.div(lst[1], int(lst[2]), int(lst[3]))
    elif cc == "sto":
        mycpu.sto(int(lst[2]), int(lst[1]))
    elif cc == "loa":
        mycpu.sto(int(lst[1]), int(lst[2]))
    elif cc == "out":
        print(mycpu.r[int(lst[1])])
    elif cc == "set":
        mycpu.r[int(lst[1])] = mycpu.stringify(c, 8)
    elif cc == "rst":
        mycpu = CPU()
    elif cc == "com":
        mycpu.c = [int(lst[1]) < int(lst[2]), int(lst[1]) == int(lst[2]), int(lst[1]) > int(lst[2])]
    elif cc == "and":
        mycpu.r[int(lst[1])] = mycpu.stringify(int(lst[2]) and int(lst[3]), 8)
    elif cc == "oor":
        mycpu.r[int(lst[1])] = mycpu.stringify(int(lst[2]) or int(lst[3]), 8)
    elif cc == "not":
        mycpu.r[int(lst[1])] = mycpu.stringify(not int(lst[2]), 8)
    elif cc == "jum":
        d = lst[1]
        nl = int(d)
    elif cc == "jue":
        if mycpu.c[1]:
            d = lst[1]
            nl = int(d)
    elif cc == "jug":
        if mycpu.c[2]:
            d = lst[1]
            nl = int(d)
    elif cc == "jul":
        if mycpu.c[0]:
            d = lst[1]
            nl = int(d)
    elif cc == "jne":
        if not mycpu.c[1]:
            d = lst[1]
            nl = int(d)
    elif cc == "jng":
        if not mycpu.c[2]:
            d = lst[1]
            nl = int(d)
    elif cc == "jnl":
        if not mycpu.c[0]:
            d = lst[1]
            nl = int(d)
    elif cc == "cmt":
        pass
    elif cc == "ech":
        print(chr(int(lst[1])), end="")
    elif cc == "lfc":
        mycpu.lfc(lst[1], int(lst[2]), int(lst[3]))
    elif cc == "sfc":
        mycpu.sfc(lst[1], int(lst[2]), int(lst[3]))
    else:
        nl = 0
    return nl


mycpu = CPU()

file = open(f"{str(cwd)}/{filename}")

fullcode = file.readlines()

file.close()

l = 1

while l:
    try:
        command = fullcode[l - 1][:-1]
    except:
        break
    l = runcommand(command, l)

print("\n")
