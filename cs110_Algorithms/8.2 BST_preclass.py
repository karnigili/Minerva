import random
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
        self.parent = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
                node.parent = root
  
            else:
                insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
                node.parent = root

            else:
                insert(root.r_child, node)

def search(root, value):
    if root is None :

        return "err"

    elif root.data == value :
        return root

    elif value < root.data:
        return search (root.l_child, value)

    else:
        return search (root.r_child, value)

def max (node):
    while node.r_child is not None:
        node = node.r_child
    return node

def min (node):
    while node.l_child is not None:
        node = node.l_child
    return node

def trans(root, node, newnode):
    if node.parent is None: 
        pass
    elif node == node.parent.l_child:
        node.parent.l_child = newnode
    else:
        node.parent.r_child = newnode

    if newnode is not None:
        newnode.parent = node.parent

def delete(root, node):
    if  search(root, node.data) == 'err':
        print "err"

    if node.l_child is None:
        trans (root, node, node.r_child)

    elif node.r_child is None:
        trans (root, node, node.l_child)

    else:
        suc = min(node.r_child)

        if suc.parent != node:

            trans (root, suc, suc.r_child)
            suc.r_child = node.r_child
            suc.r_child.parent = suc

        trans (root, node, suc)
        suc.l_child = node.l_child
        suc.l_child.parent = suc
    
    return node.data

def in_order_print(root):

    if root is None:
        return

    if root.l_child:
        in_order_print(root.l_child)

    print root.data

    if root.r_child:
        in_order_print(root.r_child)

def successor(root, node):
    parent = None

    if node.r_child != None:
        return min(node.r_child)
    parent = node.parent

    while parent != None and node == parent.r_child:
        node = parent
        parent = parent.parent
    return parent
 
def predecessor(root, node):
    parent = None

    if node.l_child != None:
        return max(node.l_child)
    parent = node.parent
    while parent != None and node == parent.l_child:
        node = parent
        parent = parent.parent
    return parent


current = None


def valid_bst(root):
    global g_current

    if root is None:
        return

    if root.l_child:
        valid_bst(root.l_child)

    if root.data < current:
        print root.data
        return False

    current = root.data

    if root.r_child:
        valid_bst(root.r_child)

    return True
#########################

numbers = range(10)
random.shuffle(numbers)
numbers = numbers+[-1]

root = Node(numbers[-1])

print "insert : "
for i in numbers[0:-1]:
    insert(root, Node(i)) 
    print "elem {} inserted ".format(i)

print "traverse in tree"
in_order_print(root)

print "root: {}".format(root.data)

# print "search : "

# for i in numbers:
#     print search(root, i)

print "delete"

for i in numbers[0:-1]:
    node  = search(root, i)
    print delete(root, node)

print

in_order_print(root)
# in_order_print(root)
