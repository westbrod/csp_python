import matplotlib.pyplot as plt

#where the data shown is coming from:
path = 'color.csv'

#names of lists 
time_list = []
Red_list = [] 
Green_list = []
Blue_list = []

# 
with open(path) as f:
    data = f.read().strip().split('\n')

# for each line in the data after the first line:
for line in data[1:]:
    #print that line    
    # print(line)
    
    vals = line.split(',')
    # print(vals)

    time_list += [float(vals[0])]
    Red_list += [float(vals[1])]
    Green_list += [float(vals[2])]
    Blue_list += [float(vals[3])]


#making each subplot
fig, axs = plt.subplots(3)
fig.canvas.set_window_title('Colors.py')
fig.suptitle('Time Vs Light length')
axs[0].plot(2, 4, time_list, Red_list, color='r')
axs[0].grid()
axs[0].legend(['615 nm (r)'])
axs[0].axis([0,40,0,60])
axs[0].set_ylabel('Light Lenght (in nm)', fontsize = 9)

axs[1].plot(4, 20, time_list, Green_list, color= 'g')
axs[1].grid()
axs[1].axis([0,40,0,60])
axs[1].set_ylabel('Light Lenght (in nm)', fontsize = 9)
axs[1].legend(['525 nm (g)'])

axs[2].plot(5, 40, time_list, Blue_list, color= 'b')
axs[2].grid()
axs[1].axis([0,40,0,60])
axs[2].legend(['415 nm (b)'])
axs[2].set_xlabel('time (in Seconds')
axs[2].set_ylabel('Light Lenght (in nm)', fontsize = 9)


plt.show()