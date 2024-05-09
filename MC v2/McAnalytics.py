import numpy as np
import pandas as pd

class McDownload():
    def readFileCSV(file_list, file_name):
        x = 0
        data_csv_temp = []
        data_csv_pressure = []
        data_csv_name = []
        
        '''     handling the replacment and reading the file for th rest of the code    '''
        
        def csvFileHandler(filepath):
            
            data = pd.read_csv(filepath)
            data_csv_temp.append(data['Temperature'])
            try:
                data_csv_pressure.append(data['Pressure'])
            except Exception as e:
                p = False
                print(bool(p))
                print('error there is no pressure index '+str(e))

        for name in file_name:
            print(name)
            data_csv_name.append(name)
        for file in file_list:
            print(file)
            csvFileHandler(file)
        return pd.DataFrame(data_csv_pressure , columns=None).T, pd.DataFrame(data_csv_temp),data_csv_name
    
    def set_zero_null(data: pd.DataFrame, rowName):
        data.head(10)
        for i,r in data.iterrows():
            if r.values < 1:
                data.loc[i,[rowName]] = np.nan
        return data
