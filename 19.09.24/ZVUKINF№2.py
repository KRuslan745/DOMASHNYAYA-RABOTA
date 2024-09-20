#2.3.4 Представление звуковой информации
# №2
def calculate(time_min, volume_mb, razresh_bits):
    volume_bytes = volume_mb * 1024 * 1024 #переводим мб в байты
    time_sec = time_min * 60 #переводим минуты в секунды
    chastota_diskr = (volume_bytes * 8) / (time_sec * razresh_bits) #преобразуем формулу для нашего примера
    return chastota_diskr

if __name__ == "__main__":
    time_min = 1 #время записи
    volume_mb = 1.3 #объем памяти в мб
    razresh_bits = 8 #разрешение(разрядность)
    print("Частота дискретизации равна", calculate(time_min, volume_mb, razresh_bits), "Гц")