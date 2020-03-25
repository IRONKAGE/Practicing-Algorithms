from random import randint

# logic of Algorithm [логіка алгоритму]
class BinaryTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, _value):
        if _value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(_value)
            else:
                self.left.insert(_value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(_value)
            else:
                self.right.insert(_value)

def in_order(root, results):
    if root:
        in_order(root.left, results)
        results.append(root.value)
        in_order(root.right, results)

def binary_tree_sort(array):
    if len(array) == 0:
        return array
    root = BinaryTreeNode(array[0])
    for vertical_index in range(1, len(array)):
        root.insert(array[vertical_index])
    result = []
    in_order(root, result)
    return result

# test case [Тестовий випадок]
N = 10
a = []
for index in range(N):
    a.append(randint(0, 99))

print(a) # Random array [Випадковий масив]
print(binary_tree_sort(a)) # Sorted array [Відсортований масив]