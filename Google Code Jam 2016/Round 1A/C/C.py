for i in range(int(input())):
	n = int(input())
	s = list(map(int, input().split()))
	pairs = list(enumerate(s, 1))
	print("Case #{}: {}".format(i+1, ''.join(list(map(str, pairs)))))
	# I have lost this battle...