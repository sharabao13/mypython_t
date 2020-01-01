# 打印圣诞树  5行树 加一行树干
    #
   ###
  #####
 #######
#########
    #

# 查找规律
# 第一行 4个空格  1 个#号
# 第二行 3个空格  3 个#号
# 第三行 2个空格  5 个#号
# 第四行 1个空格  7 个#号
# 第五行 0个空格  9 个#号
# 树干 跟第一行一样


# 让用户输入数的高度
tree_height = input("请输入树的高度: ")
# 将数的高度转换为整形
tree_height = int(tree_height)
#定义空格的初始值
space =  tree_height - 1
#定义#的初始值
hashs = 1
#定义树干的初始值
tree = tree_height - 1
#用循环打印数的结构
while tree_height != 0:
    for i in range(space):
        print(" ", end="")
    for i in range(hashs):
        print("#", end="")
    tree_height -= 1
    space -= 1
    hashs += 2
    print()
for i in range(tree):
    print(" ",end="")
print("#")