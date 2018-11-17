

from   django.shortcuts import   render,redirect,HttpResponse



import json
def  server(request):

    func=request.GET.get('callbacks')
    suc='suc'
    msg=json.dumps(func)
    return   HttpResponse('%s'%msg)
