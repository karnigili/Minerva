import random

def maxsubarray_bf (array) :
	vmax = 0
	index = [0,0]
	for i in range (len(array)):
		for j in range (i, len(array)):
			if sum(array[i:j]) > vmax:
				vmax = sum(array[i:j])
				index[0], index[1] = i,j
	return vmax, index

def maxsubarray_dc (A,start,end):
	# print "split"
	# print A,start,end

	if end == start: # base case: only one element
		return (start, end, sum(A[start:end]))
	else:
		#split 
		mid = (start + end)/2 

		left_start,left_end,left_sum = maxsubarray_dc(A,start,mid)
		right_start,right_end,right_sum = maxsubarray_dc(A,mid+1,end)
		
		#merge 
		# print "merge"
		# print A,start,end
		print left_start,left_end,sum(A[left_start:left_end])
		print right_start,right_end,sum(A[right_start:right_end])

		if (left_sum >= right_sum ) :

			return left_start,left_end,sum(A[left_start:left_end])

		elif (right_sum > left_sum ) :

			return right_start,right_end,sum(A[right_start:right_end])


def x_maxsubarray_dc (A):
	
	
	start = 0
	end = len(A)
	mid = (start + end)/2 

	max_SA_one_side_values = maxsubarray_dc(A,start,end)

	current_max_sum = max_SA_one_side_values[2] # value of max

	current_index_start = max_SA_one_side_values[0]
	current_index_end = max_SA_one_side_values[1]

	if mid >= max_SA_one_side_values[0] : #maxSA is in the left side

		for j in range(mid+1,end): #run the right side from mid to end

			if current_max_sum +A[j] >current_max_sum :
				current_max_sum += A[j]
				current_index_end = j 

	if mid < max_SA_one_side_values[0] : #maxSA is in the right side

		for i in range(mid,start-1,-1): #run the left side, mid to start
			if current_max_sum +A[i] > current_max_sum :
				current_max_sum += A[i]
				current_index_start = i

		

	return (current_index_start,current_index_end,current_max_sum)




def incremental_max_subarray(x, mx):
	max_value = sum(mx)
	value_sum = 0

	for i in range(len(x),0,-1):
		
		if value_sum + x[i]:
			value_sum += x[i]

	if value_sum > max_value:
		return value_sum

	return max_value





random_array = [random.randint(-10,10) for r in xrange(6)]
print random_array
# print maxsubarray_bf(random_array)
print maxsubarray_dc(random_array,0,len(random_array))
 
