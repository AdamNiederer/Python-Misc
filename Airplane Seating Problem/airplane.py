#!/usr/bin/python3

import random

# Author: Joshua Li
# Description:
# 	I was posed the following problem in a lecture, and
#	decided to make a simulation to solve it.

'''
Problem:

There are 100 seats in an airplane and 100 passengers. All
of the passengers are assigned their own random seat. However,
the first passenger disobeys this and takes a random seat.
All subsequent passengers, one at a time, takes their assigned
seat if it is vacant. If it is already occupied, then they will
take a random seat.

Once 99 passengers have taken seats in this manner, you are the
only passenger left who needs to take a seat. What is the probability
that your seat is vacant?

'''

def run_simulation():
	assigned_seats = list(range(100))
	random.shuffle(assigned_seats)
	passengers = list(enumerate(assigned_seats)) 
	# passenger seat assignment complete

	all_seats = [False for i in range(100)] # create seats
	passengers.pop() 
	all_seats[random.randint(0, 99)] = True
	#  first passenger has taken random seat

	while(len(passengers) > 1):
		p = passengers.pop() 
		if(not all_seats[p[1]]): # if assigned seat unoccupied
			all_seats[p[1]] = True # then occupy it
		else:
			# else take a random seat that is unoccupied
			seat = random.randint(0, 99)
			while(all_seats[seat]): # if random seat is occupied,
				seat = random.randint(0, 99) # reroll
			all_seats[seat] = True # occupy the random vacant seat
	
	you = passengers.pop()
	return (all_seats.index(False) == you[1])

if __name__ == "__main__":
	num_sessions = 100 # each session runs the simulation some # of times
	num_runs = 1000 # times to repeat simulation per session
	num_successes = 0 # keep track of successes

	for i in range(num_sessions):
		for j in range(num_runs):
			if run_simulation():
				num_successes += 1
		print(num_successes/num_runs) # success ratio in current session
		num_successes = 0 # reset session