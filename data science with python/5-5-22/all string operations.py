Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="bhulekhya is very beautiful"
>>> s.capitalize()
'Bhulekhya is very beautiful'
>>> s.center()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s.center()
TypeError: center expected at least 1 argument, got 0
>>> s.count('e')
3
>>> s.endswith('l')
True
>>> s.endswith('y')
False
>>> s.find('b')
0
>>> s.find('v')
13
>>> s.index('e')
4
>>> s.isalnum()
False
>>> s.isalpha()
False
>>> s.isascii()
True
>>> s.isdigit()
False
>>> s.islower()
True
>>> s.isnumeric()
False
>>> s.isprintable()
True
>>> s.isspace()
False
>>> s.istitle()
False
>>> s.title()
'Bhulekhya Is Very Beautiful'
>>> s.isupper()
False
>>> s1="girl"
>>> join(s,s1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    join(s,s1)
NameError: name 'join' is not defined
>>> s1.join(s)
'bgirlhgirlugirllgirlegirlkgirlhgirlygirlagirl girligirlsgirl girlvgirlegirlrgirlygirl girlbgirlegirlagirlugirltgirligirlfgirlugirll'
>>> s.lower()
'bhulekhya is very beautiful'
>>> s.partition('v')
('bhulekhya is ', 'v', 'ery beautiful')
>>> s.partition("is")
('bhulekhya ', 'is', ' very beautiful')
>>> s.replace("very","so")
'bhulekhya is so beautiful'
>>> s.startswith('v')
False
>>> s.startswith('b')
True
>>> s.startswith('i')
False
>>> s.strip()
'bhulekhya is very beautiful'
>>> s1.swapcase()
'GIRL'
>>> print( s1)
