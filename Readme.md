# VikLang
### A Simple Emulated Assembly Language

---
Table of Contents:

1. Introduction
2. Syntax
3. Commands

---

## Introduction

As told in the title, VikLang is a simple 
assembly language. But it is different from a 
normal assembly language in the sense of it 
being interpreted instead of compiled and also,
the cpu it uses is fully emulated in Python. Because it is emulated in Python, it can 
execute programs on any platform that Python 
can. 

---

## Syntax

```
cmd1 param1 param2 param3 param4...
cmd2 param1 param2 param3 param4...
```

The code above is an example of the VikLang 
syntax. `cmd1` and `cmd2` are the commands and 
the other parts are the parameters. Every line 
of code needs to use this syntax. Blank lines
act as a method to end the program.

---

## Commands

```
add dest op1 op2
sub dest op1 op2
mul dest op1 op2
div dest op1 op2
sto daddr reg
loa dest addr
out reg
set dest value
rst
com val1 val2
and dest op1 op2
oor dest op1 op2
not dest op
jum l
jue l
jug l
jul l
jne l
jnl l
jng l
cmt comment
ech code
lfc filename reg index
sfc filename reg index
```

### Out

The `out` command in Viklang outputs the value 
at the register at the index of `reg`.

### Set

The `set` command sets the value of the 
register at `dest` to `value`.

### Mathematical operations

The `add`, `sub`, `mul` and `div` commands in 
Viklang write the result of the operation between 
`op1` & `op2` into the register at index `dest`.

### The `r` expression

The `r` expression, used as in `r12`, is 
replaced by the value at the register denoted 
by the number after `r`.

### Example 1:

Code:
```
set 0 7
set 1 5
add 2 r0 r1
out 2
sub 2 r0 r1
out 2
```

Output:
```
0000000c
00000002
```

### Cmt

The `cmt` command declares a comment on that 
line. The rest of the line is ignored.

### Loa & Sto

The `loa` and `sto` commands send data between 
RAM and the CPU registers. The `loa` command 
gets from the memory and `sto` writes values 
to the memory.

### Rst

This command resets everything except for the 
console.

### Com

This command compares the two value and saves 
the result inside the CPU flags.

### And, Oor & Not

These commands execute the logical operations 
on the operands given in the 2nd and maybe 3rd 
parameters and save the result to the 
register denoted in `dest`.

### The 7 jumping commands

These commands jump to the line denoted in the 
parameter if the CPU flags align with its 
conditions except for `jum` which always jumps 
if executed.

### Example 2:

Code:
```
set 1 12
set 2 10
com 1 2
jug 7
out 1
jum 8
out 2
cmt End Of The Code
```

Output:
```
0000000a
```

### Ech

This command outputs the ASCII character with 
code `code`.

### Lfc & Sfc

These commands load from and store to a 
specific character index in the file with the 
name in `filename`, respectively.

### The `/len` expression

This expression is replaced by the number of 
characters in the file with the name denoted 
before the slash.

### Example 3:

Code:
```
set 1 2
set 2 3
add 3 r1 r2
out 3
com r3 r2
jne 10
sub 3 r2 r1
out 3
jum 12
mul 3 r2 r1
out 3
set 4 79
set 5 75
set 6 10
ech r4
ech r5
ech r6
set 0 0
set 14 1
set 15 dummy/len
set 13 0
lfc dummy 1 r0
ech r1
add 0 r0 r14
com r0 r15
jul 22
```

File `dummy`:
```
Hello, world!
```

Output:
```
00000005
00000006
OK
Hello, world!
```