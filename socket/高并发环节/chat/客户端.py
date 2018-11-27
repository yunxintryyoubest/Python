# import socket
#
# sk=socket.socket()
# sk.connect(('127.1.1.1',8080))
# while True:
#     msg=input('输入：')
#     sk.send(msg.encode('utf-8'))
#     print('已经发送')
#     data=sk.recv(1024)
#     print(data.decode('utf-8'))








# import socket
#
# sk=socket.socket()
# sk.connect(('127.1.1.1',8080))
# while True:
#     try:
#         msg=input('输入：')
#         sk.send(msg.encode('utf-8'))
#         print('已经发送')
#         data=sk.recv(1024)
#         print('接收到服务端的数据是:',data.decode('utf-8'))
#
#
#     except Exception as e:
#         print(e)

#10个人吃包子

# import queue
# import  time,random
# import  threading
# q=queue.Queue()
#
# def producess(name):
#     count=1
#     while count<1000:
#         print('%s开始>>>making....'%name)
#         time.sleep(1)
#         q.put('%s号包子'%count)
#         print('%s放了%s号包子进去'%(name,count))
#         count+=1
#         # q.join()
#         print('OK')
# def customer(name):
#     count=1
#     while count<1000:
#         time.sleep(random.randrange(1))
#         data=q.get()#取得是哪个包子
#         print('eatting..................')
#         time.sleep(2)
#         # name=name+'号消费者'
#         # q.task_done()
#         print('%s吃了%s包子'%(name,data))
#         count+=1
# t1=threading.Thread(target=producess,args=('prod',))
#
# # t2=threading.Thread(target=customer,args=('cus',))
# # t3=threading.Thread(target=customer,args=('cs',))
#
# for i in  range(10):
#     t=threading.Thread(target=customer,args=(i,))
#     t.start()
# t1.start()
# # t2.start()
# # t3.start()



#10个人搬砖



# import  time
# from multiprocessing import Pool,Process
# import  threading
# num=0
# def carry(i):
#     global  num
#     while num<100:
#         num+=1
#         print('线程%s  结果%s'%(i,num))
#         # time.sleep(2)
# # carry()
# if __name__ == '__main__':
#
#     pool=Pool()
#     for i in  range(10):
#         # pool.apply_async(fu)
#         pool.apply_async(func=carry,args=(i,))#进程是独立的空间，所以是同时在运行
#         # pool.apply_async(func=carry)
#     pool.close()
#     pool.join()
    # p_list=[]
    # for i in range(100):
    #     rel=threading.Thread(target=carry,args=(i,))
    #     p_list.append(rel)
    #     rel.start()
    #
    # for j in p_list:
    #     j.join()
    # print('endding.........')



########################################每那应该用户就创建一个线程##################################################
# import socket
#
# sk=socket.socket()
# sk.connect(('127.221.65.189',8080))
# while True:
#     msg=input('输入：')
#     sk.send(msg.encode('utf-8'))
#     print('已经发送')
#     data=sk.recv(1024)
#     print(data.decode('utf-8'))



QQ_IP=input('请输入ip:')


class normal_user_main:
    try:
        def __init__(self):
            print('欢迎进入消息页面')
            # print('QQ用户【{}】已经上线..................................'.format(QQ_ID))
            self.start()
        def start(self):
            try:
                client_main_menus = '''
                           1,选择已经发送消息的好友
                           2,搜索（个人，群，公众号等anything）
                            '''
                # msg = input('输入：')
                print(client_main_menus)
                client_main_choice = input('请输入你的选择（1-2）:').strip()
                import socket
                sk = socket.socket()
                self.sk = sk
                sk.connect((QQ_IP, 8080))
                while True:
                    print('开始运行客户端了')
                    msg = input('输入:').strip()
                    # tcp_client.sendto(client_main_choice.encode('utf-8'), ip_port)
                    print('已经发送消息给服务端了')
                    sk.send(client_main_choice.encode('utf-8'))
                    print('已经发送')
                    data = sk.recv(1024)
                    print(data.decode('utf-8'))

            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

normal_user_main()






