from random import randint

def selection_sort(array):
    for index in range(len(array) - 1):
        minimum = index
        newIndex = index + 1
        while newIndex < len(array):
            if array[newIndex] < array[minimum]:
                minimum = newIndex
            newIndex = newIndex + 1
        array[index], array[minimum] = array[minimum], array[index]

N = 10
a = []
for i in range(N):
    a.append(randint(0, 99))

print(a)
selection_sort(a)
print(a)