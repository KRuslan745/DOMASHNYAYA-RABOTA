#2.3.3 Представление графической информации
# №3
def calculate(width, height, volume_memory):
    bit_memory = (volume_memory * 1024) * 8 # здесь мы переводим 1кб в биты
    bit_deep = bit_memory // (width * height) # находим битовую глубину
    num_colors = 2 ** bit_deep #по формуле находим число цветов(K = 2 в N степени)
    return num_colors

if __name__ == "__main__":
    width = 64
    height = 32
    volume_memory = 1
    print("Максимальное число цветов: ", calculate(width, height, volume_memory))