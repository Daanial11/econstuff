import sys
import math
import random
import csv
import matplotlib.pyplot as plt
import numpy as np
from BSE import market_session
import plotting

start_time = 0.0
end_time = 1000
duration = end_time - start_time


# schedule_offsetfn returns time-dependent offset, to be added to schedule prices
def schedule_offsetfn(t):

    pi2 = math.pi * 2
    c = math.pi * 3000
    wavelength = t / c
    gradient = 100 * t / (c / pi2)
    amplitude = 100 * t / (c / pi2)
    offset = gradient + amplitude * math.sin(wavelength * t)
    return int(round(offset, 0))


range1 = (50, 150)
supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [range1], 'stepmode': 'fixed'}
                    ]

range2 = (50, 150)
demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [range2], 'stepmode': 'fixed'}
                    ]

order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': 30, 'timemode': 'periodic'}
# Use 'periodic' if you want the traders' assignments to all arrive simultaneously & periodically
#               'interval': 30, 'timemode': 'periodic'}



# run a sequence of trials, one session per trial

verbose = True

# n_trials is how many trials (i.e. market sessions) to run in total
n_trials = 20

# n_recorded is how many trials (i.e. market sessions) to write full data-files for
n_trials_recorded = 3



trial = 1

buyers_spec = [('PRSH',1),('SNPR',5)]
sellers_spec = [('SNPR',6)]

traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

for n in range(2,3):
    tdump=open('avg_balance.csv','w')
    print(n)
    for i in range(n_trials):

            if i > n_trials_recorded:
                dump_all = False
            else:
                dump_all = True

            market_session(str(i+1), start_time, end_time, traders_spec, order_sched, tdump, dump_all, verbose, 2+(n*2))
            tdump.flush()

        

    plotting.get_average_across_trails(len(buyers_spec), duration, n_trials, 2+(n*2))      
    tdump.close()

buyers_spec = [('PRSH',1),('ZIP',5)]
sellers_spec = [('ZIP',6)]

traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}    

for n in range(2,3):
    tdump=open('avg_balance.csv','w')
    print(n)
    for i in range(n_trials):

            if i > n_trials_recorded:
                dump_all = False
            else:
                dump_all = True

            market_session(str(i+1), start_time, end_time, traders_spec, order_sched, tdump, dump_all, verbose, 2+(n*2))
            tdump.flush()

        

    plotting.get_average_across_trails(len(buyers_spec), duration, n_trials, 2+(n*2))      
    tdump.close()

buyers_spec = [('PRSH',1),('ZIC',5)]
sellers_spec = [('ZIC',6)]

traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}    

for n in range(2,3):
    tdump=open('avg_balance.csv','w')
    print(n)
    for i in range(n_trials):

            if i > n_trials_recorded:
                dump_all = False
            else:
                dump_all = True

            market_session(str(i+1), start_time, end_time, traders_spec, order_sched, tdump, dump_all, verbose, 2+(n*2))
            tdump.flush()

        

    plotting.get_average_across_trails(len(buyers_spec), duration, n_trials, 2+(n*2))      
    tdump.close()


buyers_spec = [('PRSH',1),('GVWY',5)]
sellers_spec = [('GVWY',6)]

traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}    

for n in range(2,3):
    tdump=open('avg_balance.csv','w')
    print(n)
    for i in range(n_trials):

            if i > n_trials_recorded:
                dump_all = False
            else:
                dump_all = True

            market_session(str(i+1), start_time, end_time, traders_spec, order_sched, tdump, dump_all, verbose, 2+(n*2))
            tdump.flush()

        

    plotting.get_average_across_trails(len(buyers_spec), duration, n_trials, 2+(n*2))      
    tdump.close()    



buyers_spec = [('ZIP',1),('PRSH',5)]
sellers_spec = [('PRSH',6)]

traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}    

for n in range(2,3):
    tdump=open('avg_balance.csv','w')
    print(n)
    for i in range(n_trials):

            if i > n_trials_recorded:
                dump_all = False
            else:
                dump_all = True

            market_session(str(i+1), start_time, end_time, traders_spec, order_sched, tdump, dump_all, verbose, 2+(n*2))
            tdump.flush()

        

    plotting.get_average_across_trails(len(buyers_spec), duration, n_trials, 2+(n*2))      
    tdump.close()     

    




tdump.close()
