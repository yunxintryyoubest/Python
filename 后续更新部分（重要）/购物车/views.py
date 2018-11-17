from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from    app01.all_config  import  accounts
from   rest_framework.views import   APIView
from   rest_framework.response import   Response
from   app01.all_config.response import Self_Response
def   index(request):



    return   HttpResponse('index')

from  rest_framework.generics import   mixins
from   rest_framework.viewsets import   ViewSetMixin
from app01.all_config.accounts import LoginSerilazer
from  app01  import models

class  Register(ViewSetMixin,APIView):
    def register(self,request):
        res={'code':1000,'msg':'fail'}
        user=LoginSerilazer(data=request.data)
        print(request.data)
        ##去重
        username = request.data.get('username')
        all_user = models.Userinfo.objects.all()
        dic = []
        for i in all_user:
            dic.append(i.username)
        if username in dic:
            res['code']=400
            res['msg'] = '已经存在此用户'
        elif  user.is_valid():
            user.save()
            res['code']=200
            res['msg']='创建用户成功'
        return  Response(res)




from  django.db.models  import FieldDoesNotExist
class  Login(APIView):
    '''
    当登陆的时候，创建token进来
    '''
    def post(self,request):
        res=Self_Response()
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = models.Userinfo.objects.get(username=username, password=password)
            if user:
                ##存在用户
                import uuid
                ran_str = str(uuid.uuid4())
                models.UserToken.objects.update_or_create(username=user, defaults={'usertoken': ran_str})
                res.msg='设置token成功%s' % ran_str
                res.code=200
                return Response(res.get_response)
        except   ObjectDoesNotExist  as e:
            res.error='不存在此用户'
            res.code=404
            return   Response(res.get_response)








from   django.core.exceptions import   ObjectDoesNotExist
##当文件不存在的时候
from   app01.all_config.accounts import   Auth

##添加课程进来，对每一个用户进行进行添加课程进来


