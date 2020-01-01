# 字符串加密 /解密 通过 ord 函数 chr函数

# 加密 大写的的字母，在进行解密 ILY

# 让用户输入字符串
orig_msg = input('Enter upper string: ')
encryption = ""
# 将字母转换为unicode 存放在 一个变量中
for word in orig_msg:
    if word.isalpha():
        encryption += str(ord(word) - 23)
    elif word.isspace():
        encryption += str(ord(word))
# 打印unicode
print(encryption)
# 将unicode进行解密
cryption= ''
for i in range(0, len(encryption)-1, 2):
    chr_code = encryption[i] + encryption[i+1]
    #空格的UNcode 等于32
    if chr_code != '32':
        cryption += chr(int(chr_code) + 23)
    else:
        cryption += chr(int(chr_code))
# 打印字符串
print(cryption)