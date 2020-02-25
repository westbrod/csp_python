import matplotlib.pyplot as plt

path = 'MORSE.csv'

# data_selection = input("which data would you like to see: 1) Time(s), 2) Temperature 1(°C), or 3) Temperature 1(°C)?")

#names of lists 
time_list = []
temp1_list = [] 
temp2_list = []


with open(path) as f:
    data = f.read().strip().split('\n')

# for each line in the data, print the 
for line in data[1:]:
    print(line)
    
    vals = line.split(',')
    print(vals)
    time_list += [float(vals[0])]
    temp1_list += [float(vals[1])]
    temp2_list += [float(vals[2])]
   
    everything = [time_list, temp1_list, temp2_list]


plt.plot(time_list, temp1_list, color='b' )
plt.plot(time_list, temp2_list, color= 'r')

plt.title("Time Vs Sound level")
plt.xlabel('time (in Seconds)')
plt.ylabel('Sound level (in db)')
plt.grid('on')
plt.legend((['Sound level A-weighted(dB)', 'Sound level C-weighted(dB)']))
plt.grid 

plt.show()


