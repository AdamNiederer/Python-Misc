#!/usr/bin/python3

from collections import Counter
from itertools import accumulate
import matplotlib.pyplot as plt

# Author: Joshua Li
# Description:
# 	A matplotlib-powered graphical visualization of CMPSC 122 2015-2016 grades,
#	up to midterm #2! Each line is a student and represents a running sum,
#	so it's like a race!

class Student:
	'''
	The format of the grades, as it stands now, is like this:
	IDNO P1 P2 P3 P4 P5 P6 P7 P8 P9 PA  PT H1 H2 H3 H4  HT  M1  M2 TOT Proj

	PT = sum (P1 + P2 + ... + PA); PT is the total recitation grade and since I will be doing a running
	sum, PT will be ignored
	HT = sum (H1 + ... + H4 + sometimes H5); I will remove HT since some students have H5 graded
	and some do not. As of 4/18/2016 this script is going to ignore H5 until everyone has those grades.

	I'm going to ignore TOT and Proj as well, as they are total/projected score.
	'''
	def __init__(self, grade_list):
		self.__id = grade_list[0]
		processed_grade_list = grade_list[1:-2] # we don't want ID or the last 2 entries (TOT and Proj)
		del processed_grade_list[10] # remove PT
		del processed_grade_list[14] # remove HT
		self.__grades = processed_grade_list

	def get_id(self):
		return self.__id

	def get_grades(self):
		return self.__grades

def get_ranking_report(s_id, student_list):
	student_list.sort(key = lambda s: sum(s.get_grades()), reverse=True)
	for s in enumerate(student_list, 1):
		if s[1].get_id() == s_id:
			ranking = s[0]
			break
	enrollment = len(student_list)
	percentile = 100 * ((enrollment-ranking+1) / enrollment)
	return "Student ID #{} is ranked {} out of {} total students (Percentile: {})".format(s_id, ranking, enrollment, percentile)

if __name__ == "__main__":
	target_id = int(input("Enter the last 4 digits of your PSU ID: ").strip())
	all_students = []
	with open("raw_grades.txt", "r") as f:
		students_raw = [l.split() for l in f.read().split("\n")] # split each line
	for s in students_raw:
		s = [int(g) if g != '--' else 0 for g in s] # int conversion and -- denotes no grade (0)
		all_students.append(Student(s)) # create new Student object
	for s in all_students:
		if s.get_id() == target_id:
			you = s # save for later
		else:
			plt.plot(list(accumulate(s.get_grades())), color="gray")
		#print(s.get_grades())
	try:
		plt.plot(list(accumulate(you.get_grades())), color="yellow", linewidth=1.5) # you are plotted last so other lines don't overlap
	except:
		exit("Unable to locate student with ID {}.".format(target_id))
	plt.suptitle(get_ranking_report(target_id, all_students), fontsize=20, fontweight='bold')
	plt.xlabel('Time')
	plt.ylabel('Total Grade Running Sum')
	plt.gca().set_axis_bgcolor("black")
	plt.show()