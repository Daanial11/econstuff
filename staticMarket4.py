import sys
import math
import random
import csv
import matplotlib.pyplot as plt
import numpy as np



import sys
import math
import random
import csv
import matplotlib.pyplot as plt
import numpy as np
from BSE import market_session
import plotting

start_time = 0.0
end_time = 0.0
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



# Use 'periodic' if you want the traders' assignments to all arrive simultaneously & periodically
#               'interval': 30, 'timemode': 'periodic'}



# run a sequence of trials, one session per trial

verbose = True

# n_trials is how many trials (i.e. market sessions) to run in total
n_trials = 20

# n_recorded is how many trials (i.e. market sessions) to write full data-files for
n_trials_recorded = 3



trial = 1

buyers_spec = [('PRSH',5), ('ZIP',5),('ZIC',5),('SNPR', 5),('GVWY', 5)]
sellers_spec = [('PRSH',5),('ZIP',5),('ZIC', 5),('SNPR', 5),('GVWY', 5)]

traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

for n in range(6):
    duration = float(5000)
    k = 2+(n*2)
    stepMode = 'random'
    tdump=open(f'data/static-market-test/{stepMode}/avg_balanceM4k{k}.csv','w')
    print(n)
    range1 = (200, 300)
    supply_schedule = [{'from': start_time, 'to': duration, 'ranges': [range1], 'stepmode': stepMode}
                    ]

    range2 = (200, 300)
    demand_schedule = [{'from': start_time, 'to': duration, 'ranges': [range2], 'stepmode': stepMode}
                    ]

    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': 30, 'timemode': 'periodic'}
    for i in range(n_trials):

            if i > n_trials_recorded:
                dump_all = False
            else:
                dump_all = True

            market_session(str(i+1), start_time, duration, traders_spec, order_sched, tdump, dump_all, verbose, 2+(n*2))
            tdump.flush()

        

    #plotting.get_average_across_trails(len(buyers_spec), duration, n_trials, 2+(n*2), "M4", 3)      
    tdump.close()