class    AccountView(APIView):
    '''
    进行认证
    '''
    authentication_classes = [Auth,]
    def   post(self,request,*args,**kwargs):
        # print(request.POST)
        '''
        添加课程进入购物车,需要课程id传，courseid，policyid
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        dic={'code':1000,'msg':None}
        res = Self_Response()
        print(request.data)
        try:
            # username = request.data.get['username']
            res.msg='成功'
            print(res)
            return  Response(res.msg)

        except  Exception as e:

            res.msg='异常'
            print(res)
            return   Response('fail')











#
from  django.contrib.contenttypes.models  import   ContentType

# def  test(request):
    ##查找
    ##根据某个价格策略对象，找到他对应的表和数据，自动关联找到
    # price = models.PricePolicy.objects.get(id=2)
    # print(price)
    # print(price.content_object.username.username)


    ##查找，根据课程表来查找,可以拿到所哟所关联的所有价格策略，只要是相同的id
    # objs = models.Course.objects.get(id=1)
    # val=objs.price_policy.all()##说明一下，这个名字是固定的
    # for  i in val:
    #     print(i)
    # print(objs,val)

        # print(type(i.policy))
    # print(objs.policy.content_type)
    ##拿到一个一个的对象

    #创建数据1：
    ##在价格策略表里面添加一个数据  ContentType去这里面拿数据
    # models.PricePolicy.objects.create(price=2233,
    #                                   content_type=ContentType.objects.get(model='course'),
    #                                   object_id=1,
    #                                   )
    # 创建数据2：
    ##ContentType去这里面拿数据
    # models.PricePolicy.objects.create(price=22332,
    #                                   content_object=models.UserDetail.objects.get(id=1)
    #                                   )

    # return   HttpResponse('suc')


from 购物车.settings import shopping
from  django.contrib.contenttypes.models  import   ContentType
import  redis
from  app01  import  models
from     django_redis import   get_redis_connection
conn = get_redis_connection('default')  # default是连接池的名称
def  test(request):
    val = models.Userinfo.objects.all()
    res=Self_Response()
    try:
            ##获取用户提交的课程id和价格策略id
        print(request.GET)
        userid=request.data.get('userid')
            # policy_id=request.data.get('policyid')
        val1 = models.Userinfo.objects.filter(id='%s'%userid).first()
        ##注明一下啊，这个价格策略相当于是manytomany的
        good_detail_dic = {}
        for i in val1.course_name.all():
            name = 'good_%s【id】_%s【course】' % (2, i)
            for item in val1.price_policy.all():
                detail = {}
                detail['course_perid'] = item.get_course_perid_display()
                detail['price'] = item.price
                detail['img'] = item.goods_img
                detail['expire_time'] = item.get_expire_time_display()
                good_detail_dic[name] = detail
                conn.hset(name, 'course_perid', (detail['course_perid']))
                conn.hset(name, 'price', detail['price'])
                conn.hset(name, 'img', detail['img'])
                conn.hset(name, 'expire_time', detail['expire_time'])
                # return   render(request,'shopping_car.html',locals())
                res.code=1001
                res.msg='suc'
                return    Response(res.get_response)
    except  Exception  as e:
        print(e)
    return   HttpResponse('fail')

'''
genicforeign是从本表关联其他表查询的
related是其他所管来关联的来进行查询的
'''





######在这里优化处理
res = Self_Response()
from   app01.all_config.accounts import   Auth
class   shopping_car(APIView):
    authentication_classes = [Auth, ]
    ##如果认证成功的话，就可以执行下面的步骤,重点
    # def  get(self,request,*args,**kwargs):
    #     authentication_classes = [Auth, ]
    #     print(request.GET)
    #     res.code=200
    #     token=request.GET.get('token')
    #     request.session['username']=models.UserToken.objects.get(usertoken=token).username.username
    #     request.session['username_id']=models.UserToken.objects.get(usertoken=token).username.pk
    #     print(request.session.get('username'))
    #     res.msg='认证成功%s'%request.GET
    #     return   Response(res.get_response)

    def   post(self,request,*args,**kwargs):
        if   not   request.auth:##假如没有返回值得话，就说明是认证失败
            return  Response('认证失败,token有误.........')

        '''添加商品到购物车的操作'''
        '''
        接受到两个参数，一个是课程id，一个是价格策略,添加数据的操作
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        '''
        价格策略就是说linux可以非常多的版本，比如这个linux的时间不同，价格不同，周期不同等'''
        try:
            print('进入到添加页面')
            print('用户id是', request.session['username_id'])
            user_id = request.session['username_id']
            course_id=request.POST.get('course_id')
        ##可能一个商品里面有很多的价格策略

            pricepolicy_id=int(request.POST.get('pricepolicy_id'))##价格策略的idUI对应course的id，就是说当course有id为1的时候，价格策略就为1

            all_course_id = []
            pricepolicy_list={}
            for j in models.Course.objects.values('id'):
                all_course_id.append(j['id'])
            # for j in models.Course.objects.get(id=course_id):
            course_obj = models.Course.objects.get(id=course_id)
            for   i in   course_obj.price_policy.all():
                pricepolicy_list[i.id] = {
                    'price': i.price,
                    'expire_time': i.get_expire_time_display(),
                    'course_perid': i.get_course_perid_display(),
                    'diff_level': i.get_course_diff_level_display(),
                    'course_level': i.get_course_level_display(),
                }

            # print('所有的价格策略是:',pricepolicy_list)
            # print(conn.keys())
                    # pricepolicy_list = {
                    #     'price': i.price_policy.price,
                    #     'expire_time': i.price_policy.get_expire_time_display(),
                    #     'course_perid': i.price_policy.get_course_perid_display(),
                    #     'diff_level': i.price_policy.get_course_diff_level_display(),
                    #     'course_level': i.price_policy.get_course_level_display(),
                    # }

            ##取出所有的课程id
            # name='User_Shop_Car_%s_%s'%(course_id,pricepolicy_id)
            name=shopping%(user_id,course_id)
            # name='User_Shop_Car_%s_%s'%(user_id,course_id)
            ##判断这个价格策略id存在还是不存在（更具对应的课程id来进行判断）
            import json
            if pricepolicy_id not in pricepolicy_list:
                res.code = 404
                res.error = '价格策略不合法'
                res.all_data=None
                return Response(res.get_response)
            public_dic = {
                'name': course_obj.course_name,
                'img': course_obj.goods_img,
                'default': pricepolicy_id,
                'pricepolicy_list': json.dumps(pricepolicy_list)
                # 'pricepolicy_list': pricepolicy_list
            }
            '''注明一下，有局限，后面的价格策略只能有一个，不能多个'''
            ##存入redis里面
            conn.hmset(name, public_dic)####批量价数据进去，可以后面直接是字典的形式
            res.code=200
            res.all_data=None
            # res.msg='添加数据成功%s'%public_dic
            res.msg=conn.keys()
            res.error=None
            # val = str(conn.hget(name, 'pricepolicy_list'), encoding='utf-8')
            # res.msg=json.loads(val)
            # res.default='课程%s的默认价格策略是%s'%(name,pricepolicy_id)

            res.default=pricepolicy_id
            print('继续*'*100)
            print(all_course_id)
            print(pricepolicy_id)
        except ObjectDoesNotExist as e:
            res.msg = 'course_id不存在'
        except  Exception  as   e:
            res.error=400
            res.msg='错误，添加失败'
        return   Response(res.get_response)
    def  delete(self,request):
        print('进入删除')
        '''
            删除购物车里面的东西,可以删除多个商品，所以列表的形式
        :return:
        '''
        # print(request)

        user_id=request.session.get('username_id')
        course_id_list=request.data.get('course_id')
        ##删除
        all_val=conn.keys()
        del_name_list=[shopping%(user_id,    i  )  for  i in course_id_list]
        conn.delete(*del_name_list)
        print('删除成功')
        all_val = conn.keys()
        print(all_val)
        return   Response(all_val)
