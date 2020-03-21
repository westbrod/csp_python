import matplotlib.pyplot as plt 

path = 'weather.csv'

date = []
actual_mean_temp = []
actual_min_temp = []
actual_max_temp = []
actual_precipitation = []
record_min_temp = []
record_max_temp = []

with open(path) as f:
    data = f.read().strip().split('\n')


for line in data[1:]:

    # print(line)
    
    vals = line.split(',')
    # print(vals)
    actual_mean_temp += [int(vals[1])]
    actual_min_temp	+= [int(vals[2])]
    actual_max_temp += [int(vals[3])]
    actual_precipitation +=	[float(vals[4])]
    record_min_temp	+= [int(vals[5])]
    record_max_temp += [int(vals[6])]

date = range(365)


fig, axs = plt.subplots(2, 3)
fig.canvas.set_window_title('Weather Data')
fig.suptitle('Weather Data')
axs[0][0].plot(date, actual_mean_temp, color='blanchedalmond')
axs[0][0].grid()
axs[0][0].legend(['actual_mean_temp'])


axs[0][1].plot(date, actual_min_temp, color='lightgrey')
axs[0][1].grid()
axs[0][1].legend(['actual_min_temp'])

axs[0][2].plot(date, actual_max_temp, color='gold')
axs[0][2].grid()
axs[0][2].legend(['actual_max_temp'])

axs[1][0].plot(date, actual_precipitation, color='deepskyblue')
axs[1][0].grid()
axs[1][0].legend(['actual_precipitation'])

axs[1][1].plot(date, record_min_temp, color='steelblue')
axs[1][1].grid()
axs[1][1].legend(['record_min_temp'])
axs[1][1].set_xlabel('Date')

axs[1][2].plot(date, record_max_temp, color='royalblue')
axs[1][2].grid()
axs[1][2].legend(['record_max_temp'])


plt.show()



