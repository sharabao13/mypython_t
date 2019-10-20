#判断学生成绩 学生成绩A-E ,其中90分以上为A ，80-89分为B，70-79为C 60-69为D，60分以下为E
#
score = input("input a student score: ")
score =  int(score)

if score >= 70:
    if score >= 90:
        val = "A"
    elif score >= 80:
        val = "B"
    else:
        val = "C"
else:
    if score >= 60:
        val = "D"
    else:
        val = "E"
print (val)