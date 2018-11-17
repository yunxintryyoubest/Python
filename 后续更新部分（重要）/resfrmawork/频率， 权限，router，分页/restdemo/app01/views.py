from django.shortcuts import render,HttpResponse

# Create your views here.

from django.views import View
from rest_framework.response import Response
from .models import *

from app01.serilizer import *


from rest_framework.views import APIView
# Publish表
class PublishView(APIView):
    def get(self,request):

        # restframework
        # 取数据
        # print("request.data", request.data)
        # print("request.data type", type(request.data))
        # print(request._request.GET)
        # print(request.GET)
        # 序列化
        # 方式1：
        # publish_list=list(Publish.objects.all().values("name","email"))

        # 方式2：
        # from django.forms.models import model_to_dict
        # publish_list=Publish.objects.all()
        # temp=[]
        # for obj in publish_list:
        #     temp.append(model_to_dict(obj))

        # 方式3：
        # from django.core import serializers
        # ret=serializers.serialize("json",publish_list)

        # 序列组件
        publish_list = Publish.objects.all()
        ps = PublishModelSerializers(publish_list, many=True)
        return Response(ps.data)

    def post(self,request):
        # 取数据
        # 原生request支持的操作
        # print("POST",request.POST)
        # print("body",request.body)
        # # print(request)
        # print(type(request))
        # from django.core.handlers.wsgi import WSGIRequest
        #  新的request支持的操作
        # print("request.data",request.data)
        # print("request.data type",type(request.data))


        #
        # post请求的数据
        ps = PublishModelSerializers(data=request.data)
        if ps.is_valid():
            print(ps.validated_data)
            ps.save()  # create方法
            return Response(ps.data)
        else:
            return Response(ps.errors)
class PublishDetailView(APIView):
    def get(self, request, pk):

        publish = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish)
        return Response(ps.data)

    def put(self, request, pk):
        publish = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish, data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.errors)

    def delete(self, request, pk):
        Publish.objects.filter(pk=pk).delete()

        return Response()




from rest_framework.parsers import JSONParser,FormParser,MultiPartParser,FileUploadParser
# Book表

from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    page_size_query_param="size"
    max_page_size=2




class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit=1

class BookView(APIView):
    # authentication_classes = [TokenAuth,] # [TokenAuth(),]
    # permission_classes = []
    # throttle_classes = []
    parser_classes = [JSONParser,FormParser]

    def get(self,request):
        print("request.user",request.user) 
        print("request.auth",request.auth)
        print("_request.body",request._request.body)
        print("_request.GET",request._request.GET)
        book_list=Book.objects.all()

        # 分页

        pnp=MyLimitOffsetPagination()
        books_page=pnp.paginate_queryset(book_list,request,self)

        bs=BookModelSerializers(books_page,many=True,context={'request': request})
        return Response(bs.data)
    
    def post(self,request):
        # post请求的数据

        print("request.data",request.data)


        bs=BookModelSerializers(data=request.data)
        if bs.is_valid():
            print(bs.validated_data)
            bs.save()# create方法
            return Response(bs.data)
        else:
            return Response(bs.errors)



class BookDetailView(APIView):

    def get(self,request,id):

        book=Book.objects.filter(pk=id).first()

        bs=BookModelSerializers(book,context={'request': request})

        return Response(bs.data)

    def put(self,request,id):
        book=Book.objects.filter(pk=id).first()
        bs=BookModelSerializers(book,data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self,request,id):
        Book.objects.filter(pk=id).delete()

        return Response()

# ##############################################################Author

# from rest_framework import mixins
# from rest_framework import generics
#
# class AuthorView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Author.objects.all()
#     serializer_class =AuthorModelSerializers
#
#     def get(self,request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class AuthorDetailView(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializers
#
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)
#
#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)
#
#     def put(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)

##############################################################################

#
# from rest_framework import mixins
# from rest_framework import generics
#
#
# class AuthorView(generics.ListCreateAPIView):
#     queryset=Author.objects.all()
#     serializer_class =AuthorModelSerializers
#
# class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializers

##############################################################################

from rest_framework import viewsets

from app01.utils import TokenAuth



from app01.utils import SVIPPermission



class VisitRateThrottle(object):
    def allow_request(self,request,view):
        # 要求访问站点的频率不能超过每分钟20次
        if 1:
            print(request.META.get("REMOTE_ADDR"))

            return True
        else:
            return False


from rest_framework.response import  Response


class AuthorModelView(viewsets.ModelViewSet):

    #authentication_classes = [TokenAuth,]
    #permission_classes=[SVIPPermission,]
    #throttle_classes = [VisitRateThrottle]    # 限制某个IP每分钟访问次数不能超过20次
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers
    pagination_class = MyPageNumberPagination
    renderer_classes = []


def get_random_str(user):
    import hashlib,time
    ctime=str(time.time())

    md5=hashlib.md5(bytes(user,encoding="utf8"))
    md5.update(bytes(ctime,encoding="utf8"))

    return md5.hexdigest()


from .models import User

class LoginView(APIView):
    authentication_classes = []
    def post(self,request):

        name=request.data.get("name")
        pwd=request.data.get("pwd")
        user=User.objects.filter(name=name,pwd=pwd).first()
        res = {"state_code": 1000, "msg": None}
        if user:

            random_str=get_random_str(user.name)
            token=Token.objects.update_or_create(user=user,defaults={"token":random_str})
            res["token"]=random_str
        else:
            res["state_code"]=1001 #错误状态码
            res["msg"] = "用户名或者密码错误"

        import json
        return Response(json.dumps(res,ensure_ascii=False))





