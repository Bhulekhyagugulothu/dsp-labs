Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="data science with python"
>>> print(name[5])
s
>>> print(name[-3])
h
>>> print(name[5:-3])
science with pyt
>>> print(name[4:0])

>>> print(name[6:-4])
cience with py
>>> name.upper()
'DATA SCIENCE WITH PYTHON'
>>> name.lower()
'data science with python'
>>> name.isupper()
False
>>> name.islower()
True
>>> m="prakhya"
>>> g="prakhya"
>>> print(m+g)
prakhyaprakhya
>>> print("name=",name)
name= data science with python
>>> print(name[0,5,13,18])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(name[0,5,13,18])
TypeError: string indices must be integers
>>> print(name[0],name[5],name[13],name[18])
d s w p

index("a")


