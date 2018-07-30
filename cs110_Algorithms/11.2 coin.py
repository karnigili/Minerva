
def coin_game (array):

	# store visited combination
	mem_opt_values = {}

	#array of coins provided
	coins = array

	# recursive function
	def opt_coin(left, right, me_playing):

		# if visited, return a neutral value
	    if left >= right:
	        return 0

	    # if combination already visited, recall from array
	    if (left, right, me_playing) in mem_opt_values:
	        return mem_opt_values[(left, right, me_playing)]

	    # if it is my turn to play , choose the max option
	    if me_playing :

	    	
	        max_value = max(opt_coin(left + 1, right, False) + coins[left], opt_coin(left, right - 1, False) + coins[right])
	    	
	    # if the other plays, I get the 'leftover' assuming the other player plays by the same strategy ( I get the the min value)
	    else:
	        max_value = min(opt_coin(left + 1, right, True), opt_coin(left, right - 1, True))
	    	


	    # add visited combination to the mem array
	    mem_opt_values[(left, right, me_playing)] = max_value
	    

	    return max_value
 
	return opt_coin(0, len(coins)-1, True)



print coin_game([1,2,3,4])






