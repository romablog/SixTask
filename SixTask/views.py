from django.http import *
import random
import sys



l = """for i949afd99145346bf9d108edf25ae0710 in range(4):
    print("asdasdasdsad",end="")

for ib13aa23add38472c8e47e9c8d51d2a67 in range(4):
    print("asda",end="")

    if 2==3:
        print("body",end="")
    print("asdasdasdsgggad",end="")
print("asdasd",end="")"""


def dhb(request):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(request)
    sys.stdout = old_stdout

dhb(l)

# code = """
# i = [0,1,2]
# for j in i :
#     print(j)
# print('hello')
# """
#
# code2 = """
# i = [0,1,2]\nfor j in i :\n    print(j)\nprint('hello')
# """
#
# import sys
# from io import StringIO
#
# old_stdout = sys.stdout
# redirected_output = sys.stdout = StringIO()
# exec(code2)
# sys.stdout = old_stdout
#
# print(redirected_output.getvalue())