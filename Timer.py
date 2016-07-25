#just a timer

import time

number = 10

print("first is the timer")
for x in range (1,(number+1)):
    print(x)
    time.sleep(1)

#count down

print("now is a countdown")
for i in range(1, (number+1)):
    print(10-i)
    time.sleep(1)