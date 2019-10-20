###判断一个数是否是质数

num = input("请输入一个数：")
num = int (num)
for i in range(2,num-1):
    if num % i == 0:
        print ("不是质数")
        break
else:
    print ("是质数")