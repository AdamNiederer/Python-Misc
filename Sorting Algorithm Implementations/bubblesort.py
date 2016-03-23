# Joshua Li
# A Python implementation and step-by-step demonstration of bubble sort, with runtime analysis.

from sorttools import *

# Bubble sort is O(n^2) time complexity and is an in-place sort, like selection sort.
# But, it can recognize and skip over sorted data! So for data that is already sorted,
# one O(N) pass is sufficient to verify that it is sorted already.

# It's a very well known quadratic sort, but its primary drawback is that swapping takes time
# (three re-assignments) and bubble sort is based on swapping.

def bubble_sort(nums):
	for i in range(len(nums)-1, 0, -1):
		for j in range(i):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
	return nums

def _bubble_sort_with_runtime(nums):
	from time import time
	start_time = time()
	sorted_nums = bubble_sort(nums)
	runtime = time() - start_time
	print("Original List Size: {} elements".format(len(nums)))
	print("Bubble Sort runtime: {} seconds".format(runtime))
	print("List is actually sorted: " + ["No", "Yes"][is_sorted(sorted_nums)])

def _bubble_sort_with_step_analysis(nums):
	print("\nStarting list: ", nums, '\n')
	for i in range(len(nums)-1, 0, -1):
		print("Searching for out of order pairs between indices 0 - {}\n".format(i))
		for j in range(i):
			if nums[j] > nums[j+1]:
				print("Found unordered pair [{}, {}] that spans indices ({} - {})"
					.format(nums[j], nums[j+1], j, j+1))
				nums[j], nums[j+1] = nums[j+1], nums[j]
				print("Swapping.")
				print("List is now: ", nums, '\n')
	print("Sorted list: ", nums)

if __name__ == "__main__":
	### Just the sort:
	nums = generate_randoms()
	print("Original: ", nums)
	print("Sorted: ", bubble_sort(nums))

	### Step analysis:
	#nums = generate_randoms()
	#_bubble_sort_with_step_analysis(nums)

	### Runtime analysis:
	#nums = generate_randoms(1000)
	#_bubble_sort_with_runtime(nums)
	#_bubble_sort_with_runtime(sorted(nums))