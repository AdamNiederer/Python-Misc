from collections import Counter

# A quick midterm grade parser (professor posted everyone's grades lol).

with open("grades.txt", "r") as f:
	students = [l.split() for l in f.read().split("\n")]

midterms = dict(Counter([int(s[-3]) for s in students]))

for d in midterms:
	print(d, midterms[d])