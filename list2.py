# 冒泡排序

# import random
# numList = []
# M = 10
#
# for i in range(M):
#     numList.append(random.randrange(1,50))
# print(numList)
#
# i = len(numList) - 1
# print(i)
# while i > 0:
#     j = 0
#     while j < i:
#         if numList[j] > numList[j+1]:
#             numList[j], numList[j+1] = numList[j+1], numList[j]
#         j += 1
#     for k in numList:
#         print(k, end=", ")
#     print()
#     i -= 1
#
# import random
# num_List = []
# M = 10
# for i in range(M):
#     num_List.append(random.randrange(1,50))
# print(num_List)
# print(type(num_List))
# print()
# i = len(num_List) - 1
# while i > 0:
#     j = 0
#     while j < i:
#         if num_List[j] > num_List[j+1]:
#             num_List[j], num_List[j+1] = num_List[j+1], num_List[j]
#         j += 1
#     for k in num_List:
#         print(k, end=", ")
#     print()
#     i -= 1

# 传入几个数字 进行排序
# numList = []
# num = input("Enter some num: ").split(" ")
# for i in range(1):
#     numList.append(num)
# numList.append(num)
# print(numList)

# i = len(numList) - 1
# while i > 0:
#     j = 0
#     while j < i:
#         if numList[j] > numList[j+1]:
#             numList[j], numList[j+1] = numList[j+1], numList[j]
#         j += 1
#     for k in numList:
#         print(k, end=", ")
#     print()
#     i -= 1

import random
numList = []
M = 5
for i in range(M):
    numList.append(random.randrange(1,30))
i = len(numList) - 1
print(numList)
# numList.sort()
# print(numList)
print()

while i > 0:
    j = 0
    while j < i:
        if numList[j] > numList[j+1]:
            numList[j], numList[j+1] = numList[j+1], numList[j]
        j += 1
    for k in numList:
        print(k, end=", ")
    print()
    i -= 1