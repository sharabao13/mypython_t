# 凯撒加密
# 当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推
# 输入要加密的字符串
message = input("Enter you message: ")
# 输入偏移量 -26 - 26
key = int(input("how many charchets should we shift(-26~26): "))
# 定义secret_message 初始值
secret_message = ""
# 加密
# 遍历字符串
for char in message:
    # 判断字符索引类型 字母执行 字母+ 偏移量
    if char.isalpha():
        char_code = ord(char) + key
        # 大写判断
        if char.isupper():
            # 字母大于'Z' -26 从A开始
            if char_code > ord('Z'):
                char_code -= 26
            # 字母小于"A" +26 从Z开始
            if char_code < ord('A'):
                char_code += 26
        # 小写判断
        if char.islower():
            # 字母大于'z' -26 从A开始
            if char_code > ord('z'):
                char_code -= 26
            # 字母小于"a" +26 从Z开始
            if char_code < ord('a'):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char
print("encrypted message: ", secret_message)

# 解密
key = -key
orig_mesage = ""
for char in secret_message:
    # 判断字符索引类型 字母执行 字母+ 偏移量
    if char.isalpha():
        char_code = ord(char) + key
        # 大写判断
        if char.isupper():
            # 字母大于'Z' -26 从A开始
            if char_code > ord('Z'):
                char_code -= 26
            # 字母小于"A" +26 从Z开始
            if char_code < ord('A'):
                char_code += 26
        # 小写判断
        if char.islower():
            # 字母大于'z' -26 从A开始
            if char_code > ord('z'):
                char_code -= 26
            # 字母小于"a" +26 从Z开始
            if char_code < ord('a'):
                char_code += 26
        orig_mesage += chr(char_code)
    else:
        orig_mesage += char
print("decrypted message: ",orig_mesage)