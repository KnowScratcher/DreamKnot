# DreamKnot
DreamKnot is an advanced programming language based on Python.

Dream is not a dream anymore!!!

⚠️DreamKnot is not completed yet, it's only a draft for now, we're sorry for any inconvenience.⚠️

# More Languages
English | [台灣中文](/docs/zhtw_README.md)

# Tell us your dream
fill out the [form(Traditional Chinese)](https://forms.gle/XWxE8HftuyitmGeA7) to let us know what you want. We'll try to design the syntax to fit most people's dream.

# Reports
reports are not available just now, we are waiting for response of the form.

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

## String
Use double quote to declare a string.
```dk
myString = "hello"
```
or you can use single quote
```dk
myString = 'hello'
```
or triple quote
```dk
myString = '''hello'''
myString = "'hello'"
```
or even zero
```dk
myString = hello
```

A string is a list of characters.
You can use the indexing mark to get the characters.
```dk
myString = "KnowScratcher"
myString[1] //K
```

## Number
A number is like what it says.
```dk
myNumber = 123
pi = 3.14
```

As string is an list of characters, a number is a list of digits.
You can also use the indexing mark to get the digits.
```dk
myNumber = 567
myNumber[2] //6
```

## List
Use `[]` to make an list
```dk
myList = [1,2,3]
```

You can even place different type of data in the same list
```dk
myList = [1,hello,True]
```

Lists start at 1, if you prefer to start at 0, please write `l:0` at the first line.

Actually you can set your list start index, but it only works in the first line.
```dk
l:0  //list starts at 0
l:1  //list starts at 1
l:-1 //list starts at -1
l:a  //this will be ignore
```

`[]` can also be indexing mark.
```dk
myList = [5,4,3,2,1]
myList[4] //2
```

You can also edit the value located.
```dk
myList = [5,4,3,2,1]
myList[4] = 10 //[5,4,3,10,1]
```

Of course index can be float.
If there are no value in the index, 0 will be returned
```dk
myList = [5,4,3,2,1]
myList[4.5] // 0
myList[4.5] = 10 //[5,4,3,2,10,1]
```

To get the length, you can use `.length`
```dk
myList.length
```
or `len`
```dk
len myList
len(myList)
// both is ok
```

## Array
An arrays is the same as list, just to make some feel better because they want to use array instead of list.

## Dictionary
key-value pairs

use `{}` to declare a dictionary and use `,` to separate pairs.
```dk
myDict = {1:one,2:two,3:three}
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

## Parentheses
parentheses doesn't do anything in DreamKnot, instead, it's replaced with a white space.
So the following code works the same.
```dk
print(hello)  // hello
print hello   // hello
print()hello  // hello
print)hello(  // hello
```

# Contribution
Please refer to [CONTRIBUTE.md](/CONTRIBUTE.md)
