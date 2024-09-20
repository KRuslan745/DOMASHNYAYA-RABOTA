#2.3.4 Представление звуковой информации
# №4
def calculate(chastota_diskr_kgz, volume_kb, razresh_bits):
    volume_bytes = volume_kb * 1024 #переводим кб в байты
    chastota_diskr_gz = chastota_diskr_kgz * 1000 #переводим кГц в Гц
    time_sec = (volume_bytes * 8) / (chastota_diskr_gz * razresh_bits) #преобразуем формулу для нашего примера
    return time_sec 

if __name__ == "__main__":
    chastota_diskr_kgz = 32 #частота дискретизации в кГц
    volume_kb = 700 #объем памяти в КБ
    razresh_bits = 16 #разрешение(разрядность)
    print("Время звучания моноаудиофайла:", calculate(chastota_diskr_kgz, volume_kb, razresh_bits), "секунды")