def str2hex(str):
    strs = list(bytes(str, 'UTF-8').hex())  # 转化
    newStr = ''
    for i in range(0, int(len(strs) / 2)):
        newStr = newStr + '%' + strs[2 * i] + strs[2 * i + 1]
    return newStr
