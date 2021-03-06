import matplotlib.pyplot as plt

path = 'raw_data_311.csv'

# data_selection = input("which data would you like to see: 1) Time(s), 2) Temperature 1(°C), or 3) Temperature 1(°C)?")

#names of lists 
time_list = []
temp1_list = [] 
temp2_list = []


with open(path) as f:
    data = f.read().split('\n')

# for each line in the data, print the 
for line in data[1:]:
    vals = line.split(',')

    time_list += [int(vals[0])]
    temp1_list += [float(vals[1])]
    temp2_list += [float(vals[2])]
   
    everything = [time_list, temp1_list, temp2_list]


print(everything)

#these are the outputs to the inputs 

# if data_selection == ("1"):
#    print(time_list)
# elif data_selection == ("2"):
#     print(temp1_list)
# elif data_selection == ("3"):
#     print(temp2_list)
# else:
#     pass





plt.plot(time_list, temp1_list, color='b' )
plt.plot(time_list, temp2_list, color= 'r')
plt.title("Time Vs Temperature")
plt.xlabel('time (in Seconds)')
plt.ylabel('Temperature (in celsius) ')
plt.grid('on')
plt.legend((['Ice Water', 'Unknown Substance ']))
plt.grid 



plt.show()
