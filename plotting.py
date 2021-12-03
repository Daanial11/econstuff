import sys
import math
import random
import csv
import matplotlib.pyplot as plt
import numpy as np


# Use this to plot trades of a single experiment
def plot_trades(trial_id):
    prices_fname = trial_id + '_transactions.csv'
    x = np.empty(0)
    y = np.empty(0)
    with open(prices_fname, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            time = float(row[1])
            price = float(row[2])
            x = np.append(x,time)
            y = np.append(y,price)

    plt.plot(x, y, 'x', color='black') 
    
# Use this to run an experiment n times and plot all trades
def n_runs_plot(n, trial_id, start_time, end_time, traders_spec, order_sched):
    x = np.empty(0)
    y = np.empty(0)

    for i in range(n):
        trialId = trial_id + '_' + str(i)
        tdump = open(trialId + '_avg_balance.csv','w')

        market_session(trialId, start_time, end_time, traders_spec, order_sched, tdump, True, False)
        
        tdump.close()

        with open(trialId + '_transactions.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    plt.plot(x, y, 'x', color='black');

# !!! Don't use on it's own   
def getorderprice(i, sched, n, mode):
    pmin = min(sched[0][0], sched[0][1])
    pmax = max(sched[0][0], sched[0][1])
    prange = pmax - pmin
    stepsize = prange / (n - 1)
    halfstep = round(stepsize / 2.0)

    if mode == 'fixed':
        orderprice = pmin + int(i * stepsize)
    elif mode == 'jittered':
        orderprice = pmin + int(i * stepsize) + random.randint(-halfstep, halfstep)
    elif mode == 'random':
        if len(sched) > 1:
            # more than one schedule: choose one equiprobably
            s = random.randint(0, len(sched) - 1)
            pmin = min(sched[s][0], sched[s][1])
            pmax = max(sched[s][0], sched[s][1])
        orderprice = random.randint(pmin, pmax)
    return orderprice    

# !!! Don't use on it's own
def make_supply_demand_plot(bids, asks):
    # total volume up to current order
    volS = 0
    volB = 0

    fig, ax = plt.subplots()
    plt.ylabel('Price')
    plt.xlabel('Quantity')
    
    pr = 0
    for b in bids:
        if pr != 0:
            # vertical line
            ax.plot([volB,volB], [pr,b], 'r-')
        # horizontal lines
        line, = ax.plot([volB,volB+1], [b,b], 'r-')
        volB += 1
        pr = b
    if bids:
        line.set_label('Demand')
        
    pr = 0
    for s in asks:
        if pr != 0:
            # vertical line
            ax.plot([volS,volS], [pr,s], 'b-')
        # horizontal lines
        line, = ax.plot([volS,volS+1], [s,s], 'b-')
        volS += 1
        pr = s
    if asks:
        line.set_label('Supply')
        
    if bids or asks:
        plt.legend()
    plt.show()

# Use this to plot supply and demand curves from supply and demand ranges and stepmode
def sup_dem(seller_num, sup_ranges, buyer_num, dem_ranges, stepmode):
    asks = []
    for s in range(seller_num):
        asks.append(getorderprice(s, sup_ranges, seller_num, stepmode))
    asks.sort()
    bids = []
    for b in range(buyer_num):
        bids.append(getorderprice(b, dem_ranges, buyer_num, stepmode))
    bids.sort()
    bids.reverse()
    
    make_supply_demand_plot(bids, asks) 

# plot sorted trades, useful is some situations - won't be used in this worksheet
def in_order_plot(trial_id):
    prices_fname = trial_id + '_transactions.csv'
    y = np.empty(0)
    with open(prices_fname, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            price = float(row[2])
            y = np.append(y,price)
    y = np.sort(y)
    x = list(range(len(y)))

    plt.plot(x, y, 'x', color='black')


def profit_per_trader_plot(duration):

    PRZI_y = np.empty(0)
    ZIP_y = np.empty(0)
    with open('avg_balance.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            PRZI_y = np.append(PRZI_y, float(row[7]))
            ZIP_y = np.append(ZIP_y, float(row[11]))
            if(int(row[1]) == int(duration)):
                break

    x = list(range(len(PRZI_y)))
    
    plt.plot(x, PRZI_y, label = "PRSH")
    plt.plot(x, ZIP_y, label = "ZIP")

    plt.legend()



def get_average_across_trails(numTraders, duration, numTrails, k):

    traderProfitTuples = {}
    with open('avg_balance.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if(int(row[1]) == int(duration)):
                for i in range(numTraders):
                    if str(row[4 + (4*i)]) in traderProfitTuples:
                        traderProfitTuples[str(row[4 + (4*i)])] = traderProfitTuples[str(row[4 + (4*i)])] + float(row[7 + (4*i)]) 
                    else:
                        print(4 + (4*i))
                        print(7 + (4*i))
                        traderProfitTuples[str(row[4 + (4*i)])] = float(row[7 + (4*i)]) 


    for name, profit in traderProfitTuples.items():
        traderProfitTuples[name] = round(profit / numTrails, 1)

    f = open("data/8n2.txt", "a")
    f.write("average profit per trader over: " + str(numTrails) + " trails |" " trail duration: " + str(duration) + "k= " + str(k))
    f.write(str(traderProfitTuples) + " k= " + str(k) + "\n")
    f.close
    
    print(traderProfitTuples)  

