def int_fract(var1):
    int_part = ""
    fract_part = ""
    flag = False
    for i in var1:
        if i == ",":
            flag = True
            continue
        if flag == False:
            int_part = int_part + i
        else:
            fract_part = fract_part + i
    if flag == False:
        return str(int_conv(int_part))
    else:
        return str(int_conv(int_part)) + "," + str(fract_conv(fract_part))[2:]

def int_conv(var1):
    index = len(var1) - 1
    otv = 0
    for i in var1:
        otv = otv + int(i) * (2 ** index)
        index = index - 1
    return otv

def fract_conv(var1):
    index = 1
    otv = 0
    for i in var1:
        if index <= len(var1):
            otv = otv + int(i) * (2 ** -index)
            index = index + 1
    return otv


if __name__ == "__main__":
    var1 = str(input("Введите число: "))
    print(int_fract(var1))