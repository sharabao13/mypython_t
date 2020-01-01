#汇率转换  美元转换人民币
#  汇率7

#用户输入一个美元数字
dollor=input("Enter dollor: ")

#转换美元的数据类型 ,将字符串转换为整形 convert str to intger
dollor=int(dollor)

#计算美元的汇率
CNY=dollor*7

#格式化输出
print('{} dollor equals  {} yuan'.format(dollor,CNY))