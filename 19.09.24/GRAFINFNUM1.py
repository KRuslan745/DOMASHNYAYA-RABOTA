#2.3.3 Представление графической информации
# №1
def calculate(width, height):
    total_bits = int(width) * int(height) * 1 #здесь мы находим сколько всего бит занимает изображение (горизонатль на вертикаль и умножаем на 1 потому что битовая глубина 2-х цветного изображение равна 1)
    total_bytes = total_bits / 8 #здесь переводим в байты
    if total_bytes % 1 > 0: #этот цикл для того чтобы не получилось не целое число, м здесь округляем его если оно не целое до ближайшего
        total_bytes_rounded = int(total_bytes) + 1
    else:
        total_bytes_rounded = int(total_bytes)
    return total_bytes_rounded

if __name__ == "__main__":
    width = 10
    height = 10
    print(calculate(width, height), "байт")