#打印斐波那契第101项
a = 1
b = 2
index = 2
print("{0},{1}" .format(0,0))
print("{0},{1}" .format(1,1))
print("{0},{1}" .format(2,1))
while True:
    c = a + b
    a = b
    b = c
    index += 1
    print('{0},{1}'.format(index,c))
    if index == 101:
        break

