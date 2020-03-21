from random import randint

def insertionSort(array):
    for index in range(N):
        currentvalue = array[index]
        while index > 0 and array[index - 1] > currentvalue:
            array[index] = array[index - 1]
            index = index - 1
        array[index] = currentvalue

N = 10
a = []
for index in range(N):
    a.append(randint(0, 99))

print(a)
insertionSort(a)
print(a)