#求一个数的阶乘 3！ 3*2*1

num = input ("请输入一个数：")
num = int (num)
jc = 1
count = 0
for i in range (1,num+1):
    for j in range (1,i+1):
        jc *= j
    count += jc
    jc = 1
print (count)

