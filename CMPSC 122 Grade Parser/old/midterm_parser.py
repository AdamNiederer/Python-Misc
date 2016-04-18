#!/usr/bin/python3

from collections import Counter

# Author: Joshua Li
# Description:
# 	A quick midterm grade parser (professor posted everyone's grades lol).

if __name__ == "__main__":
	with open("grades.txt", "r") as f:
		students = [l.split() for l in f.read().split("\n")]

	midterms = dict(Counter([int(s[-3]) for s in students]))

	for d in midterms:
		print(d, midterms[d])