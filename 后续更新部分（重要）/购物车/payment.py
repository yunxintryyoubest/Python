
from   rest_framework.viewsets import   ModelViewSet
from   rest_framework.views import   APIView
from   rest_framework.response import    Response
from   app01.all_config.accounts import     Auth
from   购物车.settings    import    shopping,all_pay_courses_coupon,golbal_pay_course_coupon
from   django_redis  import get_redis_connection
import   json
from   app01.all_config.response import   Self_Response
import  datetime
from   app01  import models
from   rest_framework.generics import   GenericAPIView
#可以自定制函数名字，不用默认的get，post等函数名字

##结算中心
'''
pay_course_id_price_plocy_id:{
img:'',
name:'',
price:'',
........

'''
conn=get_redis_connection('default')
class   Payment_Viewset(APIView):
    authentication_classes = [Auth,]
    res = Self_Response()
    def post(self,request,*args,**kwargs):
        ##后面的2个参数可能会有其他的参数（比如版本等）
        try:
            username_id = request.auth.username.id  # requets.user,requets,auth
            username = request.user


            '''
            原理讲解：
            首先进来的时候，现将这个缓存里面的优惠卷清空，在进行设置优惠卷的信息，初始化
            获取这个传入的课程id，在根据用户id（username_id），来拿到这个用户下的课程对应的优惠卷，匹配出来
            生成字典，用户id：{
                        全局优惠卷：{
                            全局卷：
                            满减卷：
                            折扣卷：}
                        课程卷（局部卷）：{
                            课程：{
                            全局卷：
                            满减卷：
                            折扣卷：}
                                }
            在存入这个redis缓存里面
            '''
            ##当结算的时候，把这个全部的优惠卷信息给清空了，当再次结算的时候，在添加进去
            # key_list = conn.keys(all_pay_courses_coupon % (username_id, '*'))####shoping_username_id_*
            # conn.delete(*key_list)##批量删除，上面的keys是去到多个字典的键出来
            key_list = conn.keys(all_pay_courses_coupon % (username_id, '*'))####shoping_username_id_*
            key_list.append(golbal_pay_course_coupon%username_id)####把全局的优惠卷加进来
            conn.delete(*key_list)#批量删除，上面的keys是去到多个字典的键出来

            all_course_id_list = []
            for i in request.data.get('course_id').split(','):
                all_course_id_list.append(int(i)  )
            print(all_course_id_list)
            # username_id=request.session.get("username_id")
            all_pay_course_ment=[]
            for   course_id   in  all_course_id_list:

                print(course_id)
                # course_id=int(request.data.get('course_id'))
                course_obj = models.Course.objects.filter(pk=course_id).first()
                if   not  course_obj:
                    error='404没有找到这个课程'
                    return  Response(error)
                name = shopping % (username_id, course_id)
                all_data=conn.hgetall(name)
                if  not  all_data:
                    raise   FileExistsError('不存在此商品')
                # for   i in all_data:
                all_dic={
                    'name': str(conn.hget(name, 'name'), encoding='utf-8'),
                    'img':str(conn.hget(name,'img'),encoding='utf-8'),
                    'default_price_policy': str(conn.hget(name, 'default'), encoding='utf-8'),
                    'global_coupon':{},
                    # 'coupon':{},
                    'default_golbal_coupon':0,
                    'course_coupon':0
                }
                price_policy_id=all_dic['default_price_policy']
                pricepolicy_list_dic=conn.hget(name,'pricepolicy_list')
                ##拿到价格策略里面的对象，取出相对应的超时时间，价格等信息
                price_policy_val=json.loads(str(conn.hget(name, 'pricepolicy_list'), encoding='utf-8'))
                add_dic = {
                    'price': price_policy_val[price_policy_id]['price'],
                    'expire_time': price_policy_val[price_policy_id]['expire_time'],
                    'course_perid': price_policy_val[price_policy_id]['course_perid']
                }

                '''优惠卷信息如下'''
                import    datetime
                ctime=datetime.datetime.now()

                val2 = models.CouponRecord.objects.filter(**{
                    'account__username': '%s'%username,
                    'status': 0,
                    'coupon__valid_begin_date__lte': ctime,
                    'coupon__valid_end_date__gte': ctime
                })


              ##全局的优惠卷信息
                from  app01.all_config.all_conpon_pay import   get_course_conpon,get_all_conpon
                course_conpon_dic={}
                global_conpon_dic = {}
                for i in val2.all():
                    obj = models.Course.objects.filter(id=i.coupon.object_id)
                    if obj:
                        print('局部')
                        # print('*' * 1000)
                        name = obj.values('course_name')[0]['course_name']
                        course_conpon_dic[name] = {}
                        course_conpon_dic[name]['default_course_coupon']=0
                        # add_course_conpon_dic={
                        #     'title':name,
                        #     'course_id':i.coupon.object_id,
                        #     'default_course_coupon':0,
                        #     'img':obj.values('goods_img')[0]['goods_img'],
                        #     'price':models.PricePolicy.objects.filter(object_id=i.coupon.object_id).first().price,
                        # }
                        # course_conpon_dic.update(add_course_conpon_dic)
                    else:
                        print('全局')
                        global_conpon_dic = get_all_conpon(i)
                print('*'*1000)
                all_dic['global_coupon'].update(global_conpon_dic)
                print(all_dic['global_coupon'])
                print('all'*100)

                '''课程优惠卷信息'''
                for course_obj in val2:
                    # 先处理已经绑定优惠卷的
                    if course_obj.coupon.object_id:
                        ##已经把那个绑定课程id的优惠卷
                        course_naem_id = course_obj.coupon.object_id
                        name = models.Course.objects.filter(id=course_naem_id).values('course_name')[0]['course_name']
                        conpon_type = get_course_conpon(course_obj)
                        course_conpon_dic[name][course_obj.coupon.pk] = conpon_type
                    ##处理全局的，没有绑定课程的优惠卷

                all_dic.update(course_conpon_dic)
                # print(all_dic['coupon'])
                '''写入到redis里面去'''
                pay_course_coupon_list=all_pay_courses_coupon%(username_id,course_id)
                golbal_pay_coupon_list=golbal_pay_course_coupon%username_id
                print(pay_course_coupon_list,golbal_pay_coupon_list)

                ####可以一直存的，不会报错
                ##存入课程的优惠卷
                # redis_course_coupon={
                #     'coupon':all_dic['coupon']
                # }
                redis_course_coupon=all_dic
                print(type(json.dumps(redis_course_coupon)))
                ##对里面的数据进行处理，里面的内容成为字符串传过去,为了之后更好的取数据
                # redis_course_coupon=json.dumps(redis_course_coupon)
                conn.hmset(pay_course_coupon_list,redis_course_coupon)
                # ##存入全局的优惠卷
                redis_global_course_coupon={
                    'global_coupon':all_dic['global_coupon']
                }
                redis_global_course_coupon['global_coupon']=json.dumps(redis_global_course_coupon['global_coupon'])
                conn.hmset(golbal_pay_coupon_list,redis_global_course_coupon)#注明，在存入redis里面之前序列化一下，更好的操作数据,mset是只能后面是字典，或者是列表的形式 ，不能是字符串的形式
                print(conn.keys())
                # print(conn.hgetall(golbal_pay_coupon_list))
                # print(conn.hgetall(pay_course_coupon_list))
                all_dic.update(add_dic)
                print(all_dic)
                all_pay_course_ment.append(all_dic)
        ##做处理，拿到全部加入结算中的课程
            self.res.code = 200
            self.res.error=None
            self.res.msg='已经拿到%s用户购物车内容'%username
            self.res.all_data=all_pay_course_ment
            # self.res.all_data = all_pay_course_ment
            # print(all_pay_course_ment)
            return Response(self.res.get_response)
        except  Exception  as e:
            print(e)
            self.res.code=400
            self.res.msg=None
            self.res.all_data=None
            self.res.error='查看购物车信息失败'
            return   Response(self.res.get_response)


        ##局部更新,判断是全局优惠卷还是局部优惠卷，（每一次只能修改一次优惠卷，注意，缺陷）
    def  patch(self,request,*args,**kwargs):
        try:
            res=Self_Response()
            print(request.data)
            course_id_list=request.data.get('course_id')
            coupon_id=request.data.get('coupon_id')
            print(course_id_list)

            user_id=request.auth.username.id
            global_pay_coupon_key=golbal_pay_course_coupon%request.auth.username.id
            #当是全局的优惠卷的时候
            if   not  course_id_list:##根据这个是否有这个id来看
                '''更具默认的优惠卷来取'''
                ##判断全局的优惠卷是否为空default_golbal_coupon
                if    coupon_id==0:##没有使用全局的优惠卷，和if  not  coupon_id一样，都是没有使用的情况
                    gol_coupon = conn.hset(global_pay_coupon_key, 'default_golbal_coupon', coupon_id)
                    res.msg='修改全局优惠卷成功'
                    return  Response(res.get_response)
                res.msg='选择全局优惠卷%s'%coupon_id
                gol_coupon = conn.hset(global_pay_coupon_key, 'default_golbal_coupon', coupon_id)
                ##去redsi里面拿到这个全局的id数据
                global_coupon=conn.hget(global_pay_coupon_key,'global_coupon')
                # global_coupon_dic=json.loads(str(global_coupon, encoding='utf-8'))
                global_coupon_dic=str(global_coupon, encoding='utf-8')

                if    coupon_id   not   in  global_coupon_dic:
                    return  Response("不存在此全局优惠卷")
                gol_coupon=conn.hset(global_pay_coupon_key,'default_golbal_coupon',coupon_id)
                return   Response('修改全局优惠卷成功')

            #下面是局部优惠卷，判断是否是存在的
            else:
                if   coupon_id   not   in   coupon_id:
                    return  Response('局部优惠卷不存在')
                else:
                    name=models.Course.objects.filter(id=coupon_id).values('course_name')[0]['course_name']
                    # 在raw里面进行的提交数据操作            ##当是局部的优惠卷的时候
                    course_pay_coupon_key = all_pay_courses_coupon % (request.auth.username.pk, course_id_list)
                    print(name)
                    conn.hset(course_pay_coupon_key,name,coupon_id)
                    all_data=conn.hgetall(course_pay_coupon_key)
                    print(conn.hset('pay_course_coupon_2_1', 'course_coupon', coupon_id))
                    self.res.code=200
                    self.res.error=None
                    self.res.msg='局部优惠卷修改成功'
                    print(conn.hset('pay_course_coupon_2_1', 'course_coupon', 1))
                    return   Response(self.res.get_response)
        except  Exception  as  e:
            print(e)




