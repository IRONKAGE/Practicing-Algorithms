from random import randint

# class Node:
#     def __init__(self,info): #constructor of class
#         self.info = info  #information for node
#         self.left = None  #left leef
#         self.right = None #right leef
#         self.level = None #level none defined
#     def __str__(self):
#         return str(self.info) #return as string

# class BinaryTreeSort:
#     def __init__(self): #constructor of class
#         self.root = None

#     def create(self,val):  #create binary search tree nodes
#         if self.root == None:
#             self.root = Node(val)
#         else:
#             current = self.root
#             while 1:
#                 if val < current.info:
#                     if current.left:
#                         current = current.left
#                     else:
#                         current.left = Node(val)
#                         break;      

#                 elif val > current.info:
#                     if current.right:
#                         current = current.right
#                     else:
#                         current.right = Node(val)
#                         break;      
#                 else:
#                     break 

#     def bft(self):
#         self.root.level = 0 
#         queue = [self.root]
#         out = []
#         current_level = self.root.level
#         while len(queue) > 0:
#             current_node = queue.pop(0)
#             if current_node.level > current_level:
#                 current_level += 1
#                 out.append("\n")
#                 out.append(str(current_node.info) + " ")
#             if current_node.left:
#                 current_node.left.level = current_level + 1
#                 queue.append(current_node.left)  
#             if current_node.right:
#                 current_node.right.level = current_level + 1
#                 queue.append(current_node.right)  

#     def inorder(self,node):
#         if node is not None:              
#             self.inorder(node.left)
#             self.inorder(node.right)

#     def preorder(self,node):
#         if node is not None:
#             self.preorder(node.left)
#             self.preorder(node.right)

#     def postorder(self,node):
#         if node is not None:
#             self.postorder(node.left)
#             self.postorder(node.right)

# class Node: 
#     def __init__(self, d): 
#         self.data = d 
#         self.left = None
#         self.right = None
        
#     def sortedArrayToBST(arr): 
#     if not arr: 
#         return None
#     mid = (len(arr)) / 2
#     root = Node(arr[mid]) 
#     root.left = sortedArrayToBST(arr[:mid]) 
#     root.right = sortedArrayToBST(arr[mid+1:]) 
#     return root 


# class SortTree:
#     def __init__(self, value):
#         self.left = None
#         self.value = value
#         self.right = None
#     def insert_val(self, _value):
#         if _value < self.value:
#             if self.left is None:
#                 self.left = SortTree(_value)
#             else:
#                 self.left.insert_val(_value)
#         else:
#             if self.right is None:
#                 self.right = SortTree(_value)
#             else:
#                 self.right.insert_val(_value)

# def display(_node):
#     return list(filter(None, [i for b in [display(_node.left) if isinstance(_node.left, SortTree) else [getattr(_node.left, 'value', None)], [_node.value], display(_node.right) if isinstance(_node.right, SortTree) else [getattr(_node.right, 'value', None)]] for i in b]))

# tree = SortTree(4)


# class BinaryTreeSort:
#     def __init__(self, value):
#         self.left = None
#         self.value = value
#         self.right = None
#     def insert_val(self, _value):
#         if _value < self.value:
#             if self.left is None:
#                 self.left = BinaryTreeSort(_value)
#             else:
#                 self.left.insert_val(_value)
#         else:
#             if self.right is None:
#                 self.right = BinaryTreeSort(_value)
#             else:
#                 self.right.insert_val(_value)
#     @classmethod
#     def display(cls, _node):
#         return list(filter(None, [i for b in [cls.display(_node.left) if isinstance(_node.left, BinaryTreeSort) else [getattr(_node.left, 'value', None)], [_node.value], cls.display(_node.right) if isinstance(_node.right, BinaryTreeSort) else [getattr(_node.right, 'value', None)]] for i in b]))
# def display(_node):
#     return list(filter(None, [i for b in [display(_node.left) if isinstance(_node.left, BinaryTreeSort) else [getattr(_node.left, 'value', None)], [_node.value], display(_node.right) if isinstance(_node.right, BinaryTreeSort) else [getattr(_node.right, 'value', None)]] for i in b]))


# tree = SortTree(4)
# for i in [5, 3, 1, 2, 8, 7, 4]:
#     tree.insert_val(i)

# print(SortTree.display(tree))


