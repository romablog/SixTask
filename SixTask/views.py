import sys
from io import StringIO
from django.http import HttpResponse
import json

simpleDict = {}
j = '{"action": "print", "method": "onData", "data": "Madan Mohan"}'


def simpleFunction(request):
    print(request.POST)
    code = json.load(request.body.decode())
    result = functionForExec(code.data)
    return HttpResponse(result.encode())


def functionForExec(str):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(str)
    sys.stdout = old_stdout
    return (redirected_output.getvalue())
