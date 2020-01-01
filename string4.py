# 遍历字符串 进行字符串 操作

train_str = "Becauseisothesamepresentsimplethanpresentcontinuous"

for i in range(0, len(train_str)-1, 3):
    print(train_str[i] + train_str[i+1] + train_str[i+2])
