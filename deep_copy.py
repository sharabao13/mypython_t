#深度copy
import copy
date=[1,2,7,12,[4,1,1]]
copy1=copy.copy(date)
copy2=copy.deepcopy(date)
#print(copy1)
#print(copy2)
copy1[4][2]=8
print(date)
print(copy1)
print(copy2)

