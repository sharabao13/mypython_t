# 倒排99乘法表

for i in range(1,10):
    print(" " *10*(i-1), end = " ")
    for j in range(i,10):
        print("{0}*{1} = {2:<2}".format(i,j,i*j),end = "  ")
    print()