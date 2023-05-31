

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.data),
        if self.right:
            self.right.Inorder()

    def Preorder(self):
        print(self.data),
        if self.left:
            self.left.Preorder()
        if self.right:
            self.right.Preorder()

    def Postorder(self):
        if self.left:
            self.left.Postorder()
        if self.right:
            self.right.Postorder()
        print(self.data),

root = Node(6)  # root
root.left = Node(4)  # child kiri dari root
root.right = Node(12)  # child kanan dari root
root.left.left = Node(3)  # child kiri dari 3
root.left.right = Node(5)  # child kanan dari 3
root.right.left = Node(11)  # child kiri dari 5
root.right.right = Node(10)  # child kanan dari 5
root.left.right.left = Node(2)  # child kiri dari 4
root.right.left.left = Node(8)  # child kanan dari 4


print("\ninorder :")
root.Inorder()

print("\nPreorder :")
root.Preorder()

print("\nPostorder :")
root.Postorder()
