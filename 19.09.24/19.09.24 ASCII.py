alf_one = {
    'К': '11001010', 'а': '11100000', 'к': '11101010', ' ': '00100000', 'н': '11101101', 'и': '11101000', 'п': '11101111',
    'е': '11100101', 'ч': '11110111', 'л': '11101011', 'ь': '11111100', 'о': '11101110', ',': '10000010', 'т': '11110010',
    'р': '11110000', 'в': '11100010', 'ы': '11111011', 'ю': '11111110', '.': '00101110', 'Е': '11000101', 'с': '11110001',
    'ц': '11110110', '-': '10010110', 'д': '11100100', 'ж': '11100110', 'у': '11110011', 'ш': '11111000', 'щ': '11111001',
    'й': '11101001', 'ё': '10111000', 'м': '11101100', 'з': '11100111', 'б': '11100001', 'я': '11111111', 'х': '11110101'
}

alf_two = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

def sentence_to_binary(sentence, alf_one):
    internal_representation = ""
    for char in sentence:
        if char in alf_one:
            internal_representation += alf_one[char]
    return internal_representation

def binary_to_hex(internal_representation, alf_two):
    hex_representation = ""
    for i in range(0, len(internal_representation), 4):
        num = internal_representation[i:i+4]
        if num in alf_two:
            hex_representation += alf_two[num]
    return hex_representation

if __name__ == "__main__":
    sentence = "Как ни печально, но альтернативы напряжённому труду нет. Если твоя цель — сделаться незаменимым, ты должен работать дольше, быстрее и напряжённее остальных."
    print("Внутреннее представление в двоичной форме:", sentence_to_binary(sentence, alf_one))
    print("В шестнадцатеричной форме:", binary_to_hex(sentence_to_binary(sentence, alf_one), alf_two))