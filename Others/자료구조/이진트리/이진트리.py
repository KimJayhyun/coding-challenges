## PNG 파일 참고

##################################################################################################################

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def makeingTree(arr, root, i):
    if(i < len(arr)) :
        root = Node(arr[i])
        root.left = makeingTree(arr, root.left, 2*i + 1)
        root.right = makeingTree(arr, root.right, 2*i + 2)
    return root

root = None

tree = makeingTree(arr, root ,0)

print(tree.data)

##################################################################################################################

answer = []
def Inorder(root, answer):
    if (root.left != None):
        Inorder(root.left, answer)
    
    answer.append(root.data)

    if (root.right != None):
        Inorder(root.right, answer)
    
Inorder(tree, answer)

print(answer)
