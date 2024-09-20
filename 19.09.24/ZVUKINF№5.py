#2.3.4 Представление звуковой информации
# №5
def calculate(chastota_diskr_kgz, time_min, razresh_bits):
    chastota_diskr_gz = chastota_diskr_kgz * 1000 #переводим кГц в Гц
    time_sec = time_min * 60 #переводим время в секунды
    volume_mess = ((chastota_diskr_gz * time_sec * razresh_bits) / 8) / 1024 #преобразуем формулу для нашего примера (делим на 1024 чтобы получить кб из байт)
    return volume_mess

if __name__ == "__main__":
    chastota_diskr_kgz = 8 #частота дискретизации в кГц
    time_min = 1 #количество времени в минутах
    razresh_bits = 16 #разрешение(разрядность)
    print("Объем моноаудиофайла:", calculate(chastota_diskr_kgz, time_min, razresh_bits), "Кб")