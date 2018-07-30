### Did not get this code to run the wanted results but would love to get some feedback 

from query_data import *
import matplotlib.pyplot as plt
from init_db import *


if __name__ == "__main__":
    # n_test = np.logspace(1,3,3)
    n_test =[1, 10, 100]

    # queries = [top_five_ofices, top_five_agents, commision_per_agent, avg_market_days, avg_price, top_zips]
    queries=[commision_per_agent, avg_market_days, avg_price]
    
    times = {q.__name__:[] for q in queries}

    for n in n_test:
        print n
        init(int(n))

        for query in queries:

            avg_time_list = []
            for test in range(5):
                avg_time_list.append(time_it(query).microseconds)

            
            times[query.__name__].append(np.mean(avg_time_list))
      
        
    print times
    for time in times:
        plt.plot(n_test, times[time], label = time)
        
    
    plt.show()
