import matplotlib.pyplot as plt
import numpy as np

file = open("BTC.csv")
dict = {}
list = []
avglist = []
for line in file:
    line = line.strip().split(",")
    avg = (float(line[1]) + float(line[2]) + float(line[3]) + float(line[4]) + float(line[5]))/5
    list.append(float(line[5]))
    avglist.append(avg)
    #dict[line[0]] = avg

t = np.linspace(0,300,6)
prices = np.array(list)
plt.plot(prices)
plt.xlabel("Work Week")
plt.ylabel("Closing Price")
plt.title("Bitcoin Prices")

window = 3
average_data = []
for ind in range(len(avglist) - window + 1):
    average_data.append(np.mean(avglist[ind:ind+window]))
plt.plot( average_data, 'r', label='3 Week Running average')
window = 15
average_data2 = []
for ind in range(len(avglist) - window + 1):
    average_data2.append(np.mean(avglist[ind:ind+window]))
plt.plot( average_data2, 'g', label='15 Week Running average')
plt.show()