#  两个数的加减乘除
# 5 4
#5+4
#5-4
#5*4
#5/4
#5%4

# 输入两个数  input .split方法用空格分隔输入的两个变量
num1,num2=input('Enter 2 num: ').split()

#convert str to integer (+ _ * / %)
num1=int(num1)
num2=int(num2)

#Calculation num
sum=num1+num2
dif=num1-num2
mul=num1*num2
div=num1/num2
rem=num1%num2


#format print
print('{} + {} = {}'.format(num1,num2,sum))
print('{} - {} = {}'.format(num1,num2,dif))
print('{} x {} = {}'.format(num1,num2,mul))
print('{} / {} = {}'.format(num1,num2,div))
print('{} % {} = {}'.format(num1,num2,rem))