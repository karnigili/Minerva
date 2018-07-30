from  heapq import heappush, heappop, heapify
import random

#swap two elements in an array based on their indices
def swap (A, h, m):
	tmp = A[h]  
	A[h] = A[m]
	A[m]= tmp



# return the max value of the heap
def heap_maximum (A):
	return A[0]

# pop the max element out . maintain max heap 	
def heap_extrat_max (A):

	return heappop (A)

	

# adds an element to the heap
def max_heap_insert(A,key):

	return heappush(A, key)

random_array = [random.randint(-10,10) for r in xrange(8)]

home_work_array = [39, 85, 85, 16, 49, 7, 49, 92, 76, 15, 21, 30, 29, 31, 28]

heap = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]


max_heap_insert(heap,10)
print heap