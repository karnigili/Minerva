import random
def swap (A, h, m):
	tmp = A[h]  
	A[h] = A[m]
	A[m]= tmp


def partition(A, start, end):
	#randomized 
	pivot_index = random.randint(start, end - 1)
	
	swap(A, pivot_index, start)


	pivot = A[start]

	#checks if all elemnts are the same
	if (all([A[i] == A[i + 1] for i in range(len(A) - 1)])) :
		return len(A)/2

	# the elemnt right after the pivot to the left
	mark_after_pivot = start + 1

	for test_current_index in range(start + 1, end):
		if A[test_current_index] < pivot:
			# if the current element is smaller , we swap it to right after the pivot and move the mark to the right
			swap(A, mark_after_pivot, test_current_index) 
			mark_after_pivot += 1 

	#moving the pivot to its place and position 
	swap(A, start, mark_after_pivot -1)
	
	#return the pivot position
	return mark_after_pivot -1 



def quicksort (A ,start=0, end=None, call_num=0):
	if end is None:
		end = len(A)

	if call_num == 500:
		print A
		return 

	if start < end:
		# pivot position
		pivot_position = partition(A, start, end)

		# print A[start:pivot_position], A[pivot_position], A[pivot_position + 1:end]
		# print
		call_num += 2
		quicksort(A, start, pivot_position, call_num)
		quicksort(A, pivot_position + 1, end, call_num)



def fast_det_quick_sort (A):
	if len(A) <= 1: return A
	return fast_det_quick_sort( [ smaller_than for smaller_than in A[1:] if smaller_than < A[0] ] )+ [ A[0] ]  +  fast_det_quick_sort( [ greater_than for greater_than in A[1:] if greater_than >= A[0] ] )



def fib(n):
	if n <= 0: 
		return 0
	if n == 1: 
		return 1 
	return fib(n-1) + fib(n-2) 



NUM_TESTS = 1

for _ in range(NUM_TESTS):
	arra = [random.randint(0, 100) for _ in range(100000)]
	
	quicksort(arra)
	assert(all([arra[i] <= arra[i + 1] for i in range(len(arra) - 1)]))

print 'Finished {num} tests succesfully'.format(num=NUM_TESTS)


