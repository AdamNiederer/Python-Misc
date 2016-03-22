# Joshua Li
# A Python implementation and step-by-step demonstration of selection sort, with runtime analysis.

from sorttools import *

# Selection sort is O(n^2) time complexity and is an in-place sort.
# However, it cannot recognize already sorted data.
# It's probably the worst performing out of all the "quadratic" sorts.

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

def _selection_sort_with_runtime(nums):
	from time import time
	start_time = time()
	sorted_nums = selection_sort(nums)
	runtime = time() - start_time
	print("Original List Size: {} elements".format(len(nums)))
	print("Selection Sort runtime: {} seconds".format(runtime))
	print("List is actually sorted: " + ["No", "Yes"][is_sorted(sorted_nums)])

def _selection_sort_with_step_analysis(nums):
	print("\nStarting list: ", nums, '\n')
	size = len(nums)
	for i in range(size-1):
		min_index = i
		print("Searching for minimum between indices {} - {}".format(i, size-1))
		for j in range(i+1, size):
			if nums[j] < nums[min_index]:
				min_index = j
		print("Found minimum ({}) at index {}".format(nums[min_index], min_index))
		if min_index != i:
			print("Swapping minimum with element at index ({})".format(i))
			nums[i], nums[min_index] = nums[min_index], nums[i]
		else:
			print("No need to swap, minimum is at beginning of sublist already.")
		print("List is now: ", nums, '\n')
	print("Sorted list: ", nums)

if __name__ == "__main__":
	### Just the sort:
	#nums = generate_randoms()
	#print("Original: ", nums)
	#print("Sorted: ", selection_sort(nums))

	### Step analysis:
	#nums = generate_randoms()
	#_selection_sort_with_step_analysis(nums)

	### Runtime analysis:
	nums = generate_randoms(1000)
	_selection_sort_with_runtime(nums)