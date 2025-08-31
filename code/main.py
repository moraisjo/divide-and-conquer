def maxmin_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    mid = (left + right) // 2
    
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)
    
    # Combinação dos resultados
    return min(min1, min2), max(max1, max2)

if __name__ == "__main__":
    numeros = [7, 2, 9, 4, 1, 6, 10, 3, 152, 8, 5]
    minimo, maximo = maxmin_select(numeros, 0, len(numeros) - 1)
    print("Sequência:", numeros)
    print("Menor elemento:", minimo)
    print("Maior elemento:", maximo)
