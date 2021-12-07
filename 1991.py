class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(root):
    if root:
        print(root.data, end='')
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end='')
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end='')


N = int(input())
nodes = [Node(chr(i)) for i in range(65, 65+N)]

for i in range(N):
    input_str = input().split(' ')
    node = nodes[ord(input_str[0])-65]
    left = input_str[1]
    right = input_str[2]
    if left != '.':
        left = nodes[ord(input_str[1])-65]
    else:
        left = None
    if right != '.':
        right = nodes[ord(input_str[2])-65]
    else:
        right = None
    node.left = left
    node.right = right

preorder(nodes[0])
print()
inorder(nodes[0])
print()
postorder(nodes[0])