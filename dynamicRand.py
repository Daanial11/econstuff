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

  # supply_schedule = [ {'from':start_time, 'to':duration/3, 'ranges':[range1], 'stepmode':'fixed'},
    #                     {'from':duration/3, 'to':2*duration/3, 'ranges':[range2], 'stepmode':'fixed'},
    #                     {'from':2*duration/3, 'to':end_time, 'ranges':[range1], 'stepmode':'fixed'}
    #                   ]

trial = 1

buyers_spec = [('PRSH',5), ('ZIP',5),('ZIC',5),('SNPR', 5),('GVWY', 5)]
sellers_spec = [('PRSH',5),('ZIP',5),('ZIC', 5),('SNPR', 5),('GVWY', 5)]

traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

for n in range(6):
    duration = float(5000)
    k = 2+(n*2)
    stepMode = 'random'
    tdump=open(f'data/dynamic-market-test/{stepMode}/avg_balancek{k}.csv','w')
    print(n)
    Srange1 = (75, 200)
    Srange2 = (130, 175)
    Srange3 = (75, 200)
    Srange4 = (200, 300)
    supply_schedule = [{'from': start_time, 'to': duration/4, 'ranges': [Srange1], 'stepmode': stepMode},
                        {'from': duration/4, 'to': duration/2, 'ranges': [Srange2], 'stepmode': stepMode},
                        {'from': duration/2, 'to': duration*(3/4), 'ranges': [Srange3], 'stepmode': stepMode},
                        {'from': duration*(3/4), 'to': duration, 'ranges': [Srange4], 'stepmode': stepMode}
                    ]

    Drange1 = (75, 200)
    Drange2 = (75, 200)
    Drange3 = (130, 175)
    Drange4 = (200, 300)
    demand_schedule = [{'from': start_time, 'to': duration/4, 'ranges': [Drange1], 'stepmode': stepMode},
                        {'from': duration/4, 'to': duration/2, 'ranges': [Drange2], 'stepmode': stepMode},
                        {'from': duration/2, 'to': duration*(3/4), 'ranges': [Drange3], 'stepmode': stepMode},
                        {'from': duration*(3/4), 'to': duration, 'ranges': [Drange4], 'stepmode': stepMode}
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
    
        

    #plotting.get_average_across_trails(len(buyers_spec), duration, n_trials, 2+(n*2), "M1", 1)      
    tdump.close()
