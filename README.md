# DreamKnot
DreamKnot is an advanced programming language based on Python.

# More Languages
English | [台灣中文](/docs/zhtw_README.md)

# Tell us your dream
fill out the [form(Traditional Chinese)](https://forms.gle/XWxE8HftuyitmGeA7) to let us know what you want.

# You Do Less We Do More
We want to make programming easy for anyone.

We believe you should spend less time thinking about how to code and spend more time on being creative.
So trust us, we're going to make this easy.

Some syntax might seem weird for experienced programmers, but it's actually very simple, just look at the examples below.

# Basics
## Syntax
DreamKnot doesn't have strict syntax rules. (at least for now)

every line ends with nothing
```dk
print hello world
```

## Naming
You can name your variable with any unicode characters.
```dk
myVar = 0
myVar2 = True
myVar3 = "hello"
```
This includes numbers.
```dk
3 = 2
print(1+1===3) //true
```

## Output
DreamKnot uses `print` to output.

Anything in the line after print will be printed
```dk
print "hello world"
```
you can also use parentheses.
```dk
print("hello world")
```

## Variable
The name of the variable goes in front of the `=` sign and the value goes after the `=` sign

You can declare a variable without type.
```dk
variable = 0
```
or with type
```dk
int variable = 0
```
**Note:** type does not do anything in DreamKnot but it make some feel better.

## Input
DreamKnot uses `input` to input.

Use a variable to store the input
```dk
myInput = input
```

You can also specify the type of the input
```dk
myInput = input int
```

# Advanced
## Constants
There are three types of constant.
Constant can be edited, but not re-assigned.
```dk
const name = "KS"
name.pop()
```

Constant Constant cannot be changed anyway.
```dk
const const name = "KS"
```

Constant Constant Constant cannot be changed anyway, and it's assigned globally.
```dk
const const const pi = "3.14"
```
**Note:** It's very dangerous to use `const const const` because will affect all the file ran forever.
