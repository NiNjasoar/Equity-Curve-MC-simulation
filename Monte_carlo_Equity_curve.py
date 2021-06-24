import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style



#Edit parameters here
accuracy = 55
profit_stop =1

num_simulations = 60
num_days = 300
risk_per_trade = 0.01
starting_equity = 100

simulation_df = pd.DataFrame()

for x in range(num_simulations):
  
    equity_curve = [starting_equity]*num_days
    
    for y in range(num_days):
        if y == num_days-1:
            break
        profit = profit_stop*risk_per_trade if  np.random.randint(100) < accuracy else -risk_per_trade
        equity_curve[y+1] = equity_curve[y] * (1 + profit)
    
    simulation_df[x] = equity_curve

style.use('ggplot')
fig = plt.figure()
fig.suptitle('Equity curve for Accuracy: ' + str(accuracy) + ' and Profit to Stop: ' + str(profit_stop))
plt.plot(simulation_df)
plt.ylabel("Returns(%)")
plt.xlabel('Trades')
plt.show()