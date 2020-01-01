#随机数
import random
i = 1
a = random.randint(0,5)
b = int( input('请输入0-100的数字\n然后查看是否与电脑一样: '))
while a != b:
    if a > b:
        print("你第%d次输入的数字小于电脑的随机数"%i)
        b = int(input("请再次输入数字： "))
    else:
        print("你第%d次输入的数字大于电脑的随机数" %i)
        b = int(input("请再次输入数字： "))
    i+=1
else:
    print("恭喜你，你第%d次输入的数字与电脑的随机数一样"%(i,b))