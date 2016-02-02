import sys
from io import StringIO
from django.http import JsonResponse

simpleDict = {}


def simpleFuction(request):
    if request.method == 'GET':
        print(request.GET)
    elif request.method == 'POST':
        print(request.POST)
        code =  request.POST['data']
        str = functionForExec(code)
    return JsonResponse({'foo': str})

def functionForExec(str):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(str)
    sys.stdout = old_stdout
    return (redirected_output.getvalue())
