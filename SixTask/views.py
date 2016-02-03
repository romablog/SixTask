import sys
from io import StringIO
from django.http import HttpResponse, JsonResponse
import json
import random
import string

simpleDict = {}
j = '{"action": "print", "method": "onData", "data": "Madan Mohan"}'


def run(request):
    text = json.load(request.body.decode())
    code = simpleDict[text.id]
    result = functionForExec(code)
    return JsonResponse({result: result})

def program(request):
    code = json.load(request.body.decode())
    id = id_generator()
    simpleDict[id] = code
    return JsonResponse({id: code})

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def functionForExec(str):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(str)
    sys.stdout = old_stdout
    return (redirected_output.getvalue())
