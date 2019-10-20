#请输入成绩：如果大于等于90，输出“优秀”，如果大于等于70，输出“良好”，如果大于等于60，输出“及格”，否则输出“不及格”
#
while True:
    a = input("请输入成绩：")
    if len(a) == 3:
        b =  int(a)
        if b == 100:
            print("满分优秀")
            break
        else:
            print("输入错误，请重新输入: ")
    elif len(a) == 2:
        b = int(a)
        if b >= 90:
            print("优秀")
            break
        elif b>= 70:
            print("成绩良好")
            break
        elif b>= 60:
            print("成绩及格")
            break
        else:
            print("成绩不及格")
            break
    elif len(a) == 1:
        b = int(a)
        if b >= 0:
            print("成绩不及格")
            break
    else:
        print("输入有误，请重新输入：")