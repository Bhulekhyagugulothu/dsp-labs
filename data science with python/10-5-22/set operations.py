Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={2,3,4,5}
>>> f={4,5,6,7}
>>> s.union(f)
{2, 3, 4, 5, 6, 7}
>>> s.intersection(f)
{4, 5}
>>> s={1,2}
>>> h={6}
>>> s.intersection(h)
set()
>>> s.difference(h)
{1, 2}
>>> s.add('t')
>>> print(s)
{1, 2, 't'}
>>> s.add(1)
>>> print(s)
{1, 2, 't'}
>>> s.remove(1)
>>> print(s)
{2, 't'}
>>> f.discard(6)
>>> print(f)
{4, 5, 7}
>>> f.discard(2)
>>> print(f)
{4, 5, 7}
>>> f.pop()
4
>>> f.pop(0)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    f.pop(0)
TypeError: pop() takes no arguments (1 given)
>>> f.pop(5)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    f.pop(5)
TypeError: pop() takes no arguments (1 given)
>>> f=
SyntaxError: invalid syntax
>>> g={3,4,5,6,7}
>>> g.pop(2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    g.pop(2)
TypeError: pop() takes no arguments (1 given)
>>> del(g)
>>> print(g)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(g)
NameError: name 'g' is not defined
>>> g={1,2,3,4,5,6}
>>> del[2:5]
SyntaxError: invalid syntax
>>> insert(0,5)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    insert(0,5)
NameError: name 'insert' is not defined
>>> g.insert(0,5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    g.insert(0,5)
AttributeError: 'set' object has no attribute 'insert'
>>> g.clear()
>>> print(g)
set()
>>> b={1,3}
>>> d={4,5}
>>> b&d
set()
>>> b|d
{1, 3, 4, 5}
>>> b.subset(d)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b.subset(d)
AttributeError: 'set' object has no attribute 'subset'
>>> j={4,5,3,2,7}
>>> j.sort()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    j.sort()
AttributeError: 'set' object has no attribute 'sort'
>>> sort(j)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    sort(j)
NameError: name 'sort' is not defined
>>> b.issubset(d)
False
>>> a={1,2,3,4}
>>> b={3,4}
>>> b.issubset(a)
True
>>> a={3,4,5}
>>> b={1,2}
>>> a.issubset(b)
False
>>> a.issuperset(b)
False
>>> a={1,2,3,45}
>>> n={1,2}
>>> a.issuperset(b)
True
>>> 