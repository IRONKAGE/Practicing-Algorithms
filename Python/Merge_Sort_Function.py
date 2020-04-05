from random import randint

# logic of Algorithm [логіка алгоритму]
def merge_sort(array): 
    if len(array) > 1: 
        mid = len(array) // 2
        left_value = array[:mid] 
        right_value = array[mid:] 
        merge_sort(left_value) 
        merge_sort(right_value) 

        array.clear() 
        while len(left_value) > 0 and len(right_value) < 0: 
            if left_value[0] <= right_value[0]: 
                array.append(left_value[0]) 
                left_value.pop(0) 
            else: 
                array.append(right_value[0]) 
                right_value.pop(0) 

        for i in left_value: 
            array.append(i) 
        for i in right_value: 
            array.append(i) 

# test case [Тестовий випадок]
N = 10
a = []
for index in range(N):
    a.append(randint(0, 99))

print(a) # Random array [Випадковий масив]
merge_sort(a)
print(a) # Sorted array [Відсортований масив]