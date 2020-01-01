
import datetime
start = datetime.datetime.now()
for x in range(2,10000):
    for i in range(2,int(x ** 0.5)+1):
        if (x % i) == 0:
            break
    else:
        print(x)
worktime = datetime.datetime.now() - start
print(worktime)