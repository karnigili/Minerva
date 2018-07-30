import random

#swap two elements in an array based on their indices
def swap (A, h, m):
	tmp = A[h]  
	A[h] = A[m]
	A[m]= tmp


# keeps the heap in order (max) by comparing parent element to its 'kids' //heapify
def max_heapify (A,root, heap_size):
	# defines the roots kids (left/right)
	l= 2*root + 1
	r= 2*root + 2
	largest_index = root

	#checks which is the largest elemnt
	if (l <= heap_size-1) and (A[l] > A[root]):
		largest_index = l
	
	if (r <= heap_size-1) and (A[r] > A[largest_index]):
		largest_index = r
	
	#moves the largest elemnt to the top
	if largest_index != root:
		print A
		swap(A,root,largest_index)
		max_heapify(A, largest_index, heap_size)


# return the max value of the heap
def heap_maximum (A):
	return A[0]

# pop the max element out . maintain max heap 	//heappop
def heap_extrat_max (A):

	heap_size = len(A)
	
	assert heap_size > 1 , "heap underflow"

	max_value = A[0]

	A[0] = A.pop(-1)

	heap_size = heap_size - 1

	max_heapify(A, 0, heap_size)
	print A
	return max_value

	
# floats a new added element to its correct location 
def heap_increase_key (A,key_index,key):
	
	# not -inf
	assert key > A[key_index] , "new key is smaller than current key"

	# insert the key to the last location
	A[key_index] = key

	# swpas with parents untill in its place.
	#as long as not in the top of the tree & parent > kid

	while (key_index > 0) and ( A[(key_index-1)/2] < A[key_index]):
		print A
		swap(A,key_index,(key_index-1)/2)

		# new key is in parent index
		key_index = (key_index-1)/2
	
	
# adds an element to the heap ///heappush
def max_heap_insert(A,key):

	# marks the last index (len-1)
	heap_size = len(A)

	# adds the smallest value possible
	A.append(float('-inf'))

	# calls heap_increase_key to find the location for the added key
	heap_increase_key (A, heap_size , key)
	

random_array = [random.randint(-10,10) for r in xrange(8)]

home_work_array = [39, 85, 85, 16, 49, 7, 49, 92, 76, 15, 21, 30, 29, 31, 28]

heap = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]

print heap_extrat_max([9,7,8,3,2,5,4])
print 