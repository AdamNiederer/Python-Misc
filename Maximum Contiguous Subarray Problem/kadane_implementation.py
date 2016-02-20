# 2.20.2016
# Quick implementation of Kadane's algorithm for the maximum subarray problem:
# 	Given a list of numbers (-100 to 100), find the maximum sum 
# 	found in any contiguous subsequence of the list.

# This script takes one argument in the command line,
# which is the size of the list of numbers.
# If no argument is specified, the default is 1000.

import sys
from random import randint
from itertools import accumulate
from time import time

########################
# Function definitions #
########################

# Kadane's beautiful algorithm.
def kadane(num_list):
    max_ending_here = max_so_far = 0
    for x in num_list:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Implementation of the brute force method to verify the correctness of the new algorithm.
def useBruteForce(num_list): 
	all_sums = []
	for i in range(len(num_list)):
		all_sums.extend(list(accumulate(num_list[i:])))
	return max(all_sums)

# Kadane's algorithm actually ends up being marginally slower after list compression. 
# Looks like compress's timespace can't make up for a halved list size.
def compress(input_list):
	result = []
	current_sum = 0
	for n in input_list:
		if n != 0:
			if (current_sum == 0) or ((current_sum < 0) == (n < 0)):
				current_sum += n
			else:
				result.append(current_sum)
				current_sum = n
	result.append(current_sum)
	return result

##############################
# Start of program execution #
##############################
if len(sys.argv) == 1:
	list_size = 1000
else:
	list_size = int(sys.argv[1])
nums = [randint(-10, 10) for i in range(list_size)]

start_time = time()
#compressed_nums = compress(nums)
result = kadane(nums)
runtime = time() - start_time

#######################
# Brute Force Testing #
#######################
# Use brute force to validate that the algorithm is correct for small list sizes.
#brute_result = useBruteForce(nums)
#brute_result = -1

#print("\nOriginal List: " + str(nums) + "\n")
print("\nAlgorithm runtime [KADANE'S]: {} seconds".format(runtime))
print("Original list size: {} elements".format(list_size))
#print("Compressed list size: {} elements".format(len(compressed_nums)))
print("Maximum consecutive sum as determined by algorithm: " + str(result))
#print("Maximum consecutive sum as determined by brute forcing: " + str(brute_result))
##################
# End of program #
##################



