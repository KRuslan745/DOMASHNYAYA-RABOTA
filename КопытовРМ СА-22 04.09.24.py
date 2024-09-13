import math
def task18(bait, straniza, stroka, simbol):
    all = straniza * stroka * simbol
    bit = bait * 8
    razmer_one_simbol = bit / all
    alfavit = 2 ** razmer_one_simbol
    return int(alfavit)


def task19(first, second):
    first_alf_simb = math.log2(first)
    second_anf_simb = math.log2(second)
    inf = first_alf_simb / second_anf_simb
    return int(inf)

def task20(alf_simbol, bit):
    razmer_one_simb = math.log2(alf_simbol)
    all_simb = bit / razmer_one_simb
    return int(all_simb)

def task21(bit):
    etazh = 2 ** bit
    return int(etazh)

def task22(bit):
    pod = 2 ** bit
    return int(pod)

def task23(bit, blue_kraska):
    white_kraska = blue_kraska
    mbjar = 2 ** bit
    p_white = 1 / mbjar
    N = white_kraska / p_white
    brown_kraska = N - (white_kraska + blue_kraska)
    return int(brown_kraska)

if __name__ == "__main__":
    #var1 = int(input("Объем в байтах: ")) 
    #var2 = int(input("Количество страниц: ")) 
    #var3 = int(input("Количество строк: "))
    #var4 = int(input("Количество символов: "))
    #print(task18(var1, var2, var3, var4), "символа")

    #var1 = int(input("Алфавит с наибольшей мощностью: ")) 
    #var2 = int(input("Алфавит с наименьшей мощностью: "))
    #print("В", task19(var1, var2), "раз")

    #var1 = int(input("Размер алфавита: ")) 
    #var2 = int(input("Обьем сообщения в битах: "))
    #print(task20(var1, var2), "символов")

    #var1 = int(input("Количество бит информации: ")) 
    #print(task21(var1), "этажей")

    #var1 = int(input("Количество бит информации: ")) 
    #print(task22(var1), "подъезда")

    var1 = int(input("Объем сообщения, о том что закончилась банка белой краски в битах: ")) 
    var2 = int(input("Количество синих банок: ")) 
    print(task23(var1, var2), "банок коричневой краски израсходовали")




