import multiprocessing
import psutil
import pandas as pd
import time


##########initiate
num_cores = multiprocessing.cpu_count()
corelist = []
for i in range(num_cores):
    corelist.append("core_"+str(i))

columns= ['stage','time']+corelist
cpu_df = pd.DataFrame(columns=columns)
percentage_per_core = psutil.cpu_percent(percpu=True)

######################


#####out of loop example

percentage_per_core = psutil.cpu_percent(percpu=True)
cpu_df.loc[len(cpu_df)] = ["outofloop",str(time.strftime("%H:%M:%S", time.localtime()))] + percentage_per_core



#for loop example
for i in range(20):
    time.sleep(0.5) #example code goes here

    #add this line
    percentage_per_core = psutil.cpu_percent(percpu=True)
    cpu_df.loc[len(cpu_df)] = ["inaloop",str(time.strftime("%H:%M:%S", time.localtime()))] + percentage_per_core



#def example


def myfunc(inputexample):
    outexample = 0

    #add this
    global monitor
    monitor = []

    for i in range(inputexample):
        time.sleep(0.1) #example code goes here
        outexample +=1
        
        #add these
        percentage_per_core = psutil.cpu_percent(percpu=True)
        monitor.append(["myfunc",str(time.strftime("%H:%M:%S", time.localtime()))] + percentage_per_core)

    return outexample

inputexample = 10
myfunc(inputexample)

#add this directly after every function call
for i in range(len(monitor)):
    cpu_df.loc[len(cpu_df)] = monitor[i]
monitor = None

#loop that contains a defined subroutine
for k in range(5):
    inputexample = k
    myfunc(inputexample)

    #add this directly after every function call liek such when in a loop
    for i in range(len(monitor)):
        cpu_df.loc[len(cpu_df)] = monitor[i]
    monitor = None


#save csv
savepath = "my_csv.csv"
cpu_df.to_csv(savepath, mode='a', header=False)

print(cpu_df)