#######局部更新

    def  patch(self,request,*args,**kwargs):
        '''
        修改价格策略，局部更新
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        try:
            course_id=request.data.get('course_id')
            pricepolicy_id=request.data.get('pricepolicy_id')
            all_course_ids=[ i['id']  for   i in  models.Course.objects.values('id')]
            after_ids = [i['id'] for i in models.Course.objects.filter(id=course_id).first().price_policy.values('id')]
            if  int(course_id)  not in  all_course_ids:
                res.code=1001
                res.error='不存在此课程'
                return  Response(res.get_response)
            if int(pricepolicy_id)  not   in  after_ids:
                res.code=1001
                res.error='价格策略不合法'
                res.msg=None
                res.all_data=None
                return    Response(res.get_response)
            ##进行修改
            name=shopping%(request.session.get('username_id'),course_id)
            print(name)
            print(type(name))
            conn.hset(name,'default',pricepolicy_id)
            res.code=200
            res.msg='修改成功'
            res.error=None
            all_data=conn.hget(name,'pricepolicy_list')
            import json
            all_data=json.loads(all_data.decode('utf-8'))
            # after_dic = {}
            # for i in all_data:
            #     after_dic[str(i, encoding='utf-8')] = str(all_data[bytes(i)], encoding='utf-8')
            # res.all_data=after_dic
            res.all_data=all_data[(pricepolicy_id)]
            res.modify_result='修改之后的价格策略是%s'%pricepolicy_id
            return   Response(res.get_response)
        except  Exception  as e:
            res.code=1003
            res.error='修改失败'
            print(e)
            return  Response(res.get_response)
    def  get(self,request,*args,**kwargs):
        '''
        查看购物车所有商品
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        '''
        讲解一下，当这个请求发送过来的时候，后面的course_id不要设置，所以是*，匹配所有的内容出来
        这个当前的用户可以多个商品，所以是多个值shoping_1_1,shoping_1_2,shoping_1_3等,conn.getall(shopping_1_1)，把全部拿到的商品放进一个列表里面
        返回
        '''
        try:
            all_course_list=[]
            name = shopping % (request.session.get('username_id'), '*')  ##后面的*代表所有的course_id
            print(name)
            all_data = conn.keys()
            al=conn.hgetall(name)
            print(al)
            import    json
            '''decode可以将字节转化为字符串，json.loads可以内部将序列化'''
            for key in conn.scan_iter(name, count=10):
                key=str(key,encoding='utf-8')
                print(key)
                dic1 = {
                    'name': str(conn.hget(key, 'name'), encoding='utf-8'),
                    # 'pricepolicy_list':str(conn.hget('User_Shop_Car_1_2','pricepolicy_list'),encoding='utf-8'),
                    'pricepolicy_list': json.loads(conn.hget(key, 'pricepolicy_list').decode('utf-8')),
                    'img': str(conn.hget(key, 'img'), encoding='utf-8'),
                    'default': str(conn.hget(key, 'default'), encoding='utf-8'),
                }
                all_course_list.append(dic1)##可以一个用户多个商品，所以是列表的形式，把全部的商品放进去
            print(all_course_list)
            all_data=all_course_list
            res.all_data = all_data
            res.code = 200
            res.error=None
            return   Response(res.get_response)
        except  Exception  as e:
            res.error='查看商品失败'
            return   Response(res.get_response)

##注明一下，这个response，和httpresponse是http的请求的格式，可以渲染出来，当是其他的格式的时候，是渲染不出来的
'''AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, 
but received a `<class 'str'>`'''







def  pricepolicy_id_not_exist(pricepolicy_id,all_course_id,res):
    if pricepolicy_id   not   in all_course_id:
        return  True



















