import time
import random


def insertion_sort (A):
	count =0
	for j in range (1, len(A)): #iteration
			
		key= A[j] #saves the Js element
		position = j # and it's position 

		count += 2

		while position > 0 and A[position -1] >key: #not reached the begining & Ccurrent key is smaller than comparison 
			A[position]=A[position-1] # push bigger element 
			position=position -1 #check with the next (smaller) element
			
			count +=2
			count+=1

		A[position]=key # position key in its right position
		
		count +=1
		count +=1		

	return A,count

def bubble_sort(A):
	count = 0

	for i in range(len(A)):  #iterate 
		for k in range(len(A)-1,i,-1): # iterate (strat,stop,step) 
			if ( A[k] < A[k - 1] ): # if "last" element is bigger then previous one
				tmp = A[k] #swap
				A[k] = A[k-1]
				A[k-1] = tmp
				
				count += 3
				count += 1 
				count += 1
		count +=1

	return A,count
 
def selection_sort(A):
	count = 0 # basic number before iteration

	for i in range(len(A)): #iterate
		small = i #index for iterated
		
		count +=1
		
		for k in range(i+1,len(A)): #(start,stop)
			if A[k] < A[small]: # comparison
				small = k #assigning new small value
				
				count +=1
			
			count +=1
			count +=1
 		
 		tmp = A[small] #swap
		A[small] = A[i]
		A[i] = tmp
		
		count +=3
		count +=1


	return A, count

def shell_sort(lis):
    
    interval = len(lis)/2 #choosing interval size
    
    while (interval > 0): # the interval is about to decrease to 0 and then the loop stops
        for k in range(1, len(lis),interval): #in each interval we will run the insertion sort
            
            keep = lis[k]
            pos = k -1

            while pos >=0  and lis[pos] > keep:
                lis[pos+1] = lis[pos]
                pos = pos -1 

            lis[pos+1 ] = keep

        interval -= 1 #decrease the interval
           
       
    return lis

def time_calc (f,A):
	start_time = time.time()
	result = f(A)
	runtime = (time.time() - start_time)

	return  runtime


b = [random.randint(0,1000) for r in xrange(1000)]


print time_calc(shell_sort,b)
print time_calc(selection_sort,b)
