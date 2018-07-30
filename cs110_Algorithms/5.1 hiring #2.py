import random

#checks if list is sorted
def is_sorted (n):
	for index in range(1,len(n)):

		if n[index] < n[index-1]:
			return False 

	return True


def recursive_worst_sort (n):

	random.shuffle(n)

	# checks if by order, comaring each elemnt to its previous one
	# if even one is not by order the function runs again
	for index in range (1,len(n)):

		if n[index] < n[index-1]:
			return recursive_worst_sort (n)

	return n

	
def loop_worst_sort (n):
	# as long as it is not sorted keep shuffling 
	while not is_sorted(n) :

		random.shuffle(n)

		#when exitst the loop, return the list
	return n


t = [1,2,3,8,5,6,0]

# print loop_worst_sort(t)	




def median_finder (array, delta):
	#delta is between 0 to 0.5
	upper_bound = 50 + (delta/2.0)
	lower_bound = 50 - (delta/2.0)
	found = False
	counter =0

	while not found :
		counter +=1
		selcted_value = random.sample(array, 1)[0]

		# Amount of values above the selected value
		upper_position = len([index for index in range(len(array)) if array[index] > selcted_value ])
		
		# Amount of values below the selected value
		lower_position = len([index for index in range(len(array)) if array[index] < selcted_value ])
		
		# odd list length : looking for a middle point

		if len(array) % 2 !=0  and len(array)>1:
			lower_precentile = 100*lower_position/float(len(array)-1)
			upper_precentile = 100*upper_position/float(len(array)-1)

			if lower_bound <= lower_precentile <= upper_bound and lower_bound <= upper_precentile <= upper_bound:
				found = True
				# return selcted_value

			#if all numbers are the same
			if lower_precentile == upper_precentile ==0:
				found = True
				# return selcted_value

		# even list length : looking for onr of two a middle points		
		else:
			lower_precentile = 100 * lower_position/float(len(array))
			upper_precentile = 100 * upper_position/float(len(array))

			if (lower_bound <= lower_precentile <= upper_bound)  or (lower_bound <= upper_precentile <= upper_bound):
				found = True
				# return selcted_value

			#if all numbers are the same
			if lower_precentile == upper_precentile ==0:
				found = True
				# return selcted_value

	print counter
	return selcted_value






print median_finder([0,2,6,7,8,3,1,5,7,9,4,1], 0.5)









