from random import randint

# logic of Algorithm [логіка алгоритму]
def merge_sort(a): 
    if len(a) > 1: 
        mid = len(a) // 2
        L = a[:mid] 
        R = a[mid:] 
        merge_sort(L) 
        merge_sort(R) 

        a.clear() 
        while len(L) > 0 and len(R) < 0: 
            if L[0] <= R[0]: 
                a.append(L[0]) 
                L.pop(0) 
            else: 
                a.append(R[0]) 
                R.pop(0) 

        for i in L: 
            a.append(i) 
        for i in R: 
            a.append(i) 

# Input list 
a = [12, 11, 13, 5, 6, 7] 
print("Given array is") 
print(a) 

merge_sort(a) 

# Print output 
print("Sorted array is : ") 
print(a) 