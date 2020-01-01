list1 = ["apple","banana",1,2,1.5,1,3,5,6,1,1,3,4,5,6,1,1]
list2 = ["ping","bao","tae"]
list3 = [3,4,5,7,1,]

#print(list1.count(1))
#print(len(list2))
list1.append("orainge")
#print(list1)

list2[0] = "mei"
#print(list2)

list3[3] = 6
#print(list3)
list1.insert(3,"apache")
#print(list1)
list3.append("ig")
#print(list1.index(1,-8))
#print(list3)
list4 = list1 + list2
#print(list4)
list5 = list4 * 2
#print(list5)
list5.clear()
list3.remove(4)
#print(list3)
list6=list1.pop(0)
#print(list1)
#print(list6)
list1=[2,45,6,1,23,5,6,8]
list1.reverse()
#print(list1)
list1.reverse()
#print(list1)

list1.sort(reverse=True)
#print(list1)
list2=[3,5,7,11,23,56,2,3,4,7,9]
list2.sort(reverse=False)
#print(list2)
list3=[23,6,7,1,"b","apce",22]
list3.sort(key=str,reverse=True)
#print(list3)
list4=list3.copy()
#print(list4)
