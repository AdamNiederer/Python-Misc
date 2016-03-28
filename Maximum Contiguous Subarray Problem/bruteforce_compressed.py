#!/usr/bin/python3

import sys
from random import randint
from itertools import accumulate
from time import time

# Author: Joshua Li
# Description:
# 	An improved brute force implementation to the problem:
#	Given a list of numbers (-100 to 100), find the maximum sum
#	found in any contiguous subsequence of the list.

#Compresses all consecutive same-sign values in an integer list into a single value.
def compress(input_list):
	result = []
	current_sum = 0
	for n in input_list:
		if (current_sum == 0) or ((current_sum < 0) == (n < 0)):
			current_sum += n
		else:
			result.append(current_sum)
			current_sum = n
	result.append(current_sum)
	return result

if __name__ == "__main__":
	if len(sys.argv) == 1:
		list_size = 1000
	else:
		list_size = int(sys.argv[1])
	nums = [randint(-10, 10) for i in range(list_size)]

	# Start of algorithm
	start_time = time()
	compressed_nums = compress(nums)
	all_sums = []
	for i in range(len(compressed_nums)):
		all_sums.extend(list(accumulate(compressed_nums[i:])))
	result = max(all_sums)
	runtime = time() - start_time
	#End of algorithm

	print("\nOriginal List: " + str(nums) + "\n")
	print("\nCompressed List: " + str(compressed_nums) + "\n")
	print("Runtime: {} seconds".format(runtime))
	print("Original list size: {} elements".format(list_size))
	print("Compressed list size: {} elements".format(len(compressed_nums)))
	print("Maximum consecutive sum: " + str(result))