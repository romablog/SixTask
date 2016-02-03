def check(**kwargs):
    a = kwargs["a"]
    print(a)

check(a=1)

code = """
i = [0,1,2]\nfor j in i :\n    print(j)\nprint('hello')
"""

exec(code)


dic = {"d":1, "b": 3, 4: 5 }
print(dic.keys())