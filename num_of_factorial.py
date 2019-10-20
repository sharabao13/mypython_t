#求一个数的阶乘
a = input("请输入一个数： ")
a = int (a)
jc = 1
for num in range(a,0,-1):
    jc *= num
print(jc)
