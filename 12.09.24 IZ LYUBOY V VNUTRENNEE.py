def convert_to_base():
    try:
        num_bytes = int(input("Введите количество байт: "))
        number = input("Введите число : ")
        input_base = int(input("Введите систему счисления числа : "))
        output_base = int(input("Введите систему счисления результата : "))
    except ValueError:
        return "Введите корректные значения!"

    if input_base < 2 or input_base > 16 or output_base < 2 or output_base > 16:
        return "Основание системы счисления должно быть между 2 и 16!"

    num_to_char = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    char_to_num = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }

    def is_valid_digit(char, base):
        return char in char_to_num and char_to_num[char] < base


    minus = number[0] == '-'
    if minus:
        number = number[1:] 
        
    def to_binary(number, base):
        dec_value = 0
        for i in range(len(number)):
            char = number[-(i + 1)]
            value = char_to_num[char]
            dec_value += value * (base ** i)
        binary_value = ""
        if dec_value == 0:
            binary_value = "0"
        while dec_value > 0:
            binary_value = str(dec_value % 2) + binary_value
            dec_value //= 2
        binary_length = num_bytes * 8
        binary_value = "0" * (binary_length - len(binary_value)) + binary_value
        return binary_value
    binary_value = to_binary(number, input_base)
    if minus:
        inverted_binary = ""
        for bit in binary_value:
            inverted_binary += '1' if bit == '0' else '0'
        inverted_dec = int(inverted_binary, 2) + 1
        binary_value = ""
        while inverted_dec > 0:
            binary_value = str(inverted_dec % 2) + binary_value
            inverted_dec //= 2
        binary_value = "0" * (num_bytes * 8 - len(binary_value)) + binary_value

    def binary_to_base(binary_value, base):
        dec_value = 0
        for i in range(len(binary_value)):
            bit = binary_value[-(i + 1)]
            dec_value += int(bit) * (2 ** i)
        base_value = ""
        if dec_value == 0:
            base_value = "0"
        while dec_value > 0:
            base_value = num_to_char[dec_value % base] + base_value
            dec_value //= base
        return base_value
    base_value = binary_to_base(binary_value, output_base)
    required_length = num_bytes * 2
    base_value = "0" * (required_length - len(base_value)) + base_value
    return (f"Внутреннее представление : {binary_value}\n"
            f"Результат в системе счисления : {base_value}")

if __name__ == "__main__":
    print(convert_to_base())