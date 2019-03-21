# Script by Connor Maloney - 100977005

import os
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
province = input("Enter 2-letter province/territory (ex: MB for Manitoba, SK for Saskatchewan): ")
cityName = input("Enter city name (ex: BRANDON CDA or REGINA RCS): ")
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

climate_data =   [] # Store all climateData
counter = 0

print(f"Pulling data for {cityName} from {yearXrange} to {yearYrange}...")
# Main loop
for y in range(yearXrange, yearYrange+1):
    yearly_data = []
    for m in range(1,13):
        url = f'http://climate.weather.gc.ca/prods_servs/cdn_climate_summary_report_e.html?intYear={y}&intMonth={m}&prov={province}&dataFormat=csv&btnSubmit=Download+data'
        with urllib.request.urlopen(url) as response:
            csvfile = response.read().decode('utf-8').splitlines()
            for line in csvfile:
                try:
                    if cityName.upper() in line:
                        row = line.split(',')
                        tempData = ClimateData(m, y, row[4], row[14], row[1], row[2])
                        yearly_data.append(tempData)
                        printProgressBar(counter, l, prefix = f'Pulling {tempData}:', suffix = 'Complete', length = 50)
                        counter+=1
                except:
                    print("ERROR: Could not find city data")
                    pass
    climate_data.append(yearly_data)

def build_summary_per_year(data):
    avg = round(sum(float((t.temp).strip('\"')) for t in data)/len(data), 2)
    precip_avg = round(sum(float((p.precip).strip('\"')) for p in data)/len(data), 2)
    return (
        f"Year,{data[0].year},,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,Average\n"
        f"Mean Temperature Tm (°C),,,{','.join([a.temp for a in data])},{avg},\n"
        f"Total Precipitation P (mm),,,{','.join([a.precip for a in data])},{precip_avg},\n"
    )

# workaround to incredibly strange f-string error inserting backslash
yearly_summaries = ",,,,,,,,,,,,,,,\n".join([build_summary_per_year(cd) for cd in climate_data])

f = open("demofile.csv", "a")
f.write(f'''TSES 3002 2019 Swarm Assignment Data Template,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
Name:,{studentName},,,,,,,,,,,,,,
Student Number:,{studentNumber},,,,,,,,,,,,,,
Site (Name as shown in database):,{cityName},,,,,,,,,,,,,,
Site Latitude (as shown in database):,{str(climate_data[0][0].lat)},,,,,,,,,,,,,,
Site Longiture (as shown in database):,{str(climate_data[0][0].lon)},,,,,,,,,,,,,,
Years:,{','.join([str(d[0].year) for d in climate_data])},,,,,,,,,,,,
,,,,,,,,,,,,,,,
{yearly_summaries }
,,,,,,,,,,,,,,,
NOTES:,Assignment asks for BRANDON RCS outpost but only BRANDON CDA outpost was available,,,,,,,,,,,,,,''')

print(f"Download complete! File placed in {os.getcwd()} Please open the new demofile.csv there. For graphs, edit this in excel as .xlsx and work from there. Happy spreadsheeting!")
print("Note: If you already have an existing demofile.csv, please delete it and run this script to generate a new one.")
