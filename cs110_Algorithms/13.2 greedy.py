
import time, sys

# a = [[5,7],[1,4],[3,5],[0,6],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]]
a = sorted(a, key=lambda e:e[1])
# a.insert(0, [-1,0])
s, f = [e[0] for e in a], [e[1] for e in a]

# def recurisive_activity_selector(activites, starts, finishes, last_selected_activity, num_of_activites):  

#     next_activity = last_selected_activity 
#     while next_activity <= num_of_activites and starts[next_activity] < finishes[last_selected_activity]:
#         next_activity = next_activity + 1
#     if next_activity <= num_of_activites:
#         result = recurisive_activity_selector(activites, starts, finishes, next_activity, num_of_activites)
#         result.insert(0, activites[next_activity])
#         return result
#     else:
#         return []
    

# r = recurisive_activity_selector(a, s, f, 0, len(a)-1)
# print r

def hall_min(activites, starts, finishes, last_selected_activity, num_of_activites):
    halls = [[]] #stores the indexes of the activies

    for activity in activites:
        appended = False
        for room in halls:
            if len(room) == 0 or activity[0] > room[-1][1]: # if first room is empty
                appended = True
                room.append(activity)

        if not appended:
           halls.append([activity]) 

    return len(halls), halls
                


print hall_min(a, s, f, 0, len(a))

def knapsack(lim_W, wt, val):
    num_of_items = len(val)
    # 2d table t store options
    K = [[0 for x in range(lim_W + 1)] for x in range(num_of_items + 1)]
 
 
    for item in range(num_of_items + 1):
        for weight in range(lim_W + 1):
            if item == 0 or weight == 0:
                K[item][weight] = 0
            elif wt[item - 1] <= weight:
                K[item][weight] = max(val[item - 1] + K[item - 1][weight - wt[item - 1]],  K[item - 1][weight])
            else:
                K[item][weight] = K[item - 1][weight]
 
    return K[num_of_items][lim_W]
    # return K

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50


# print(knapsack(W, wt, val))

val_1 = [60, 100, 120]
wt_1 = [30, 20, 10]

def kanpsack_sorted (lim_W, wt, val):
    num_of_items = len(val)

    K = [[0 for x in range(lim_W + 1)] for x in range(num_of_items + 1)]

    for item in range(num_of_items + 1):
        for weight in range(lim_W + 1):
            if item == 0 or weight == 0:
                K[item][weight] = 0
            elif wt[item - 1] > weight:
                 K[item][weight] = K[item-1][weight]

            K[item][weight] = max(K[item-1][weight], K[item-1][weight - wt[item-1]] + val[item-1])


    return K[num_of_items][lim_W]
# print(kanpsack_sorted(W, wt, val))















