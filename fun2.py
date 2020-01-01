# 素数函数
# 判断素数 函数
def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
# 判断随机数以下的函数
def getPrime(numMax):
    primes = []
    for num1 in range(2, numMax):
        if isprime(num1):
            primes.append(num1)
    return primes
maxNum =  int(input("Enter a num: "))
listofPrimes = getPrime(maxNum)
for prime in listofPrimes:
    print(prime,end=', ')
