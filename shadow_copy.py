# 列表浅复制

list1=[1,2,3,[4,5,1]]
list2=list1.copy()
#print(list1)
#print(list2)
list2[3][1]=7
#print(list2)
#print(list1)

list3=[4,6,8]
list4=list3.copy()
#print(list3)
#print(list4)
list3[2]=1
print(list3)
print(list4)