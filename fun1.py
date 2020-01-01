# 函数
# 邮箱函数
# def allotEmail(firstName, surname):
#     return firstName+'.'+surname+'@tae.com'
#
# name = input("Enter you name: ")
# fName,sName = name.split()
# compEmail = allotEmail(fName, sName)
# print("you company email: \n",compEmail)


# + - * / 函数

def operator_fun(num1, num2):
    return (num1 + num2), (num1 - num2), (num1 * num2), (num1 / num2)
num_list = input("Enter two number: ").split()
for i in num_list:
    fir_num = int(num_list[0])
    sec_num = int(num_list[1])
# print(fir_num)
# print(sec_num)
# print(type(sec_num))
sum, differ, multi, devid = operator_fun(fir_num, sec_num)
print(sum)
print(differ)
print(multi)
print(devid)