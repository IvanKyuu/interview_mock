import threading
x = 0
def increment():
    global x
    x += 1
def threadTask():
    for _ in range(50000):
        increment()
