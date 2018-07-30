import random
# sorts and merges
def merge(leftside, rightside):

    # creates an emty new array and sets the indices to zero
    sorted_array = []
    i , j = 0 , 0 

    # iterates through both sides and adds the sorted elements to the new array
    while i < len (leftside) and j < len (rightside):
        if leftside[i] <= rightside [j]:
            sorted_array.append(leftside[i])
            i += 1
        else:
            sorted_array.append(rightside[j])
            j += 1
            
    # adds the sorted subarray to the main array
    sorted_array += leftside[i:]
    sorted_array += rightside[j:]
    #print status
    print "merge "
    print sorted_array
    #return the main array
    return sorted_array 


def mergesort(array):
    print "split "
    print array
    if len(array) <= 1:
        return array
    middle = len(array) / 2

    return merge(mergesort(array[:middle]), mergesort(array[middle:]))



random_array = [random.randint(0,100) for r in xrange(10)]

mergesort(random_array)

