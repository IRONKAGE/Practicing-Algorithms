from random import randint

# logic of Algorithm [логіка алгоритму]
def selection_sort(array):
    for horizontal_index in range(len(array) - 1):
        minimum = horizontal_index
        vertical_index = horizontal_index + 1
        while vertical_index < len(array):
            if array[vertical_index] < array[minimum]:
                minimum = vertical_index
            vertical_index = vertical_index + 1
        array[horizontal_index], array[minimum] = array[minimum], array[horizontal_index]

# test case [Тестовий випадок]
N = 10
a = []
for i in range(N):
    a.append(randint(0, 99))

print(a) # Random array [Випадковий масив]
selection_sort(a)
print(a) # Sorted array [Відсортований масив]