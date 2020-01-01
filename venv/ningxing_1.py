#打印菱形
for i in range(-3,4):
    if i < 0:
        j = -i
    else:
        j = i
    print(' '*j + "*" *(7 - j*2))

