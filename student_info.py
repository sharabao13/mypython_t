# 学生信息管理系统
score_list = []
str_print = "姓名: {}\t年龄: {}\t 数学成绩: {}\t 语文成绩: {}\t 英文成绩: {}\t 总分: {}"
while True:
    print("""
    ===========================================
    学生信息管理系统
    1. 新建学生信息
    2. 显示全部信息
    3. 查询学生信息
    4. 删除学生信息
    5. 修改学生信息
    
    0. 退出系统
    """)
    action = input("请选择你需要的操作: \n")
    if action == "1":
        """新建学生信息"""
        name = input("请输入名字: ")
        age = input("请输入年龄: ")
        math_score = input("请输入数学成绩: ")
        chinese_score = input("请输入语文成绩: ")
        english_score = input("请输入英语成绩: ")
        score_total = int(math_score) + int(chinese_score) + int(english_score)
        score_list.append([name, age, math_score, chinese_score, english_score, score_total])
        print(str_print.format(name, age, math_score, chinese_score, english_score, score_total))
    elif action == "2":
        """显示全部信息"""
        for info in score_list:
            print(str_print.format(*info))
    elif action == "3":
        """查询学生信息"""
        name =  input("请输入要查询的姓名: ")
        for info in score_list:
            if name in info:
                print(str_print.format(*info))
                break
        else:
            print("学生不存在")
    elif action == "4":
        """删除学生信息"""
        name = input("请输入要删除的姓名: ")
        for info in score_list:
            if name in info:
                info_ = score_list.pop(score_list.index(info))
                print("删除学生的信息: \n", info_)
                break
        else:
            print("学生不存在")
    elif action == "5":
        """修改学生信息"""
        name = input("请输入要修改的姓名: ")
        for info in score_list:
            if name in info:
                index_info = score_list.index(info)
                break
        else:
            print("学生不存在")
            continue
        math_score = input("请输入数学成绩: ")
        chinese_score = input("请输入语文成绩: ")
        english_score = input("请输入英语成绩: ")
        score_total = int(math_score) + int(chinese_score) + int(english_score)
        score_list[index_info][1:] = [age, math_score, chinese_score, english_score, score_total]
        print("修改后的信息: \n", score_list[index_info])
    elif action == "0":
        """退出系统"""
        break
    else:
        print("输入有误，请重新输入")