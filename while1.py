# 1-100 的奇数和

# 初始变量
num = 0
odd = 0
# while 循环
while num < 100:
     num += 1
     if num % 2 == 0:
         continue
     odd += num
# 格式化输出1-100 的奇数和
print('1-100的奇数和是: ',odd)