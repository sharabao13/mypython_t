# 字符串常用函数操作
rand_string = "  life is a beautiful struggle  "
struggle = "welcome to python"
print(rand_string)
# .lstrip 左边剥离
print(rand_string.lstrip())
# .rstrip 右剥离
print(rand_string.rstrip())
# .strip 两边剥离
print(rand_string.strip())
print()
# capitalize  首字母大写 其他小写
print(struggle.capitalize())

# upper 全部大写
print(rand_string.upper())
# lower  全部小写
print(rand_string.lower())

# .join 将列表的元素相连 形成一个新的的字符串  " " 为将字符串相连的中间连接符 为空格 "," 中间连接符为逗号
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))
print(",".join(a_list))

# count 统计某个元素出现的次数
print(rand_string.count("if"))
# find 检查字符串中是否包含字符串，如果知道begin 和 end 则检查字符串是否在指定范围内 包含返回起始位，不包含返回 -1
print(rand_string.find("is", 2, 7))
# replace 替换字符串
print(rand_string.replace("struggle", "journey"))


#  其他常用函数
letter_z = "Z"
num_3 = "3"
a_sapce = " "
# isalnum  检查字符串是否为字母+数字组成的  返回boolen
print(letter_z.isalnum())
print(num_3.isalnum())
print(a_sapce.isalnum())
print()
# isalpha  检查字符串是否为 字母组成
print(letter_z.isalpha())
print(num_3.isalpha())
print(a_sapce.isalpha())
print()
# isdigit  检查字符串是否为 数字组成
print(letter_z.isdigit())
print(num_3.isdigit())
print(a_sapce.isdigit())
print()
# islower  检查字符串是否为小写
print(letter_z.islower())
print(num_3.islower())
print(a_sapce.islower())
print()
# isupper 检查字符串是否为大写
print(letter_z.isupper())
print(num_3.isupper())
print(a_sapce.isupper())
print()
# isspace 检查字符串是否为空格组成
print(letter_z.isspace())
print(num_3.isspace())
print(a_sapce.isspace())