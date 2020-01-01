# 奇数函数
def odd_num(num):
    for i in range(1,num):
        if (num % 2) == 0:
            return False
    return True
num1 = int(input("Enter a num: "))
print("This num is a oddnum: ", odd_num(num1))
