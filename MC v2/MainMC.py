from unicodedata import name
from McAllFiles import allFiles
from McAnalytics import McDownload
from McPlotting import ploting
dir = input("insert folder path: ")


files, files_names = allFiles(dir)
pressure, temp, namef = McDownload.readFileCSV(files, files_names)
# pressureNull = McDownload.set_zero_null(pressure, 'Pressure')
ploting(pressure, temp, namef)