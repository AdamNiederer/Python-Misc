#!/usr/bin/python3

import sys
from random import randint
from itertools import accumulate
from time import time

# Author: Joshua Li
# Description:
# 	A brute force implementation to the problem:
#	Given a list of numbers (-100 to 100), find the maximum sum
#	found in any contiguous subsequence of the list.

if __name__ == "__main__":
	if len(sys.argv) == 1:
		listsize = 1000
	else:
		listsize = int(sys.argv[1])

	nums = [randint(-100, 100) for i in range(listsize)]
	print("\nOriginal List: " + str(nums) + "\n")

	start = time()
	allsums = []
	for i in range(listsize):
		allsums.extend(list(accumulate(nums[i:])))
	result = max(allsums)

	print("Runtime: {} seconds".format(time() - start))
	print("Original list size: {} elements".format(listsize))
	print("Maximum consecutive sum: " + str(result))