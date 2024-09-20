#2.3.3 Представление графической информации
# №4
import math
def calculate(num_colors, volume_memory):
    bits_memory = volume_memory * 8 # получаем биты
    bits_deep = math.log2(num_colors) #находим битовую глубину
    total_points = bits_memory // bits_deep #чтобы найти количество точек мы должны количсетво бит разделить на глубину(по формуле горизонталь * вертикаль * глубину = объем в байтах)
    return total_points

if __name__ == "__main__":
    num_colors = 256
    volume_memory = 120
    print("256-цветный рисунок состоит из", calculate(num_colors, volume_memory), "точек")