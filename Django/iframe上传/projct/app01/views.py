from django.shortcuts import render,redirect,HttpResponse

# Create your views here.



def index(request):

    return render(request,'index.html')







#ajax的时候post默认是带了请求头的
#而xmlhttprequest是不带的
import json
def ajax1(request):
    print(request.POST)
    print(request.GET)
    print('request body',request.body)
    print(request.POST)
    # print(request.GET['p'])
    ret={'status':True,'message':'alex'}
    return  HttpResponse(json.dumps(ret))
    # return render(request,'ajax1.html')




def index1(request):

    return render(request,'index1.html')






def ajax2(request):
    print(request.POST)
    print(request.GET)
    print('request body',request.body)
    print(request.POST)
    # print(request.GET['p'])
    ret={'status':True,'message':'alex'}
    return  HttpResponse(json.dumps(ret))



def index2(request):

    return render(request,'putfile.html')




def putfile(request):
    print('执行了putfile上传')
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    ret={'status':None,'message':'alex'}
    return  HttpResponse(json.dumps(ret))

