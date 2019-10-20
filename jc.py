#1-5 阶乘之和

jc = 1
count = 0
for i in range(1,6):
    jc *= i
    count += jc
print (count)