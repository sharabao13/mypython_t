#随机数练习

import random

#print(random.randint(0,100))
#print(random.choice([2,3,4,[3,5]]))
#print(random.choice("tae"))
#print("输出100-1000的随机偶数: ",random.randrange(100,1000,2))
#print ("randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3))

list1=[2,3,5,'apple',[2,4,9],22]
random.shuffle(list1)
print(list1)