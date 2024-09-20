#2.3.4 Представление звуковой информации
# №1
def calculate(time_min, chastota_diskr_kgz, razresh_bits):
    time_sec = time_min * 60 #переводим минуты в секунды
    chastota_diskr_gz = chastota_diskr_kgz * 1000 #переводим из кГц в Гц
    volume_memory = (chastota_diskr_gz * time_sec * razresh_bits) / 8 #По формуле расчитываем объем памяти
    return volume_memory

def bytes_to_megabytes(volume_memory):
    return volume_memory / (1024 * 1024)  # переводим байты в мегабайты(подумал что можно перевести в мб чтобы число выглядело поменьше)

if __name__ == "__main__":
    time_min = 2 #время звучания
    chastota_diskr_kgz = 44.1 #частота дикретизации в кГц
    razresh_bits = 16 #разрешение
    print("Объем памяти равен", calculate(time_min, chastota_diskr_kgz, razresh_bits), "байт или", bytes_to_megabytes(calculate(time_min, chastota_diskr_kgz, razresh_bits)), "Мб")