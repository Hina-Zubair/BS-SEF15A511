#!usr/bin/env python
processes={}
burst_time=[]
arrival_time=[]
total=0
priority=[]
n = input("Enter the number of processes:")
for i in range (0,n):
	prior_no=input("Priority number:")
	priority.append(prior_no)
	ar_time=input("Arrival Time:")
	arrival_time.append(ar_time)
	br_time=input("Burst Time:")
	burst_time.append(br_time)
	processes[priority[i]] = [i+1 , arrival_time[i] , burst_time[i]]

print "Priority#	Arrival Time           Burst Time"
for i in range (0,n):
	print priority[i] , "\t\t\t" , arrival_time[i], "\t\t\t" , burst_time[i] 
priority.sort()
total = processes.get(priority[0])[1]
min = total
if(total>0):
	print '0 -------' , total 
for i in range (0,n):
	total = total + processes.get(priority[i])[2]
	print min , "________" , total
	min = total
