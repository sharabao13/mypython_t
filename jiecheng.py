#求1-100的中间数的阶乘
jc = 1
num = int(input("请输入一个1-100之间的数: \n"))
for i in range(1,num+1):
    jc *= i
    count = jc
print(count)