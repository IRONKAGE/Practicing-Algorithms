from random import randint

# logic of Algorithm [логіка алгоритму]
def bubble_sort(array):
    for horizontal_index in range(len(array) - 1):
        for vertical_index in range(len(array) - horizontal_index - 1):
            if array[vertical_index] > array[vertical_index + 1]:
                current_value = array[vertical_index]
                array[vertical_index] = array[vertical_index + 1]
                array[vertical_index + 1] = current_value

# test case [Тестовий випадок]
N = 10
a = []
for index in range(N):
    a.append(randint(0, 99))

print(a) # Random array [Випадковий масив]
bubble_sort(a)
print(a) # Sorted array [Відсортований масив]