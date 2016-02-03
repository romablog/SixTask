code = """
i = [0,1,2]
for j in i :
    print(j)
print('hello')
"""

code2 = """
i = [0,1,2]\nfor j in i :\n    print(j)\nprint('hello')
"""

code3 = """
def test(x, y, z):
    print(x,y,z)
    """
exec (code3)
test([1,2,3])

import sys
from io import StringIO

old_stdout = sys.stdout
redirected_output = sys.stdout = StringIO()
exec(code2)
sys.stdout = old_stdout

print (redirected_output.getvalue())


def wrapper1(func, *args): # with star
    func(*args)

def wrapper2(func, args): # without star
    func(*args)

def func2(x, y, z):
    print (x+y+z)

wrapper1(func2, 1, 2, 3)
wrapper2(func2, [1, 2, 3])


code4="""
def tester(a):
    rint(a)

def check(x,y,z):
    print(x,y,z)
"""
code5="""
tester(1)
"""
exec(code4)
exec(code5)
check(*[1,2,3])

