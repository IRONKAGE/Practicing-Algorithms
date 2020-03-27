from random import randint

# logic of Algorithm [логіка алгоритму]
def heapify(array, number_of_values, horizontal_index):
    largest_value = horizontal_index
    left_value = 2 * horizontal_index + 1
    right_value = 2 * horizontal_index + 2
    if left_value < number_of_values and array[horizontal_index] < array[left_value]: 
        largest_value = left_value
    if right_value < number_of_values and array[largest_value] < array[right_value]: 
        largest_value = right_value 
    if largest_value != horizontal_index: 
        array[horizontal_index], array[largest_value] = array[largest_value], array[horizontal_index]
        heapify(array, number_of_values, largest_value) 

def heap_sort(array): 
    number_of_values = len(array) 
    for vertical_index in range(number_of_values, -1, -1): 
        heapify(array, number_of_values, vertical_index) 
    for horizontal_index in range(number_of_values - 1, 0, -1): 
        array[horizontal_index], array[0] = array[0], array[horizontal_index]
        heapify(array, horizontal_index, 0)

# test case [Тестовий випадок]
N = 10
a = []
for index in range(N):
    a.append(randint(0, 99))
number_of_values = len(a)

print(a) # Random array [Випадковий масив]
heap_sort(a)
print(a) # Sorted array [Відсортований масив]