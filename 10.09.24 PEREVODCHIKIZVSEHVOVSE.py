def int_fract():
    try:
        var1 = str(input("Введите число: "))
        first_num = int(input("Введите систему счисления этого числа: "))
        second_num = int(input("Введите систему счисления, в которую хотите перевести: "))
    except ValueError:
        return "Введите корректное число и основания систем счисления!"
    
    if first_num < 2 or first_num > 16:
        return "Введите существующее основание!"
    elif second_num < 2 or second_num > 16:
        return "Введите существующее основание!"

    alf = {
        "0": "0", 
        "1": "1", 
        "2": "2", 
        "3": "3", 
        "4": "4", 
        "5": "5", 
        "6": "6", 
        "7": "7", 
        "8": "8", 
        "9": "9", 
        "10": "A", 
        "11": "B", 
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    int_part = ""
    fract_part = ""
    flag = False
    
    for i in var1:
        if i == ",":
            flag = True
            continue
        if not flag:
            int_part += i
        else:
            fract_part += i

    if not int_part:
        base_int_part = "0"
    else:
        dec_int_part = int_conv(first_num, int_part, alf)
    
    if not fract_part:
        dec_fract_part = 0
    else:
        dec_fract_part = fract_conv(first_num, fract_part)

    result_int_part = str(inte_conv(alf, dec_int_part, second_num))
    
    if dec_fract_part != 0:
        result_fract_part = "," + str(fracte_conv(alf, dec_fract_part, second_num))
    else:
        result_fract_part = ""
    
    return result_int_part + result_fract_part
            
def int_conv(first_num, int_part, alf):
    dec_int_part = 0
    index = len(int_part) - 1
    for i in int_part:
        dec_int_part += int(alf[i]) * (first_num ** index)
        index -= 1
    return dec_int_part

def fract_conv(first_num, fract_part):
    dec_fract_part = 0
    index = 1
    for i in fract_part:
        dec_fract_part += int(i) * (first_num ** -index)
        index += 1
    return dec_fract_part

def inte_conv(alf, dec_int_part, second_num):
    if dec_int_part == 0:
        return "0"
    base_int_part = ""
    num = dec_int_part
    while num > 0:
        comp = num % second_num
        base_int_part = alf[str(comp)] + base_int_part
        num //= second_num
    return base_int_part
        
def fracte_conv(alf, dec_fract_part, second_num):
    if dec_fract_part == 0:
        return ""
    base_fract_part = ""
    num = dec_fract_part
    while num > 0 and len(base_fract_part) < 10:
        num *= second_num
        digit = int(num)
        base_fract_part += alf[str(digit)]
        num -= digit
    return base_fract_part

if __name__ == "__main__":
    print(int_fract())
