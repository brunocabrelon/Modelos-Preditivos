import MetaTrader5 as mt5
import pandas as pd
import matplotlib.pyplot as plt

mt5.initialize()

symbols =['WIN$', 'WDO$']

data = pd.DataFrame()

for i in symbols:
    rates = mt5.copy_rates_from_pos(i, mt5.TIMEFRAME_M15, 0, 100)
    data[i] = [y['close'] for y in rates]



mt5.shutdown()
print(data)
retornos = data.pct_change()

print(retornos)

corr = data.corr()

print(corr)

plt.figure (figsize=(10,10))
plt.imshow (corr, interpolation='none', aspect='auto')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation = 'vertical')
plt.yticks(range(len(corr)), corr.columns)
plt.suptitle("Mapa de Correlação", fontsize = 15, fontweight = 'bold')
plt.show()