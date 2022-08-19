Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3]
>>> print(l)
[1, 2, 3]
>>> l1=["ram",'mom']
>>> print(l1)
['ram', 'mom']
>>> l=[1,2,"hello",[23.5,7.89,4],'e']
>>> print(l)
[1, 2, 'hello', [23.5, 7.89, 4], 'e']
>>> l[:3]
[1, 2, 'hello']
>>> l[0:4]
[1, 2, 'hello', [23.5, 7.89, 4]]
>>> l[5:]
[]
>>> l[-4:-1]
[2, 'hello', [23.5, 7.89, 4]]
>>> l[-1:-4]
[]
>>> l3=l+l1
>>> print(l3)
[1, 2, 'hello', [23.5, 7.89, 4], 'e', 'ram', 'mom']
>>> l=[1,2,3,4]
>>> l.append(6)
>>> print(l)
[1, 2, 3, 4, 6]
>>> l.append([5,7])
>>> print(l)
[1, 2, 3, 4, 6, [5, 7]]
>>> 