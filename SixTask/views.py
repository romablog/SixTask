import sys
from io import StringIO
from django.http import HttpResponse, JsonResponse
import json
import random
import string

simpleDict = {}

j = '''
for i949afd99145346bf9d108edf25ae0710 in range(4):
    print("asdasdasdsad",end="")
for ib13aa23add38472c8e47e9c8d51d2a67 in range(4):
    rint("asda",end="")
    if 2==3:
        print(body, end="")
    print("asdasdasdsgggad",end="")
print("asdasd",end="")'''


def run(request):
    text = json.load(request.body.decode())
    code = simpleDict[text.id]
    result = functionForExec(code)
    return JsonResponse({result: result})


def program(request):
    code = json.load(request.body.decode())
    id = id_generator()
    exception = execution(code.data)
    if exception:
        return JsonResponse({id: "", exception: exception})
    simpleDict[id] = code.data
    return JsonResponse({id: id, exception: ""})


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def functionForExec(str, data):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    ex = execution(str)
    sys.stdout = old_stdout
    if ex:
        return(ex)
    return (redirected_output.getvalue())

def execution(str):
    exeption = ''
    try:
        exec(str)
    except:
        exeption = sys.exc_info()
    return exeption