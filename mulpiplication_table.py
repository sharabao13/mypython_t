#打印99乘法表
#1*1=1

for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
