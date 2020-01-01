# 函数练习
# 传入 字母 数字 空格 其他 计算个数
def num1(num):
    al_sum = 0
    space_sum = 0
    dig_sum = 0
    other_sum = 0
    for i in num:
        if i.isdigit() == True:
            dig_sum += 1
        elif i.isspace() == True:
            space_sum += 1
        elif i.isalpha() == True:
            al_sum += 1
        else:
            other_sum += 1
    return (dig_sum, space_sum, al_sum, other_sum)
r = num1("43dfe.454fdafds  fds **")
print(r)