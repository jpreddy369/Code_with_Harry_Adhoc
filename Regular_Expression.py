import re

# str1 = 'This is normal\nstring'
# print(str1)
# strr2 = r'This is normal \n string'
# print(strr2)

reg = r'm\w'


prog = re.compile(r'm\w\w')

str = 'cat mat bat rat'
result = prog.search(str)
print(result.group())


str1 = 'Operating system format'
result = prog.search(str1)
print(result.group())

# instead of compile and running, we can use single step

result = re.search(r'm\w\w', str1)
