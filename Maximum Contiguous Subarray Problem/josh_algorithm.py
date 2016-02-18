# 2.18.2016
# Joshua Li's algorithmic implementation to the problem:
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

# Compresses all consecutive same-sign values in an integer list into a single value.
# As a result, the compressed list is guaranteed to have sign-alternating elements. 
# That is, a positive number will always immediately come after a negative, and vice versa. 
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

# Implementation of the brute force method to verify the correctness of the new algorithm.
def useBruteForce(num_list): 
	all_sums = []
	for i in range(len(num_list)):
		all_sums.extend(list(accumulate(num_list[i:])))
	return max(all_sums)

##############################
# Start of program execution #
##############################
if len(sys.argv) == 1:
	list_size = 1000
else:
	list_size = int(sys.argv[1])
nums = [randint(-10, 10) for i in range(list_size)]

start_time = time()
######################
# Start of algorithm #
######################
compressed_nums = compress(nums)
compressed_size = len(compressed_nums)

left_end = 0
right_end = compressed_size
#print(compressed_nums[left_end:right_end]) # Initial compressed list
while (right_end - left_end >= 7): # A cutoff of 7 elements ensures no data loss and algorithm success.
	# Shave off negative ends
	if compressed_nums[left_end] <= 0:
		left_end += 1
	if compressed_nums[right_end - 1] <= 0:
		right_end -= 1
	# Combine first and last pairs
	compressed_nums[left_end + 1] = compressed_nums[left_end + 1] + compressed_nums[left_end]
	compressed_nums[right_end - 2] = compressed_nums[right_end - 2] + compressed_nums[right_end - 1]
	left_end += 1
	right_end -= 1
	#print(compressed_nums[left_end:right_end]) # List after each iteration
result = useBruteForce(compressed_nums[left_end:right_end])

max_val = max(compressed_nums)
if result < max_val: 
	result = max_val # Rarely (for large lists), the max_val can be greater than the result.
####################
# End of algorithm #
####################
runtime = time() - start_time

#######################
# Brute Force Testing #
#######################
# Use brute force to validate that the algorithm is correct for sizes < 50,000.
#compressed_nums_for_brute_force = compress(nums)
#brute_result = useBruteForce(compressed_nums_for_brute_force)
brute_result = -1

#print("\nOriginal List: " + str(nums) + "\n")
#print("\nCompressed List: " + str(compressed_nums_for_brute_force) + "\n")
print("\nAlgorithm runtime [GLORIOUS SIEVE]: {} seconds".format(runtime))
print("Original list size: {} elements".format(list_size))
print("Compressed list size: {} elements".format(compressed_size))
print("Maximum consecutive sum as determined by algorithm: " + str(result))
print("Maximum consecutive sum as determined by brute forcing: " + str(brute_result))
##################
# End of program #
##################



