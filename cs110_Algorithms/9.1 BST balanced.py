import random
import math
import matplotlib.pyplot as plt
import numpy as np



class Node:
    def __init__(self, val, left=None, right=None):
        self.l_child = left
        self.r_child = right
        self.data = val
        self.l_count = 0


def insert(root, node):
	if root is None:
		root = node

	else:
		if root.data > node.data:
			root.l_count += 1

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

def avg_cmp(root):

	# keeps all nodes
	elements = [(root, 1)] #(node, its level)

	# set the vars that keep the num of comparisons and the num of nodes
	comp = 0.0
	summ_of_nodes = 0

	# as long as there are still elements to check
	while elements:
		# current elemet and cuurent level taken from the list
		node, level = elements.pop()

		# add an element with its weight (based on level) to the sum
		comp += level

		# add 1 to the sum of elements
		summ_of_nodes += 1

		# add the element children to the list of elements to check
		if node.l_child:
			elements.append((node.l_child, level + 1))

		if node.r_child:
			elements.append((node.r_child, level + 1))

	return comp / summ_of_nodes

def max_depth(root):
	#using th cmp func to check to deepest level

	elements = [(root, 1)] #node, its level
	depth = 0

	while elements:
		node, level = elements.pop()

		depth += level

		if node.l_child:
			elements.append((node.l_child, level + 1))

		if node.r_child:
			elements.append((node.r_child, level + 1))

	return depth

def delete(root, node):
    if  search(root, node.data) == 'err':
        print "err"

    if node.parent.data > node.data :
    	node.parent.l_count -= 1

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

def search(root, value):
    if root is None :

        return "err"

    elif root.data == value :
        return root

    elif value < root.data:
        return search (root.l_child, value)

    else:
        return search (root.r_child, value)

def select(root, k):

	#starting from the root with its left count = root rank
	node = root
	count = node.l_count

	# as long as the desirable count was not achieved 
	while count != k:

		# if the count is too small
		if count < k:

			# modify k to move to the right side of the tree by removing the amount of elemnts on the left side + the root
			k -= (count + 1)
			node = node.r_child

		# if the count is too big - go deeper in the left branch
		elif count > k : 
			node = node.l_child

		if node is None:

			return 

		count = node.l_count

	return node.data


def rank(root, value):

	# starting with the root with its values
	current_node = root
	node_value = current_node.data
	

	root_rank = 0

	# as long as the desirable value was not found 
	while node_value != value:

		#if value is too high - go right
		if node_value < value:

			# the current root is its left count + 1
			root_rank += current_node.l_count + 1
			current_node = current_node.r_child

		#if value is too low - go left (if data > value)
		else:  
			# deeper the left brach does not require a modification
			current_node = current_node.l_child

		if current_node is None:
			return 

		node_value = current_node.data

	return root_rank + current_node.l_count  
 

##########
### test ###
T1 = Node(12, Node(14))
T2 = Node(5, Node(2, right=Node(4)), Node(7, Node(6), Node(9, Node(8))))

numbers = range(10)

random.shuffle(numbers)
numbers = numbers

T3 = Node(numbers)

for i in numbers:
    insert(T3, Node(i)) 



### rank and select ###

print "there are {} elem smaller than {}".format(rank(T3, 6),6) 
print "the {}th smallest elem is {}".format(2,select (T3,2)) 

print rank(T3, select(T3, 2)) == 2


#### plot ####
x_axis = np.linspace(10, 10000, 30)
x_axis_int = [int(round(i)) for i in x_axis]

max_avg_scaling_log = []
avg_avg_scaling_log = []

for test in range(5):

	max_scaling_log = []
	avg_scaling_log = []

	for i in x_axis_int:
		seq = range(i)
		random.shuffle(seq)

		T4 = Node(seq)
		
		for j in seq:
			insert(T4, Node(j))

		max_scaling_log.append(max_depth(T4))
		avg_scaling_log.append(avg_cmp(T4))
	
	max_avg_scaling_log.append(max_scaling_log)
	avg_avg_scaling_log.append(avg_scaling_log)



avg_results = np.mean(avg_avg_scaling_log, axis = 0)
max_results = np.mean(max_avg_scaling_log, axis = 0)



plt.subplot(211)
plt.plot(x_axis_int, avg_results, label = 'avg depth')
plt.plot(x_axis_int, [2*math.log(i) for i in x_axis_int], label ='C log n')

plt.ylabel('avg depth')
plt.xlabel('n items')
plt.legend(loc =4)


plt.subplot(212)
plt.plot(x_axis_int, max_results, label = 'max depth')
plt.plot(x_axis_int, [20*i for i in x_axis_int], label = 'Cn')

plt.ylabel('max depth')
plt.xlabel('n items')
plt.legend(loc =4)

plt.title ('avg and max depth for BST')
plt.show()



