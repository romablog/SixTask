import sys
from io import StringIO
from django.http import HttpResponse
import json

simpleDict = {}
j = '{"action": "print", "method": "onData", "data": "Madan Mohan"}'

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


def simpleFunction(request):
    print(request)
    if request.method == 'GET':
        print(request.GET)
    elif request.method == 'POST':
        print(request.POST)
        code =  request.body
        p = Payload(code)
        #str = functionForExec(p.data)
    return HttpResponse(p.data)

def functionForExec(str):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(str)
    sys.stdout = old_stdout
    return (redirected_output.getvalue())
