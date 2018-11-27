#
#
#
# import  socket
# import selectors
# import  time
# #一直监听有没有客户进来
# class FTPconnect():
#     def __init__(self):
#         self.dic=[]
#         self.rel=selectors.DefaultSelector()
#         self.create_socket()
#         self.handler()
#     def create_socket(self):
#         self.sock=socket.socket()
#         self.sock.bind(('127.1.1.1',8080))
#         self.sock.listen(100)
#         self.sock.setblocking(False)
#         self.rel.register(self.sock, selectors.EVENT_READ, self.accept)
#         print('创建socket成功')
#
#     def handler(self):
#         while True:
#             try:
#         #     while True:
#                 print('开始监听有没有用户进来......')
#             # self.rel.register(self.sock,selectors.EVENT_READ,self.accept)
#                 events=self.rel.select()
#                 for key,mask in events:
#                     callback=key.data
#                     callback(key.fileobj)#开始执行accept函数了
#             except Exception as e:
#                 print(e)
#         #     callback
#
# #当有用户进来时，建立连接
#     def accept(self,sock):
#         try:
#             print('有新用户进来，开始建立链接了')
#             conn, addr = self.sock.accept()
#             print(conn)
#             # self.dic[conn] = {}
#             self.dic.append(conn)
#             # print(self.dic)
#             # print('与用户%s建立通信'%self.dic.index(conn))
#             self.sock.setblocking(False)
#             self.rel.register(conn, selectors.EVENT_READ, self.read)
#         except Exception as e:
#             print(e)
#
#
#
# #与用户进行通信循环
#     def read(self,conn):
#         try:
#             data = conn.recv(1024)
#             if data:
#             # self.dic.append(conn)
#                 print('与用户%s建立通信' % self.dic.index(conn))
#             # print('已经接收到%s的数据%s' %((self.dic.index(conn)),(data.decode('UTF-8'))))
#                 msg = input('输入:')
#                 conn.send(msg.encode('utf-8'))
#                 print('发送数据给%s'%self.dic.index(conn))
#             else:
#                 print('错误')
#         except Exception as e:
#             print(e)
#
#
# if __name__ == '__main__':
#     FTPconnect()

##################################每连接一个用户############################################
#############################多用户环节################################################




















#
# import  socket
# import selectors
# import  time
# #一直监听有没有客户进来
# class FTPconnect():
#     def __init__(self):
#         self.dic=[]
#         self.rel=selectors.DefaultSelector()
#         self.create_socket()
#         self.handler()
#     def create_socket(self):
#         self.sock=socket.socket()
#         self.sock.bind(('127.221.65.189',8080))
#         self.sock.listen(100)
#         self.sock.setblocking(False)
#         self.rel.register(self.sock, selectors.EVENT_READ, self.accept)
#         print('创建socket成功')
#
#     def handler(self):
#         while True:
#             try:
#         #     while True:
#                 print('开始监听有没有用户进来......')
#             # self.rel.register(self.sock,selectors.EVENT_READ,self.accept)
#                 events=self.rel.select()
#                 for key,mask in events:
#                     callback=key.data
#                     callback(key.fileobj)#开始执行accept函数了
#             except Exception as e:
#                 print(e)
#         #     callback
#
# #当有用户进来时，建立连接
#     def accept(self,sock):
#         try:
#             print('有新用户进来，开始建立链接了')
#             conn, addr = self.sock.accept()
#             print(conn)
#             # self.dic[conn] = {}
#             self.dic.append(conn)
#             # print(self.dic)
#             # print('与用户%s建立通信'%self.dic.index(conn))
#             self.sock.setblocking(False)
#             self.rel.register(conn, selectors.EVENT_READ, self.read)
#         except Exception as e:
#             print(e)
#
#
#
# #与用户进行通信循环
#     def read(self,conn):
#         try:
#             data = conn.recv(1024)
#             if data:
#             # self.dic.append(conn)
#                 print('与用户%s建立通信' % self.dic.index(conn))
#             # print('已经接收到%s的数据%s' %((self.dic.index(conn)),(data.decode('UTF-8'))))
#                 msg = input('输入:')
#                 conn.send(msg.encode('utf-8'))
#                 print('发送数据给%s'%self.dic.index(conn))
#             else:
#                 print('错误')
#         except Exception as e:
#             print(e)
#
#
# if __name__ == '__main__':
#     FTPconnect()





