import random
import string
import numpy as np
import time

# crosswords

def DAT_initialize (DAT, n):
	for _ in range(n):
		DAT.append(None)

def DAT_insert (DAT, index, answer):
	DAT[index] = answer

def DAT_delete (DAT, index):
	DAT[index] = None


DAT_up = []
DAT_across = []


# SSN

# chained hash


def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def empty_hash_table(N):
    return [[] for n in range(N)]


def add_to_hash_table(hash_table, item, hash_function):
	N = len(hash_table)

	slot = hash_function(item)
	mod_slot = slot % N

	hash_table[mod_slot].append(item)
	# else:
	# 	print slot
    
	return hash_table


def contains(hash_table, item, hash_function):
    # N = len(hash_table)
    
    slot = hash_function(item)

    for element in hash_table[slot]:
    	if element == item :
    		return True

    # return False

def remove(hash_table, item, hash_function):
    if not contains(hash_table, item, hash_function):
        raise ValueError()

    slot = hash_function(item)

    hash_function[slot].remove(item)


    return hash_table


def hash_str1(string):
	# sum of ord of all chrs
    ans = 0
    for chr in string:
        ans += ord(chr)
    return ans


def hash_str2(string):
	# com power of ord of all chrs
    ans = 0
    for chr in string:
        ans = ans ^ ord(chr)
    return ans


def hash_str3(string):
    ans = 0
    for chr in string:
        ans = ans * 128 + ord(chr)
    return ans


def hash_str4(string):
	# first letter seed
	# 32 bit random
    random.seed(ord(string[0]))

    return random.getrandbits(32)

def collision_count (hash_table):
	sum_coll = 0

	for bucket in range(len(hash_table)):
		if len(hash_table[bucket]) > 1:

			sum_coll += len(hash_table[bucket])-1


	return sum_coll
	

def avg_bucket_len (hash_table):

	elements_per_bucket = []

	for bucket in range(len(hash_table)):
		if len(hash_table[bucket]) > 0:

			elements_per_bucket.append(len(hash_table[bucket]))

	if elements_per_bucket != []:
		return elements_per_bucket, np.mean(elements_per_bucket)
	else:
		return elements_per_bucket, 0




#create words
words = []
N = 100000 
word_len = 10

for _ in range(N):
	words.append(randomword(word_len))
# print words	

# chain hash_tables
slots = 5000



# HT1 = empty_hash_table(slots)
# HT2 = empty_hash_table(slots)
# HT3 = empty_hash_table(slots)
# HT4 = empty_hash_table(slots)

# for word in words:
# 	HT1 = add_to_hash_table(HT1, word, hash_str1)
# 	HT2 = add_to_hash_table(HT2, word, hash_str2)
# 	HT3 = add_to_hash_table(HT3, word, hash_str3)
# 	HT4 = add_to_hash_table(HT4, word, hash_str4)
# # print HT1

# print 'avg elements:'
# avg1 = avg_bucket_len(HT1)
# avg2 = avg_bucket_len(HT2)
# avg3 = avg_bucket_len(HT3)
# avg4 = avg_bucket_len(HT4)
# print "hash table 1 {}".format(avg1[1])
# print "hash table 2 {}".format(avg2[1])
# print "hash table 3 {}".format(avg3[1])
# print "hash table 4 {}".format(avg4[1])


# print "colls"
# print collision_count(HT1)
# print collision_count(HT2)
# print collision_count(HT3)
# print collision_count(HT4)

# print 'hash table shape'
# print "hash table 1 {}".format(avg1[0])
# print "hash table 2 {}".format(avg2[0])
# print "hash table 3 {}".format(avg3[0])
# print "hash table 4 {}".format(avg4[0])