##讲解一下：
    def  get(self,requets,*args,**kwargs):
        print(requets.data)
        ##拿到所有的结算数据
        all_course_data=all_pay_courses_coupon%(requets.auth.username.pk,'*')##可以迭代拿出所有的匹配相关的数据出来，可以限制数量（scan_iter）
        # all_course_keys=conn.keys(all_course_data)##最好不要直接这样取数据

        course_coupons=[]
        for  val  in   conn.scan_iter(all_course_data):
            course_dic={}
            data=conn.hgetall(val)
            print(data)
            for   k,v   in   data.items():

                '''如果字典外面是字节的话，就转换成字节的形式，如果是反序列化的话，就进行序列化操作，不用管字典里面是什么，直接进行相对应的操作'''
                if   k.decode('utf-8')=='course_coupon':
                    course_dic['default_course_coupon']=conn.hget(val,'course_coupon').decode('utf-8')
                else:
                    course_dic[k.decode('utf-8')]=v.decode('utf-8')
            course_coupons.append(course_dic)
      ##注明一下，这个键就是转化为字符串，值就是序列化一下，如果是字典的话，就序列化一下，如果是字节的话，就得转化为字符串
        # print(course_coupons)

            ##对全局的优惠卷进行处理##,不用管字典里面的的是什么，字典外码是字节就用字节的方，是序列化的，就进行反序列化

        global_course_coupon=golbal_pay_course_coupon%requets.auth.username.id
        val=conn.hgetall(global_course_coupon)
        global_course_coupon_dic={}
        # print(val)
        for   k,v   in  val.items():
            # print(k.decode('utf-8'))
            # print(json.loads(v.decode('utf-8')))
            if  k.decode("utf-8")=='default_golbal_coupon':
                global_course_coupon_dic['default_golbal_coupon']=v.decode('utf-8')
            else:
                global_course_coupon_dic[k.decode('utf-8')]=json.loads(v.decode('utf-8'))
        # print(global_course_coupon_dic)
        all_data={
            'global_course_coupon_dic':global_course_coupon_dic,
            'course_coupons_dict':course_coupons
        }

        res=Self_Response()
        res.code=200
        res.msg='查看用户【%s】全部的结算信息'%requets.user
        res.all_data=all_data##这个返回的是可以为字典的
        return   Response(res.get_response)







'''
{b'img': b'julia.png',
b'pricepolicy_list': b'{"1": {"price": 21214.0, 
"expire_time": "\\u4e24\\u4e2a\\u6708\\u65f6\\u95f4",
"course_perid": "1\\u4e2a\\u6708\\u65f6\\u95f4", "diff_level": "\\u4e00\\u822c",
"course_level": "vip\\u8bfe\\u7a0b"}, 
b'name': b'linux',
b'default': b'1'}
'''


