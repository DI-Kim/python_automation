# more about strings

import pyperclip

"""
\' single quote
\" double quote
\t tab
\n new line
\\ backslash
"""

"That's a string"
'That\'s a string'
'He said "Hello"'

spam = 'Hello, world!'
print(spam[0])  # 'H'
print(spam[0:5])  # 'Hello'
print(spam[-1])  # '!' (last character)
print('x' in spam)  # True if x is in spam
print('HELLO' in spam)  # False (case-sensitive)
print('HELLO' in spam.upper())  # True (upper() converts to uppercase)
print('hello' in spam.lower())  # True (lower() converts to lowercase)
print(spam.startswith('Hello'))  # True (starts with 'Hello')
print(spam.endswith('world!'))  # True (ends with 'world!')

print(','.join(['a', 'b', 'c']))  # 'a,b,c' (joins list with comma)
print('a,b,c'.split(','))  # ['a', 'b', 'c'] (splits string by comma)
print('My name is Simon'.split())
# ['My', 'name', 'is', 'Simon'] (splits by whitespace)
print('       x       '.strip())  # 'x' (whitespace to remove)

pyperclip.copy('Hello, world!')  # Copy to clipboard
print(pyperclip.paste())  # Paste from clipboard

# formatting
age = 30
name = 'Simon'
# 'My name is Simon and I am 30 years old'
print('My name is {} and I am {} years old'.format(name, age))
print(f'My name is {name} and I am {age} years old')  # f-string (Python 3.6+)