# def orderTree(node):        
#     if "children" in node and node['children']:
#         node['children'].sort(key= lambda x : (findHeight(x), children(x) ) )

#         for child in node['children']:
#             print(child['name'])
#             orderTree(child)




# class Node: 
#     def __init__(self,key): 
#         self.left = None
#         self.right = None
#         self.val = key 

# def printInorder(root): 
#     if root: 
#         printInorder(root.left) 
#         print(root.val), 
#         printInorder(root.right) 

# def printPostorder(root): 
#     if root: 
#         printPostorder(root.left) 
#         printPostorder(root.right) 
#         print(root.val), 

# def printPreorder(root): 
#     if root: 
#         print(root.val), 
#         printPreorder(root.left) 
#         printPreorder(root.right) 



# root = Node(1) 
# root.left      = Node(2) 
# root.right     = Node(3) 
# root.left.left  = Node(4) 
# root.left.right  = Node(5) 
# printPreorder(root) 
# printInorder(root)
# printPostorder(root) 



# def tree_by_levels(node):
#     return [v for v, _, _ in sorted(extract_nodes(node), key = lambda x: (x[1], x[2]))]

# def extract_nodes(node, lvl=0, directions=[]):
#     if node:
#         return [(node.value, lvl, directions)] + extract_nodes(node.left, lvl+1, directions + [-1]) + extract_nodes(node.right, lvl+1, directions + [1])
#     return []

# def printSorted(arr, start, end):
#     if start > end:  
#         return
      
#     # print left subtree  
#     printSorted(arr, start * 2 + 1, end) 
      
#     # print root  
#     print(arr[start], end = " ")  
      
#     # print right subtree  
#     printSorted(arr, start * 2 + 2, end) 


# if __name__ == '__main__':
#     N = 10
#     arr = []
#     for index in range(N):
#         arr.append(randint(0, 99))
#     arr_size = len(arr)
#     print(arr) # Random array [Випадковий масив]
#     printSorted(arr, 0, arr_size - 1) 



# class BTNode:
#     def __init__(self, val=None, left=None, right= None):
#         self.val=val
#         self.left=left
#         self.right=right
#     def grow_left(self, val=None):
#         if self.left != None:
#             print ("This Node Already has Left Child")
#         else:
#             self.left = BTNode(val)
#     def grow_right(self, val = None):
#         if self.right != None:
#             print("This Node Already has Right Child")
#         else:
#             self.right =BTNode(val)
#     def print_tree(self):
#         print('(', end='')
#         if self.left != None:
#             self.left.print_tree()
#         print(self.val, end='')
#         if self.right != None:
#             self.right.print_tree()
#         print(')', end= '')
    
# class BTree:
#     def __init__(self):
#         self.root=None
# def build_tree(tree,values):
#         if tree.root != None:
#             print("The Tree is not Empty")
#         else:
#             if len(values)== 0:
#                 print("The List is empty")
#             else:
#                 tree.root =BTNode(values[0])
#                 for value in values [1:]:
#                     current_node = tree.root
#                     while current_node != None:
#                         if value < current_node.val:
#                             if current_node.left == None:
#                                 current_node.left = BTNode(value)
#                                 current_node=None
#                             else:
#                                 current_node = current_node.left
#                         else:
#                             if current_node.right== None:
#                                 current_node.right = BTNode(value)
#                                 current_node=None
#                             else:
#                                 current_node=current_node.right    

# my_tree = BTree()

# build_tree(my_tree, [4,9,2,3,11,0,6,12])



class node():
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 
    
    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

def inorder(root, res):
    # Recursive travesal 
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)

def treesort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])
    # Traverse BST in order. 
    res = []
    inorder(root,res)
    return res

# print(treesort([7,1,5,2,19,14,17]))

# my_tree.root.print_tree()
# test case [Тестовий випадок]
N = 10
a = []
for index in range(N):
    a.append(randint(0, 99))

print(a) # Random array [Випадковий масив]
print(treesort(a))
# print(a) # Sorted array [Відсортований масив]


# test case [Тестовий випадок]
# N = 10
# a = []
# for index in range(N):
#     a.append(randint(0, 99))

# print(a) # Random array [Випадковий масив]
# printSorted(a)
# print(a) # Sorted array [Відсортований масив]


# print(a) # Random array [Випадковий масив]
# Node(a)
# # BinaryTreeSort.display(a)
# print(a) # Sorted array [Відсортований масив]