#!/usr/bin/python3

# Author: Joshua Li
# Description:
# 	A compilation of popular sorting algorithms implemented
#	in Python.

'''
TODO:

>	Add a generalized runtime recording function that can call any sorting algorithm
	on a list of size N and return the runtime.

'''

# === Selection Sort ===
# Runtime Complexity:
#	Average: O(n^2)
#	Best: O(n^2)
#	Worst: O(n^2)
def selection_sort(nums):
	size = len(nums)
	for i in range(size-1):
		min_index = i
		for j in range(i+1, size):
			if nums[j] < nums[min_index]:
				min_index = j
		if min_index != i:
			nums[i], nums[min_index] = nums[min_index], nums[i]
	return nums

# === Bubble Sort ===
# Runtime Complexity:
#	Average: O(n^2)
#	Best: O(n)
#	Worst: O(n^2)
def bubble_sort(nums):
	for i in range(len(nums)-1, 0, -1):
		for j in range(i):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
	return nums

if __name__ == "__main__":
	print("Script executed.")