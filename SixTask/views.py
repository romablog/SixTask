import sys
from io import StringIO
from django.http import HttpResponse, JsonResponse
import json
import random
import string
import iso8601

simpleDict = {}

j = '''
for i949afd99145346bf9d108edf25ae0710 in range(4):
    print("asdasdasdsad",end="")
    print(b)
for ib13aa23add38472c8e47e9c8d51d2a67 in range(4):
    rint("asda",end="")
    if 2==3:
        print(body, end="")
    print("asdasdasdsgggad",end="")
print("asdasd",end="")'''

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


def run(request):
    inf = json.loads(request.body.decode())
    i, values = getData(inf)
    code = simpleDict[i]
    functionForExec(code)
    result = test(*values)
    return HttpResponse(inf['id']+result)


def getData(data):
    values = []
    i = ''
    for item in data:
        if item == 'id':
            i = item[item.keys[0]]
        elif 'date' in item:
            dtime = iso8601.parse_date(item['date'])
            values.append(dtime)
        else:
            values.append(item[item.keys[0]])
    return i, values


def program(request):
    data = json.loads(request.body.decode())['data']
    id = id_generator()
    exception = execution(data)
    if exception:
        return HttpResponse(exception)
    simpleDict[id] = data
    return HttpResponse(id)


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