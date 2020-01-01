# 列表
randList = ["string", 1.234, 28]

first3 = randList[0:3]
print(first3)

# 判断元素是否在列表里面 'in'
print("string" in first3)

# 判断 元素在列表第几个索引 '.index('元素')'

print("string元素在列表的第几个索引： ", first3.index("string"))

# 扩展
for i in first3:
    print('{} 元素对应的索引是： {}'.format(i,first3.index(i)))

# 计算元素在列表的个数 '.count('元素')'
for i in first3:
    print('{} 元素在列表的个数： {}'.format(i,first3.count(i)))

# 列表的元素增加 '.append('元素')'
first3.append('string')
print(first3)
for i in first3:
    print('{} 元素对应的索引是： {}'.format(i,first3.index(i)))
for i in first3:
    print('{} 元素在列表的个数： {}'.format(i,first3.count(i)))

# 列表的更改
first3[3] = "Another"
print(first3)

# random 模块
# random.randrange(begin,end) 产生随机数
import random
rand_num = random.randrange(1,50)
print(rand_num)

# 冒泡排序

