from random import randint

# logic of Algorithm [логіка алгоритму]
def insertionSort(array):
    for horizontal_index in range(len(array)):
        current_value = array[horizontal_index]
        vertical_index = horizontal_index
        while vertical_index > 0 and array[vertical_index - 1] > current_value:
            array[vertical_index] = array[vertical_index - 1]
            vertical_index = vertical_index - 1
        array[vertical_index] = current_value

# test case [Тестовий випадок]
N = 10
a = []
for index in range(N):
    a.append(randint(0, 99))

print(a) # Random array [Випадковий масив]
insertionSort(a)
print(a) # Sorted array [Відсортований масив]