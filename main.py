'''

obj :
- reading csv/excel files of the MC "Microship"
- take data and plot all of them in one pic

--------------------------------------------------

docs:
- matplotlib docs == https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html , https://www.w3schools.com/python/matplotlib_plotting.asp
- pandas docs == https://www.w3schools.com/python/pandas/pandas_csv.asp
- numpy docs == https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
- for alignment == https://stackoverflow.com/questions/31810461/python-matplotlib-vertically-aligned-plots-in-matplotlib


'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
'''p is for pressure variable fro making sure there is a pressure value'''
class MCanalysis():
        
    def sourceFolder():
        # folder_p = input('drag or insert folder:')
        # folder_p= folder_p.replace(" '", "")
        
        # folder_p= folder_p.replace("'", "")
        # folder_p= folder_p.replace('"', "")
        # folder_p= folder_p.replace("&", "")
        
        # print(folder_p)
        folder_p = r"/Users/theking/Desktop/Projects/MC/data"
        path_list = os.listdir(folder_p)
        
        file_list = []
        file_name = []
        
        for file in path_list:
            file_list.append(folder_p + '/' + file)
            file = file.replace('.csv', '')
            file_name.append(file)
            
        return file_list, file_name


    def openFile():
        
        data_csv_temp = []
        data_csv_pressure = []
        data_csv_name = []
        file_list, file_name = sourceFolder()
        
        '''     handling the replacment and reading the file for th rest of the code    '''
        
        def csvFileHandler(filepath):
            
            data = pd.read_csv(filepath)
            print(data.shape)
            data_csv_temp.append(data['Temperature/℃'])
            try:
                data_csv_pressure.append(data['Pressure'])
            except Exception as e:
                p = False
                print(bool(p))
                print('error there is no pressure index '+str(e))

        for file in file_list:
            print(file)
            csvFileHandler(file)
        
        for name in file_name:
            print(name)
            data_csv_name.append(name)

        return data_csv_pressure, data_csv_temp, data_csv_name


    # pressure_list, temp_list, name_list = openFile()
    '''     plotting def    '''

    def ploting():
        pressure_list, temp_list, name_list = openFile()
        if p == False :
            fig, axs = plt.subplots(len(name_list))
        
        elif len(name_list)<2:
            fig, axs = plt.subplots(2,2)
        
        else:
            fig, axs = plt.subplots(2,len(name_list))

        fig.suptitle('MC figure')
        x=0
        y=0
        print(len(name_list))
        while x < len(name_list):
            if p:
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

if __name__ == '__main__':
    p = True
    ploting()

