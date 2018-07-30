
import random

#swap two elements in an array based on their indices
def swap (A, h, m):
	tmp = A[h]  
	A[h] = A[m]
	A[m]= tmp

# creates heaps 
def build_max_heap (A, heap_size):

	for i in range(heap_size/2 ,-1,-1) : #iterates on a layer in the heap

		max_heapify (A,i,heap_size) #"sort" the sub heap for each element

# keeps the heap in order (max) by comparing parent element to its 'kids'
def max_heapify (A,root, heap_size):
	# defines the roots kids (left/right)
	l= 2*root +1
	r= 2*root +2
	largest = root

	#checks which is the largest elemnt
	if (l < heap_size) and (A[l] > A[root]):
		largest = l
	
	if (r < heap_size) and (A[r] > A[largest]):
		largest = r
	
	#moves the largest elemnt to the top
	if largest != root:
		swap(A,root,largest)
		max_heapify(A, largest, heap_size)


def build_min_heap (A, heap_size):

	for i in range(heap_size/2 ,0,-1) : #iterates on a layer in the heap

		min_heapify (A,i,heap_size) #"sort" the sub heap for each element

def min_heapify (A,root, heap_size):
	# defines the roots kids (left/right)
	l= 2*root +1
	r= 2*root +2
	smallest = root

	#checks which is the smallest elemnt
	if (l <= heap_size-1) and (A[l] < A[root]):
		smallest = l
	
	if (r <= heap_size-1) and (A[r] < A[smallest]):
		smallest = r
	
	#moves the smallest elemnt to the top
	if smallest != root:
		swap(A,root,smallest)
		min_heapify(A, smallest, heap_size)

# sorting an array using hepsort
def heapsort (A):
	print "given array : "
	print A
	build_max_heap (A,len(A))
	for i in range(len(A)-1, 0, -1):  #iterates through the array, from end (bottom) to beggining (top)
		
		max_heapify (A, 0, i+1)
		swap(A,0,i)
	print "sorted array: "
	print A



random_array = [random.randint(-10,10) for r in xrange(8)]
home_work_array = [39, 85, 85, 16, 49, 7, 49, 92, 76, 15, 21, 30, 29, 31, 28]
heapsort(home_work_array)


