# import  threading
# import time
# def music():
#     print('music开始时间是%s'%time.ctime())
#     time.sleep(3)
#     print('music结束时间是%s'%time.ctime())
#
# def game():
#     print('game开始时间是%s'%time.ctime())
#     time.sleep(5)
#     print('game结束时间是%s'%time.ctime())
#
#
#
# t1=threading.Thread(target=music)
#
# t2=threading.Thread(target=game)
# t1.start()
# t2.start()
#
# t1.join()
# # t2.join()
#
# print('endding')
#
#
#
# import  threading
# import  time
# def hi(num):
#     print('开始时间是%s'%time.ctime())
#     print('hello %d'%num)
#     time.sleep(num)
#     print('结束时间是%s'%time.ctime())
#
#
#
#
# t1=threading.Thread(target=hi,args=(3,))
# # t1.start()
# t2=threading.Thread(target=hi,args=(5,))
# t1.start()
# t2.start()
# t1.join()#等待t1执行完后打印endding
# t2.join()#等待t2执行完后打印endding\
# #总共耗时5秒钟
# print('endding')




#
# #
# import  threading
# import  time
# def hi(num):
#     print(t.getName())
#     print('开始时间是%s'%time.ctime())
#     print('hello %d'%num)
#     time.sleep(num)
#     print('结束时间是%s'%time.ctime())
#     print(t2.isAlive())
# thread=[]
#
# t1=threading.Thread(target=hi,args=(3,))
#
# t2=threading.Thread(target=hi,args=(5,))
#
#
# thread.append(t1)
# thread.append(t2)#把t1，t2放进列表thread里面
# # t1.setDaemon(t1)
# t1.setDaemon(True)#当t1结束时，主线程也结束了，t2是守护主线程的，当主线程结束时，t2也跟着结束
# # print('t2进程是否结束',t2.isAlive())
# for t in thread:
#     t.start()#所有线程都开启了
#     # print(t.setName('Thread-1'))
#
#
# print('all over')
# print(t2.isAlive())#判断t2线程是否活动



# import  threading
# import time
#
# class Mythread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#
#     def run(self):
#         # print(Mythread.getName(self))#得到子线程的名字,调用函数里面的方法，传实例self进去
#         # print(self.getName())#当那个实例运行时就打印出那个线程在运行
#         print('running 的是:%s'%self.num)
#
#         time.sleep(2)
#         print('当前时间是%s'%time.ctime())#过两秒后同时结束
# t1=Mythread(1)
# t2=Mythread(2)
# t1.setDaemon(True)
# t1.start()
# t2.start()
#
# print('endding ........')





#同步锁
def add():
    sum=1

# import time
# def mul():
#     global  num
#     lock.acquire()#只能有一个线程,只支持一个cpu进行一个线程
#     num-=1
#     time.sleep(0.000001)
#     lock.release()
#
# num=100
# import threading
# l=[]
# lock=threading.Lock()#拿到所
# for i in range(100):
#     t=threading.Thread(target=mul)#给100个线程
#     t.start()
#     # print(num)

# print(num)







# import  threading
# import  time
# class Mythread(threading.Thread):
#     def actionA(self):
#         r_lock.acquire()
#         print(self.getName(),'得到A',time.ctime())
#         time.sleep(2)
#
#         r_lock.acquire()#又加了一把B锁
#         print(self.getName(),'得到B',time.ctime())
#         time.sleep(1)
#         r_lock.release()
#         print('已经释放B锁',self.name)
#         r_lock.release()
#         print('已经释放A锁', self.name)
#     def actionB(self):
#         r_lock.acquire()
#         print(self.getName(),'得到B',time.ctime())#产生死锁的原因，第一个线程先进来，得到A锁，等待2秒后拿到B锁，等待1秒后B锁钥匙释放，紧接着A锁钥匙释放，然后线程11执行actionB，另一个线程2进来了，执行actionA
#         #线程1执行actiomB的时候拿到了B锁钥匙，还没有释放，线程2执行actionA的时候拿到了A锁钥匙也还没有释放，所以卡住了，产生了死锁，其他线程也进不来，一个锁对应一把钥匙,只能一个线程在执行
#         time.sleep(2)
#
#         r_lock.acquire()#又加了一把B锁
#         print(self.getName(),'得到A',time.ctime())
#         time.sleep(1)
#         r_lock.release()
#         print('已经释放A锁',self.name)
#         r_lock.release()
#         print('已经释放B锁', self.name)
#     def run(self):
#         self.actionA()
#         # time.sleep(2)
#         self.actionB()
#
# r_lock=threading.RLock()
# A=threading.Lock()
# B=threading.Lock()#创建两把锁
# L=[]
# for i in range(5):
#   t=Mythread()#5个线程
#   t.start()
#   L.append(t)
#
#
# for i in L:
#     i.join()
#
#
# print('ending')




#
# import threading
# import  time
# class Boss(threading.Thread):
#     def run(self):
#         print('BOSS：今天晚上10点下班')
#         print(event.is_set())
#         event.set()
#         time.sleep(3)
#         print('BOSS:可以下班了')
#         print(event.is_set())#查看event是否被设定
#         event.set()#event被设定
#
#
# class workers(threading.Thread):
#     def run(self):
#         event.wait()#等待被设定的event，被动状态，只能等待
#         print('workers：命苦呀')#做出回应
#         time.sleep(1)
#         # event.clear()#清空之前被设定的event
#         event.wait()
#         print('workers：哦豁yeah！！！！')
#
#
#
# event=threading.Event()
#
# L=[]
#
# for i in range(5):
#     L.append(workers())
#
# L.append(Boss())
#
# for j in L:
#     j.start()
#
#
# for i in L:
#     i.join()
#
#
# print('endding')







