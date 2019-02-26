import threading, time


loop1_index = 1
loop2_index = 2
loop3_index = 3
loop4_index = 4
loop5_index = 5

def information(n):
    print('thread %s is running...' % threading.current_thread().name)
    print('thread %s >>> %s' % (threading.current_thread().name, n))
    time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

def loop1():
    global loop1_index
    while loop1_index < 100:
        information(loop1_index)
        loop1_index = loop1_index + 5

def loop2():
    global loop2_index
    while loop2_index < 100:
        information(loop2_index)
        loop2_index = loop2_index + 5

def loop3():
    global loop3_index
    while loop3_index < 100:
        information(loop3_index)
        loop3_index = loop3_index + 5

def loop4():
    global loop4_index
    while loop4_index < 100:
        information(loop4_index)
        loop4_index = loop4_index + 5

def loop5():
    global loop5_index
    while loop5_index < 100:
        information(loop5_index)
        loop5_index = loop5_index + 5

print('thread %s is running...' % threading.current_thread().name)
t1 = threading.Thread(target=loop1, name='LoopThread1')

t2 = threading.Thread(target=loop2, name='LoopThread2')

t3 = threading.Thread(target=loop3, name='LoopThread3')

t4 = threading.Thread(target=loop4, name='LoopThread4')

t5 = threading.Thread(target=loop5, name='LoopThread5')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print('thread %s ended' % threading.current_thread().name)