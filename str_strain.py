#  提取每个字符串首字母 简写练习 练习
#  least recently userd = LRU
#  monthly active users =  MAU
#  daliy active users = DAU
#  Routing Information Protocol = RIP

# ask user input string 让用户输入需转换的字符串
str =  input("Please input the str: ")
# covert str to upper 将字符串转换大写
str = str.upper()
#  抽取整个字符串为单个字符串 存放在列表
listofstr = str.split()
# 遍历列表取首个字母
for word in listofstr:
    # 打印首个字符
    print(word[0], end='')