# ##########################################################这里有多个用户在此运行########################################################
#
#
# #########################################################多线程运行多个用户######################################################################
#
# ############从这个数据库里面去这个相对应的ip
# class multi_user:
#     def __init__(self):
#         print('#' * 200)
#         print('正打开这个多用户环节..............................')
#         # self.take_ip()
#         # self.QQ_IP_login()
#         print('已经进入此服务器的多用户环节............................................................')
#     ############################可以拿到这个上线的QQ和对应的ip地址
#
#
#     def take_ip(self):
#         f = open('login_QQ_ID.txt', 'r')
#         data= f.read()
#         f.close()
#         import demjson
#         data=demjson.decode(data)
#         print('这个已经上线的用户是:',data)
#         print(type(data))
#         all_QQ_IP=[]
#         for i in range(0, len(data)):
#             (key, value), = data[i].items()
#             ########################这里是对过来的用户进行ip匹配
#             print(value)
#             print(key)
#             if value in all_QQ_IP:
#                 print('已经存在此用户，不需要在存入')
#                 continue
#             else:
#                 print('不存在，写入进去')
#                 all_QQ_IP.append(value)
#             print('这个用户对应的ip地址是：',data[i])
#             # return  value
#
#         print('所有已经上线的QQ用户IP是：',all_QQ_IP)
#         print('，。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。')
#         for ip_addr in all_QQ_IP:
#             print('循环返回这个ip地址')
#             print(ip_addr)
#             # global  ip_addr
#             # return ip_addr
#
#
#         # fh = open('login_QQ_ID.txt', 'r')
#         # data = fh.read()
#         # fh.close()
#         # import demjson
#         # data = demjson.decode(data)
#         # (key, value), = data.items()
#         # print(value)
#         # print('这个对应的ip地址是')
#         # return  value
#
#
#
#     ###########################################进入相应的ip地址###########################################
#     def QQ_IP_login(self):
#         print('执行Myserver函数，请等待..................................')
#         Myserver()
#         # ip_addr=self.take_ip()
#         # print('这个取到的ip地址是:',ip_addr)
#         #################拿到相对应的ip地址
#
#
# #########################################每进来一个用户，就进行通信
#     def create_QQ_ID_thread(self):
#         print('开始监听用户进来，就开一个线程')
#         ####################################取已经登录的用户
#         ##############拿到所有已经上线的用户####################################################################################
# multi_user()
#
# ###############################################高并发写入用户进来，在这里进行通信
#
#
# # for i in range(0,)
#
#
#
# # all_QQ_IP=multi_user.take_ip('self')
# # print('拿到所有已经上线的QQ用户')
# # print(all_QQ_IP)
# # print(type(all_QQ_IP))
# # t1 = threading.Thread(target=music)
#
#
#
#
#
#
# f = open('login_QQ_ID.txt', 'r')
# data = f.read()
# f.close()
# import demjson
#
# data = demjson.decode(data)
# print('这个已经上线的用户是:', data)
# print(type(data))
# all_QQ_IP = []
# for i in range(0, len(data)):
#     (key, value), = data[i].items()
#     ########################这里是对过来的用户进行ip匹配
#     print(value)
#     print(key)
#     if value in all_QQ_IP:
#         print('已经存在此用户，不需要在存入')
#         continue
#     else:
#         print('不存在，写入进去')
#         all_QQ_IP.append(value)
#     print('这个用户对应的ip地址是：', data[i])
#
#
# print(all_QQ_IP)
#
#
#
#
#
#
#



#
#
#
#
# ###################################################开启多线程通信#####################################
############进行监听#############################################################################################

