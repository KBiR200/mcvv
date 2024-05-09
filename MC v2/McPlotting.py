from unicodedata import name
import matplotlib.pyplot as plt
import pandas as pd

def ploting(pressure_list, temp_list,name_list ):
    fig, axs = plt.subplots(2,len(name_list))

    fig.suptitle('MC figure')
    x=0
    y=0
    print(len(name_list))
    print(name_list[0][0])
    while x < len(name_list):
        axs[0,y].set_title(name_list[y])
        axs[0,y].set(ylabel='pressure')
        pressure_time = (pressure_list[y].index * 3)/3600
        axs[0,y].plot(pressure_time,pressure_list[y], 'tab:blue')

        temp_time = (temp_list[y].index * 3)/3600
        axs[1,y].set_title(name_list[y],)
        
        axs[1,y].set(ylabel='temp')
        axs[1,y].plot(temp_time,temp_list[y], "tab:red")
        
        y =y +1
        x=x+1
        print(x)

    plt.show()