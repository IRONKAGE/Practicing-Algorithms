from random import randint

# logic of Algorithm [логіка алгоритму]
def shell_sort(array):
    gap = len(array) // 2
    while gap > 0: 
        for horizontal_index in range(gap, len(array)):
            current_value = array[horizontal_index] 
            vertical_index = horizontal_index
            while vertical_index >= gap and array[vertical_index - gap] > current_value: 
                array[vertical_index] = array[vertical_index - gap] 
                vertical_index -= gap 
            array[vertical_index] = current_value 
        gap //= 2

# test case [Тестовий випадок]
N = 10
a = []
for index in range(N):
    a.append(randint(0, 99))

print(a) # Random array [Випадковий масив]
shell_sort(a)
print(a) # Sorted array [Відсортований масив]