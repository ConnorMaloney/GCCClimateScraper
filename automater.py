# Script by Connor Maloney - 100977005

import csv
import urllib.request 
from time import sleep
 
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

# Input user info
studentName = input("Enter student name (ex: Connor Maloney): ")
studentNumber = int(input("Enter student number (ex: 100977005): "))
cityName = input("Enter city name (ex: BRANDON CDA): ")
yearXrange = int(input("Enter starting range in years (ex: 1956): "))
yearYrange = int(input("Enter ending range in years (ex: 1958): "))

# Lits of years for progress bar print
items = list(range((yearYrange+1 - yearXrange) * 12))
l = len(items)

class ClimateData:
  def __init__(self, month, year, temp, precip, lat, lon):
    self.month = month
    self.year = year
    self.temp = temp
    self.precip = precip
    self.lat = lat
    self.lon = lon
  def __str__(self):
      return f'{self.month}/{self.year} Tm: {self.temp} P: {self.precip} Lat: {self.lat} Lon: {self.lon}'

climateDataArr =   [] # Store all climateData
climateDataArrY1 = [] # Lists split by years
climateDataArrY2 = []
climateDataArrY3 = []
counter = 0

print(f"Pulling data for {cityName} from {yearXrange} to {yearYrange}...")
# Main loop
for y in range(yearXrange, yearYrange+1):
    for m in range(1,13):
        url = f'http://climate.weather.gc.ca/prods_servs/cdn_climate_summary_report_e.html?intYear={y}&intMonth={m}&prov=MB&dataFormat=csv&btnSubmit=Download+data'
        with urllib.request.urlopen(url) as response:
            csvfile = response.read().decode('utf-8').splitlines()
            for line in csvfile:
                try:
                    if cityName.upper() in line:
                        row = line.split(',')
                        tempData = ClimateData(m, y, row[4], row[14], row[1], row[2])
                        climateDataArr.append(tempData)
                        printProgressBar(counter, l, prefix = f'Pulling {tempData}:', suffix = 'Complete', length = 50)
                        counter+=1
                except:
                    print("ERROR: Could not find city data")
                    pass

# Split up data into 3 separate arrays for averaging @TODO: Optimize this
for i in range(len(climateDataArr)):
    if i < 12:
        climateDataArrY1.append(climateDataArr[i])
    elif i >= 12 and i < 24:
        climateDataArrY2.append(climateDataArr[i])
    elif i >= 24 and i < 36:
        climateDataArrY3.append(climateDataArr[i])

# @TODO: This is shit code and could be optimized
tempAvgY1 = round(sum(float((t.temp).strip('\"')) for t in climateDataArrY1)/len(climateDataArrY1), 2)
tempAvgY2 = round(sum(float((t.temp).strip('\"')) for t in climateDataArrY2)/len(climateDataArrY2), 2)
tempAvgY3 = round(sum(float((t.temp).strip('\"')) for t in climateDataArrY3)/len(climateDataArrY3), 2)
precAvgY1 = round(sum(float((p.precip).strip('\"')) for p in climateDataArrY1)/len(climateDataArrY1), 2)
precAvgY2 = round(sum(float((p.precip).strip('\"')) for p in climateDataArrY2)/len(climateDataArrY2), 2)
precAvgY3 = round(sum(float((p.precip).strip('\"')) for p in climateDataArrY3)/len(climateDataArrY3), 2)

f = open("demofile.csv", "a")
f.write(f'''TSES 3002 2019 Swarm Assignment Data Template,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
Name:,{studentName},,,,,,,,,,,,,,
Student Number:,{studentNumber},,,,,,,,,,,,,,
Site (Name as shown in database):,{cityName},,,,,,,,,,,,,,
Site Latitude (as shown in database):,{str(climateDataArr[0].lat)},,,,,,,,,,,,,,
Site Longiture (as shown in database):,{str(climateDataArr[0].lon)},,,,,,,,,,,,,,
Years:,{climateDataArrY1[0].year},{climateDataArrY2[0].year},{climateDataArrY3[0].year},,,,,,,,,,,,
,,,,,,,,,,,,,,,
Year,{climateDataArrY1[0].year},,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,Average (Annual Mean Temp)
Mean Temperature Tm (°C),,,{','.join([a.temp for a in climateDataArrY1])},{tempAvgY1},
Total Precipitation P (mm),,,{','.join([a.precip for a in climateDataArrY1])},{precAvgY1},
,,,,,,,,,,,,,,,
Year,{climateDataArrY2[0].year},,
Mean Temperature Tm (°C),,,{','.join([a.temp for a in climateDataArrY2])},{tempAvgY2},
Total Precipitation P (mm),,,{','.join([a.precip for a in climateDataArrY2])},{precAvgY2},
,,,,,,,,,,,,,,,
Year,{climateDataArrY3[0].year},,
Mean Temperature Tm (°C),,,{','.join([a.temp for a in climateDataArrY3])},{tempAvgY3},
Total Precipitation P (mm),,,{','.join([a.precip for a in climateDataArrY3])},{precAvgY3},
,,,,,,,,,,,,,,,
NOTES:,Assignment asks for BRANDON RCS outpost but only BRANDON CDA outpost was available,,,,,,,,,,,,,,''')

print("Download complete! Please open the new demofile.csv in the directory where you placed this script :) Happy spreadsheeting!")
print("Note: If you already have an existing demofile.csv, please delete it and run this script to generate a new one.")