def right(root):
	return 2 * root + 2

def left(root):
	return 2 * root + 1

def root(node):
	return (node-1)/2

def inorder_tree_walk (t, node = 0):
	# print node
	if node < len(t):

		inorder_tree_walk (t,left(node))
		print t[node]
		inorder_tree_walk (t,right(node))



def bt_search (t, item, node=0):
	if node > len(t):
		return False

	if t[node] == item:
		return node

	if item < t[node]:
		return bt_search(t, item, left(node))
	else:
		return bt_search(t,item, right(node))

def bt_iterative_search (t, node, item):

	while (node < len(t)) and (t[node] != item):

		if item < t[node]:

			node = left(node)
		else:
			node = right(node)

	if node < len(t):
		return node
	else:
		return False


def bt_min(t, node = 0):
	while node < len(t):
		node = left(node)

	return root(node)

def bt_max(t, node = 0):

	while node < len(t):
		node = right(node)

	return root(node)


def bt_successor (t, item):
	node = bt_search(t,item)

	if node > len(t):

		return bt_min(t, right(node))

	y = root(node)
	while y >= 0 and node == right(y):

		node = y
		y = root(y)

	return y	



# def bt_insert (t, item):



# print bt_successor([15,6,18,3,7,17,20], 17)

# print bt_iterative_search([15,6,18,3,7,17,20],0,20)
# print bt_max([15,6,18,3,7,17,20])
# inorder_tree_walk([15,6,18,3,7,17,20])