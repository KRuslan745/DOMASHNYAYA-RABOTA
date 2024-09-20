#2.3.4 Представление звуковой информации
# №3
def calculate(chastota_diskr, volume_gb, razresh_bits):
    volume_bytes = volume_gb * 1024 * 1024 * 1024 #переводим Гб в байты
    time_sec = (volume_bytes * 8) / (chastota_diskr * razresh_bits) #преобразуем формулу для нашего примера
    return time_sec #не стал переводить в минуты потому что не понтяно нужно или нет

if __name__ == "__main__":
    chastota_diskr = 44100 #частота дискретизации в Гц
    volume_gb = 0.01 #объем памяти в гб
    razresh_bits = 16 #разрешение(разрядность)
    print("Длительность звучания аудиофайла:", calculate(chastota_diskr, volume_gb, razresh_bits), "секунда")