# import threading
# import time
#
#
# class mythread(threading.Thread):
#     def run(self):
#         if semaphone.acquire():
#             print(self.name)
#             time.sleep(2)  # 没隔2秒出来5个
#             semaphone.release()
#
#
# semaphone = threading.Semaphore(5)  # 开了一把锁，每次放5个线程进去
#
# thrs = []  # 写了一个列表
#
# for i in range(100):
#     thrs.append(mythread())  # 开了100个线程
#
# for i in thrs:
#     i.start()
#
# for i in thrs:
#     i.join()
#
# print('endding')




# import  queue#FIFO
#
# q=queue.Queue(3)
#
# q.put(12)
# q.put('name','alex')
# q.put('fasf')
# # q.put('sfasf',block=False)#队列满了
#
#
# while 1:
#     p=q.get()#先进先出
#     print(p)import  queue#FIFO
#

#先进后出
# import  queue#
# # q=queue.LifoQueue(3)#先进后出
#
# q=queue.PriorityQueue(3)#优先级来输出
# q.put([2,12])
# q.put([1,'name','alex'])
# q.put([5,'fasf'])
# # q.put('sfasf',block=False)#队列满了
#
#
# print(q.empty())#如果队列为空，返回True
# print(q.full())#如果队列满了，返回True
# print(q.qsize())#返回队列的大小
#
# while 1:
#     p=q.get()#先进先出
#     print(p)
# #
# #
#

# li=[1,2,3,4,5,5]
# print(li[-1])
# a=li[-1]
# li.remove(a)
# print(li)
# def pri():
#     while 1:
#         a=li[-1]
#         print(a)
#         li.remove(a)
#
# # pri()
#
#
#
# import  threading
#
# # t1=threading.Thread(target=pri(),args=())
# t2=threading.Thread(target=pri(),args=())
# # t1.start()
# t2.start()
# print(li)








#
# import  time
# from multiprocessing import Process
#
# class Myproess(Process):
#     def __init__(self,num):
#         super(Myproess,self).__init__()
#         self.num=num
#     def run(self):
#         time.sleep(1)
#         print(self.pid)
#         print(self.is_alive())
#         print(self.num)
# # p_list=[]
# if __name__ == '__main__':
#     p_list = []
#     for i in range(10):
#         p=Myproess(i)
#     # p=Process(target=foo,args=(i,))#,开了10个进程，传10个参数，从0到9
#         p_list.append(p)
#
#     for i in p_list:
#         i.start()
#
#     print('endding')





# import  queue
#
# from  multiprocessing import  Process,Pipe
#
# def f(conn):
#     conn.send('nihao')
#     response=conn.recv()
#     print('response',response)
#     print(id(conn))
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn,child_conn=Pipe()#双向管道
#     p=Process(target=f,args=(child_conn,))#向f函数传一个参数child_conn
#     p.start()
#     print(parent_conn.recv())
#     parent_conn.send('hello')
#     print(id(parent_conn))
#     p.join()
#
#     print('endding')






#
# from multiprocessing import  Process,Manager
# def f(d,l,n):
#     d[n]='1'#d是字典,n是进来的进程，n会改变
#     d['2']=2
#     # d['0.12']=None
#     l.append(n)#在l列表中添加n
#
#
#
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d=manager.dict()#定义一个字典
#         l=manager.list(range(5))#l是一个列表
#         p_list=[]
#
#         for i in range(10):
#             p=Process(target=f,args=(d,l,i))
#             p.start()
#             p_list.append(p)
#
#         for res in p_list:
#             res.join()
#
#         print(d)
#         print(l)




# from multiprocessing import  Process,Lock
# import time
#
#
# def f(l,i):
#     # with l:
#     #     print('hello %s'%i)
#     # l.acquire()#2种方式
#     print('hello %s'%i)
#     time.sleep(1)
#     # l.release()
# #同步锁
# if __name__ == '__main__':
#     Lock=Lock()
#     for i in range(10):
#         t=Process(target=f,args=(Lock,i))
#         t.start()


#
# import  time,os
# from multiprocessing import  Process,Pool
#
#
# #子进程的
# def foo(i):
#     print(i)
#     time.sleep(2)
#     return  i
#
# #主进程的
# def Bar(num):
#     # pass
#     print(os.getpid())
#     print(num)
# if __name__ == '__main__':
#     pool=Pool(5)
#     for i in range(100):
#         # pool.apply(func=foo,args=(i,))#同步，一个进程一个进程的走
#      #某个动作后某个函数执行成功后，在执行的函数
#         pool.apply_async(func=foo,args=(i,),callback=Bar)#异步,几个进程进程的走
#     pool.close()
#     pool.join()
#     print('endding')





# def f():
#     print('ok')
#     s=yield 3#相当于send的值给了s，然后在打印s出来
#     print(s)
#     print('ok1')
#     yield
#     print('ok2')
#     yield 3
#
#
# gen=f()
#
# print(gen.__next__())#print会返回一个值
# gen.send(7)#send会继续往下走
# print(gen.__next__())
# gen.send(7)
# next(gen)










