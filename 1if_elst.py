# 随机输入三个数打印三个数按升序输出

# input 3 num
num1, num2, num3 = input('Enter 3 num: ').split()

# convert the num
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
# judge the num format print
if num1 > num2:
    if num2 > num3:
        print("{} > {} > {}".format(num1,num2,num3))
    else:
        if num1 > num3:
            print("{} > {} > {}".format(num1, num3, num2))
        elif  num2 == num3:
            print("{} > {} = {}".format(num1, num3, num2))
        else:
            print("{} > {} > {}".format(num3, num1, num2))
if num1 < num2:
    if num2 < num3:
        print("{} > {} > {}".format(num3, num2, num1))
    else:
        if num2 == num3:
            print("{} = {} > {}".format(num2, num3, num1))
        elif num3 > num1:
            print("{} > {} > {}".format(num2, num3, num1))
        else:
            print("{} > {} > {}".format(num2, num1, num3))
if num1 == num2:
    if num1 < num3:
        print("{} > {} = {}".format(num3, num1, num2))
    elif num1 == num3:
        print("{} = {} = {}".format(num1, num2, num3))
    else:
        print("{} = {} > {}".format(num1, num2, num3))



