#!usr/bin/env python
waiting_time=[]
burst_time=[]
arrival_time=[]
total=0
processes={}
avgwt=0
n = input("Enter the number of processes:")
for i in range (0,n):
	ar_time=input("Arrival Time:")
	arrival_time.append(ar_time)
	br_time=input("Burst Time:")
	burst_time.append(br_time)
	processes[arrival_time[i]] = [i,arrival_time[i] , burst_time[i]]

print "Arrival Time         Burst Time"
for i in range (0,n):
	print arrival_time[i],    "\t\t\t"       , burst_time[i]

total = processes.get(arrival_time[0])[1]
min = total
if(total>0):
	print "0 ......" , total 

for i in range (0,n):
	total = total + processes.get(arrival_time[i])[2]
        res=processes.get(arrival_time[i])[0]
        a_time=arrival_time[i]
        wt=min-a_time
        waiting_time.insert(res,wt)
	print min , "......" , total
	min = total
        avgwt=wt/n
print  "Waiting time"
for i in range(0,n):
     print waiting_time[i]
     print avgwt
