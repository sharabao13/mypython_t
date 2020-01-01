t = (2,4,6,3,4,2)
#print(t)
#print(type(t))
t1 = tuple(range(1,7,2))
#print(t1)
#print (type(t1))

t2=(1,)
#print(t2)
#print(type(t2))

t3= (t) * 2
#print(t3)

#print(t3.count(1))

#print(len(t))

#命名元祖 namedtuple
#返回一个子列，并定义了字段  fields_name 可以是空格 或者是字段的列表
# 使用 from collections import namedtuple

from collections import namedtuple
point=namedtuple('point','x,y')
p1=point(4,5)
p2=point(-2,6)
print (p1)
print (p2)
#字段操作
print (p1.x + p1.y)
print (p2.x * p2.y)
studends=namedtuple('studend','name,age')
tom=studends('tom',18)
jerry=studends('jerry',20)
print(tom)
print(jerry)
#.字段去字段的值
print(tom.age)
print(jerry.name)

#三数比较