print('进入到多用户高并发环节......................................................')
import os,sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
##########################这个是当前的绝对路径
sys.path.append(PATH)
import json
print(PATH)

f = open('login_QQ_ID.txt', 'r')
data = f.read()
f.close()
import demjson

data = demjson.decode(data)
print('这个已经上线的用户是:', data)
all_QQ=[]
for i in range(0, len(data)):
    (key, value), = data[i].items()
    print('运行')
    print('........................................................')
    if value in all_QQ:
        print('已经存在此用户，不需要在存入')
        continue
    else:
        print('不存在，写入进去')
        all_QQ_dic={}
        all_QQ_dic[key]=value
        all_QQ.append(all_QQ_dic)
    print('这个用户对应的ip地址是：', data[i])


print(all_QQ)
print('全部的用户ip已经上线的QQ用户')




import  threading
import  time
import  socket
import selectors
import  time
#一直监听有没有客户进来
class FTPconnect():

    def __init__(self,QQ_ID,QQ_IP):
        self.QQ_ID=QQ_ID
        self.QQ_IP=QQ_IP
        print('开始时间是%s' % time.ctime())
        print('hello %s'%QQ_ID)
        self.dic=[]
        self.rel=selectors.DefaultSelector()
        self.create_socket()
        self.handler()
    def create_socket(self):
        self.sock=socket.socket()
        print('正在请求连接的用户是:',self.QQ_ID)
        print('这个正在请求连接的ip是',self.QQ_IP)
        self.sock.bind((self.QQ_IP,8080))
        self.sock.listen(100)
        self.sock.setblocking(False)
        self.rel.register(self.sock, selectors.EVENT_READ, self.accept)
        print('创建socket成功')

    def handler(self):
        while True:
            try:
        #     while True:
                print('开始监听有没有用户进来......')
                print('%s用户已经连接进来'%self.QQ_ID)
            # self.rel.register(self.sock,selectors.EVENT_READ,self.accept)
                events=self.rel.select()
                for key,mask in events:
                    callback=key.data
                    callback(key.fileobj)#开始执行accept函数了
            except Exception as e:
                print(e)
        #     callback

#当有用户进来时，建立连接
    def accept(self,sock):
        try:
            print('有新用户进来，开始建立链接了')
            conn, addr = self.sock.accept()
            print(conn)
            # self.dic[conn] = {}
            self.dic.append(conn)
            # print(self.dic)
            # print('与用户%s建立通信'%self.dic.index(conn))
            self.sock.setblocking(False)
            self.rel.register(conn, selectors.EVENT_READ, self.read)
        except Exception as e:
            print(e)

#与用户进行通信循环
    def read(self,conn):
        try:
            data = conn.recv(1024)
            if data:
            # self.dic.append(conn)
            #     print('与用户%s建立通信' % self.dic.index(conn))

                print ('与用户{}建立通信'.format(self.QQ_ID))
            # print('已经接收到%s的数据%s' %((self.dic.index(conn)),(data.decode('UTF-8'))))
                data=conn.recv(1024)
                print('接收到的数据是',data)
                msg = input('输入:')
                conn.send(msg.encode('utf-8'))
                print('发送数据给%s'%self.dic.index(conn))
            else:
                print('错误')
        except Exception as e:
            print(e)


# if __name__ == '__main__':
#     FTPconnect()



    # print('结束时间是%s'%time.ctime())
    # print(t2.isAlive())
thread=[]
t=[]
for i in range(0,len(all_QQ)):
    # (key,value),=all_QQ.items()
    (key,value),=all_QQ[i].items()
    print('这个当前用户ip是:',value)
    print('这个当前用户是:',key)
    # current_QQ_IP=
    # print(current_QQ_ID)
    # t1=threading.Thread(target=hi,args=(3,))
    i=threading.Thread(target=FTPconnect,args=(key,value,))
    thread.append(i)
for j in thread:
    j.start()
print('ending................。。。。')


