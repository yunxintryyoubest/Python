




from  rest_framework.authentication import   BaseAuthentication
from    rest_framework.views import   APIView
from   rest_framework.serializers import   ModelSerializer
from   app01  import  models
from   rest_framework.exceptions import    AuthenticationFailed
from   app01.all_config.response import   Self_Response

# class    accountserivializer(BaseAuthentication):
#     '''
#     认证
#
#     '''


from  rest_framework.response import   Response
 ###认证
# class   Auth(BaseAuthentication):
#     def   authenticate(self, request):
#     ##拿到加密的token
#         token=request.query_params.get('token')
#         obj=models.UserToken.objects.get(usertoken=token)
#         res={'code':1000,'msg':None}
#         if   not  obj:
#             raise   AuthenticationFailed({'code':1001,'error':'fail'})
#         # return    (obj.username.username,obj)
#         return   [1,2,3]


##注明一下，这个是get的请求，认证
'''
注明一下，这里的method不被允许是因为在view里面没有设置get的请求方式，所以返回不了
def   get():
pass
'''
from  rest_framework.views import   APIView
from   django.shortcuts import  HttpResponse
class Auth(BaseAuthentication):
    def authenticate(self, request):
        try:
            print('认证开始')
            print(request.data)
            # http://wwwww...c0ovmadfasd/?token=adfasdfasdf
            # print(request.POST.get('token'))
            res = Self_Response()
            # token=request.GET.get('token')
            # print(token)
            # token = request.query_params.get('token')##注明一，这个接受只能是get的请求方式的时候
            # print(token)
            token=request.data.get('token')
            print(token)
            if  not  token:
                token = request.query_params.get('token')##注明一，这个接受只能是get的请求方式的时候
            print('token是',token)
            print(type(token))
            obj = models.UserToken.objects.filter(usertoken=token).first()
            print(obj)
            if not obj:
                print('不存在obj')
                res.code=1001
                res.error='认证失败'
                print(res.get_response)
                raise AuthenticationFailed(res.get_response)
            res.msg='%s'%obj.username.username
            res.code=200
            request.session['username']=models.UserToken.objects.get(usertoken=token).username.username
            request.session['username_id']=models.UserToken.objects.get(usertoken=token).username.pk
            print(request.session.get('username'))
            # res.msg='认证成功%s'%request.GET
            res.msg='认证成功%s'%token
            # return   Response(res.get_response)'
            #注明一下

            #####下面返回的2个分别是request.user,request.auth,分别对应下面的值，当你requets,.auth的时候，就拿到了下面的对象obj，直接是requets.auth.useranem.id就可以拿到用户的id值了
            return (obj.username.username, obj)##3在底层源码里面是元祖的形式
            # return (obj.username.username,'sfgsfsdf')##3在底层源码里面是元祖的形式   not enough values to unpack (expected 2, got 1),必须是两个参数
            # return   Response(res.get_response)
        ##放返回值的时候，就可以直接调用，requets.user,requets.auth来进行使用


        except  Exception  as  e:
            print('异常')
            print(e)
            return  (None,None)



###注明一下，应该返回元祖的形式，是返回两个回去


from   app01 import  models
class  LoginSerilazer(ModelSerializer):
    class  Meta:
        model = models.Userinfo
        fields = '__all__'


