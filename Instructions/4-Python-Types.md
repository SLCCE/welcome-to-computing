# Python Types

The data we use in coding have classifications. These are called types. The three main types we’ll be learning are ints, strings, and floats.

A string, or str is a combination of characters. Strings are differentiated by quotes. They can be either single quotes or double quotes.  
For example:

```py
'this is a string'
"this is also a string"
```

An int is short for integer, which is a countable number. Ints cannot have decimal places in them.  
For example:

```py
1
10
45
```

Lastly, a float is a number, similar to an int. However, floats contain decimal places.  
For example:

```py
1.0
3.14
5.86325
```

To check what type a piece of data is, you can use the type function and input your data inside it.  
For example:

```py
type('hello!')
>>> str
type(4)
>>> int
type(8.7)
>>> float
```

Finally, if it’s possible, you can change the type of your data using different type functions. You can use the str(), int(), and float() functions.

```py
# changes value to a string
str(3)
>>> '3'

# changes value to an int
int(4.0)
>>> 4

# changes value to a float
float('5.673')
>>> 5.673
```
