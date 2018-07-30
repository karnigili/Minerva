# Directions:
# -----------
#
# You and your friends rented a bus and have gotten lost.  This is because the
# person with the map was sitting at the back of the bus and gave directions to
# the person in front of them.  This person then told the person in front of them.
# Eventually the directions reached the driver in the front.  Occasionally someone
# would make a mistake, and they would either:
#  - leave out a step,
#  - add a step,
#  - give the wrong instruction.
#
# Each direction was either "Straight", "Left", or "Right".
#
# You and you friends would like to figure out who made the most mistakes.
# Fortunately everyone wrote down the instructions they gave. Write a function
# ('blame') to figure out who is to blame.
#
# directions = [('map', 'SSSRSSLRLS'), ('jane', 'SSRSLSLSSRLS'), ('jayna',
#                'SRSLSLSRLS'), ('jomo', 'SRSLRRSLSRSLSR')]
#
# >>> print(blame(directions))
# 'jayna'


def total_mistakes (st1, st2):
	
	mistakes = {}  # (indexes_st1,indexes_st2) : value


	def count_mistakes (st1, start_st1, st2, start_st2, mistakes):
		

		if len(st1) - start_st1 == 0 : 
			return len(st2) - start_st2

		if len(st2) - start_st2 == 0 :
			return len(st1) - start_st1

		if (start_st1, start_st2) in mistakes:
			return mistakes[(start_st1, start_st2)]

		if st1[start_st1] == st2[start_st2]:
			return count_mistakes(st1, start_st1+1, st2, start_st2+1, mistakes)

		else:
			value = 1 + min(count_mistakes(st1, start_st1+1, st2, start_st2, mistakes), # insertion
				count_mistakes(st1, start_st1, st2, start_st2+1, mistakes), # deletion
				count_mistakes(st1, start_st1+1, st2, start_st2+1, mistakes)) # modification

		mistakes[(start_st1, start_st2)] =  value

		return value

	return count_mistakes (st1, 0, st2, 0, mistakes)

# print total_mistakes('aa','aa')
directions = [('map', 'SSSRSSLRLS'), ('jane', 'SSRSLSLSSRLS'), ('jayna','SRSLSLSRLS'), ('jomo', 'SRSLRRSLSRSLSR')]

def blame(directions):
	mistakes_per_friends = {}

	for friend_index in range(len(directions)-1):
		
		mistakes = total_mistakes(directions[friend_index][1], directions[friend_index + 1][1])
		
		mistakes_per_friends[directions[friend_index+1][0]] = mistakes 


	print mistakes_per_friends


blame(directions)

