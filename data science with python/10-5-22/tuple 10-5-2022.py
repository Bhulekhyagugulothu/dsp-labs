Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=("apple","mango","banana")
>>> type(s)
<class 'tuple'>
>>> len(s)
3
>>> help(s)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> l=list(s)
>>> print(l)
['apple', 'mango', 'banana']
>>> type(l)
<class 'list'>
>>> l[0]="pineapple"
>>> print(l)
['pineapple', 'mango', 'banana']
>>> s=tuple(l)
>>> print(s)
('pineapple', 'mango', 'banana')
>>> a=("mango","mango","apple","banana")
>>> max(a)
'mango'
>>> s=(1,2,3,10)
>>> max(s)
10
>>> min(a)
'apple'
>>> min(s)
1
>>> t=("pravallika",7)
>>> max(t)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'int' and 'str'
>>> sum(s)
16
>>> any(s)
True
>>> a=
SyntaxError: invalid syntax
>>> 

>>> 

>>> 

>>> 9
>>> a=(0,1,2)
>>> any(a)
True
>>> a=(0,2,3,4)
>>> any(a)
True
>>> n=(0)
>>> any(n)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    any(n)
TypeError: 'int' object is not iterable
>>> any(0)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    any(0)
TypeError: 'int' object is not iterable
>>> a=(1,2,3,4,5)
>>> any(a)
True
>>> b=(0,0,"false")
>>> any(b)
True
>>> b=("0","0","false")
>>> any(b)
True
>>> c=(0,0)
>>> any(c)
False
>>> 
