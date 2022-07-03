# Welcome to the VikLang compiler!
## Let's learn this simple language!
### Firstly, the syntax:
```
/function param1 param2 param3 param4...   ...param99 param100...
```
the parameters can go on infinitely actually...

### Then echo:
```
/echo 'Hello,world!'
/echo 142857
/echo True
/echo 26.579
...
```
### Then var:
```
/var name value
```
```
/var name 'Bora'
```
### Then str(which is the only way to use spaces in strings):
```
/str 'Hello, world!'
```
then you can use `stringmade` to use that string.
### Then input, to take input:
```
/input 'name: '
```
then use `inputtaken` to use the input.
### Then calc, to do calculations:
```
/calc 2+2
```
then use `calc` to acces the result.
### Then alert:
```
/alert 'Hello!'
```
### Then if:
```
/if condition function param1 param2 param3...
```
param1, param2 and param3 are the parameters passed to function, which is run only if the condition is true.
### Then while loops:
```
/var i 0
/while i<5 code
```
code.vl:
```
/echo i
/var i i+1
```
### Then json:
```
/json greeting
/echo json["hello"]
```
greeting.json:
```
{"hello":"hi"}
```
output:
```
hi
```
### Then last but not least, func:
```
/func filename funcname param1 param2 param3...
```
filename is the name of the file with the code of the function.

### Custom functions:
```
/myfunc param1 param2 param3
```
myfunc is the name of the function in this case.