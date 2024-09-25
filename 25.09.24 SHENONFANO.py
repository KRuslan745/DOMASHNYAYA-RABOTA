def ShennonFano(array, left, right):
    if left >= right:
        return
    border = delit(array, left, right)
    for i in range(left, border + 1):
        array[i][2] += "1"
    for i in range(border + 1, right + 1):
        array[i][2] += "0"
        
    ShennonFano(array, left, border)      
    ShennonFano(array, border + 1, right) 
    
def delit(array, left, right):
    total_sum = sum(item[1] for item in array[left:right + 1])
    half_sum = total_sum / 2
    current_sum = 0
    for i in range(left, right):
        current_sum += array[i][1]
        if current_sum >= half_sum:
            return i
    return left

def sort_ub(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j][1] < array[j + 1][1]:  
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == "__main__":
    array = [["a", 3, ""], ["b", 3, ""], ["c", 3, ""], ["d", 3, ""]]
    sort_ub(array)
    ShennonFano(array, 0, len(array) - 1)
    for symbol in array:
        print(f"Символ: {symbol[0]}, - {symbol[2]}")