# 列表其他函数
numList = []
import random
for i in range(5):
    numList.append(random.randrange(1, 9))
print(numList)
# .sort() 列表元素从大到小排序
numList.sort()
print(numList)

# .sort(reverse = True) 列表元素从小到大
# numList.sort(reverse=True)
# print(numList)

# 内置函数sorted 对当前列表进行排序可重新赋值，不改变列表本身
print(sorted(numList))
print(numList)


# .reverse() 列表元素取反
# numList.reverse()
# print(numList)

# .insert() 插入元素 .insert(索引位置，元素值)
numList.insert(4,"str")
print(numList)

# .remove 删除元素 .remove(元素值)
numList.remove("str")
print(numList)

# .pop 删除索引位置的元素 .pop(索引位置)
numList.pop(0)
print(numList)

# 列表产生
# 手工输入
num_List = [1, 2, 3]
# 随意肌数产生列表
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))

# for i in 产生列表
nList = [i*2 for i in range(10)]
print(nList)

# 平方的内置函数pow()  pow(元素，平方)
numList = [1, 2, 3, 4]
print(numList)
pList = [pow(i, 2) for i in numList]
print(pList)

# 二维列表
dList = [[pow(i,2), pow(i,3), pow(i,4)] for i in numList]
print(dList)
for k in dList:
    print(k)
