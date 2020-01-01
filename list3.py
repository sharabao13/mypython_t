# 冒泡排序

# 定义一个空列表 存放冒泡排序列表值
numList = []
# 产生10 个元素 元素的值在1-100之间 存放在numlist 中
import random
M = 10
for i in range(M):
    numList.append(random.randrange(1, 100))
# 打印该列表的初始值
print(numList)
# 将列表值进行两两比较
# 定义一个循环的初始值
i = len(numList) - 1
# 进入循环 定义一个内层循环的初始值
while i > 0:
    # 比较列表相邻两个索引大小 进行对换
    j = 0
    while j < i:
        if numList[j] > numList[j+1]:
            numList[j], numList[j+1] = numList[j+1], numList[j]
        # 内层循环控制变量 +1
        j += 1
    # 外出循环控制变量 - 1
    # 打印列表的排序
    for k in numList:
        print(k, end=" ")
    print()
    i -= 1
