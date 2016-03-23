# Just some helper functions here.
import random

def generate_randoms(size=10):
	return [random.randint(-100, 100) for i in range(size)]

# A simple check to validate that the algorithm works for larger lists.
def is_sorted(nums):
	for i in range(len(nums) - 1):
		if nums[i] > nums[i+1]:
			raise Exception("Found unsorted pair [{}, {}] that spans indices ({} - {})"
				.format(nums[i], nums[i+1], i, i+1))
			return False
	return True