#打印1=100的素数
print(1)
print(2)
for i in range(3,100,2):
    for j in range(2,i):
        if (i % j) < 1:
            break
    else:
         print(i)