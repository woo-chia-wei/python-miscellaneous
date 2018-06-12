import time
import datetime
from random import randint

randint(100, 999)
numbers = [randint(10 ** 10, 10 ** 11 - 1) for i in range(10)]

def huge_computation(x):
    time.sleep(1)
    return x

def trace(msg):
    print(datetime.datetime.now(), msg)

# Without generator, use list instead
trace('Start with list')
for x in [huge_computation(n) for n in numbers]:
    trace(x)
trace('End with list')

# Use generator
trace('Start with generator')
for x in (huge_computation(n) for n in numbers):
    trace(x)
trace('End with generator')