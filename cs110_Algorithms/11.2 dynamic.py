

CURR = ['USD','EUR','GBP','CHF','CAD']

exchange_price = [[1, 0.741, 0.657, 1.061, 1.005],
[1.349, 1, 0.888, 1.433, 1.366],
[1.521, 1.126, 1, 1.614, 1.538],
[0.942, 0.698, 0.619, 1, 0.953],
[0.995, 0.732, 0.650, 1.049, 1]]


def relax (node, next_node, dist, weight = exchange_price, currencies = CURR):
	if dist[node] == None or dist[next_node] == None:
		dist[next_node] = weight[node][next_node]
	else:
		dist[next_node] = min( dist[node] + weight[node][next_node], dist[node])
	print dist

def BF (origin_index, weight = exchange_price, currencies = CURR):
	length = len(currencies)

	dist = [None] * length
	dist[origin_index] = 0

	for i in range(length-1):
		for u in range(length):
			for v in range(length):
				relax(u,v,dist)
	
	print 
	print dist
	# for u in range(length):


def shortest_path (origin_index, weight= exchange_price, currencies = CURR):
	length = len(currencies)

	origin = currencies[origin_index]
	dist = [float('inf')] *length
	dist[0] = 0

	for currency_index in range(1, length):

		for x in range(length-1):

			for y in range(length-1):

				dist[x] = min (dist[y], dist[x] + exchange_price[x][y])

	return dist

print BF(2)
