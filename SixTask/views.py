import sys
from io import StringIO
from django.http import HttpResponse, JsonResponse
import json
import random
import string
import iso8601



j = '''
def test(b, dt):
    for i949afd99145346bf9d108edf25ae0710 in range(4):
        print("asdasdasdsad",end="")
    for ib13aa23add38472c8e47e9c8d51d2a67 in range(4):
        print("asda",end="")
        print(type(dt))
        print("!!!!!!!",end="", sep="")
        if 2==3:
            print(body, end="")
        print("asdasdasdsgggad",end="")
    print("asdasd",end="")'''

simpleDict = {'0000000000': j }


class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


def run(request):
    inf = json.loads(request.body.decode())
    i, values = getData(inf)
    code = simpleDict[i]
    result = functionForExec(code, values)
    print(type(i))
    print(type(result))
    return HttpResponse(result)


def getData(data):
    values = []
    i = ''
    for item in data:
        if 'id' in item:
            i = item['id']
        elif 'date' in item:
            dtime = iso8601.parse_date(item['date'])
            values.append(dtime)
        else:
            values.append(list(item.values())[0])
    return i, values


def program(request):
    data = request.body.decode()
    id = id_generator()
    exception, test = execution(data)
    if exception:
        return HttpResponse(exception)
    simpleDict[id] = data
    return HttpResponse(id)


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def functionForExec(code, val):
    ex, test = execution(code, val)
    if ex:
        return(ex)
    result = callFunction(test, val)
    return result

def execution(str, val):
    exeption = ''
    try:
        exec(str)
    except:
        exeption = sys.exc_info()
    return exeption, locals()['test']

def callFunction(func, vals):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        func(*vals)
    except:
        exception = sys.exc_info()
        return str(exception)
    finally:
        sys.stdout = old_stdout
    return "".join(redirected_output.getvalue())