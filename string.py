# 字符串处理

# 字符串索引取值

samb_string = "Welcome to Python"
#  取第一个索引
print(samb_string[0])
# 取最后一个索引
print(samb_string[-1])

# 截取Welcome
print(samb_string[:7])

# 取 Welcome 后面的字符串
print(samb_string[8:])

# 截取 come to 前包后不包原则
print(samb_string[3:11])

url = "http://youtube.com"
# 截取url 协议部分
print(url[:5])
# 截取主机名部分
print(url[7:-4])
# 截取顶级域名
print(url[-4:])

# 遍历字符串内容
for i in samb_string:
    print(i)

# 字符串 运算
for i in range(0,len(samb_string)-1,2):
    print(samb_string[i] + samb_string[i+1])