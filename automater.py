import csv
import urllib.request 
from time import sleep
 
'''
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

# A List of Items
items = list(range(yearXrange, yearYrange+50))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
'''
studentName = input("Enter student name: ")
studentNumber = int(input("Enter student number: "))
cityName = input("Enter city name (ex: BRANDON A): ")
yearXrange = int(input("Enter starting range (in years): "))
yearYrange = int(input("Enter ending range (in years): "))
print(f"Pulling data for {cityName} from {yearXrange} to {yearYrange}...")



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

climateDataArr = [] # Store all climateData
climateDataArrY1 = [] # Lists split by years
climateDataArrY2 = []
climateDataArrY3 = []

for y in range(yearXrange, yearYrange+1):
    for m in range(1,13):
        #sleep(0.3)
        url = f'http://climate.weather.gc.ca/prods_servs/cdn_climate_summary_report_e.html?intYear={y}&intMonth={m}&prov=MB&dataFormat=csv&btnSubmit=Download+data'
        #sleep(0.3)
        #with open(f'.\sheets\eng-climate-summaries-Manitoba-{j},{i}.csv', newline='') as csvfile:
        with urllib.request.urlopen(url) as response:
            csvfile = response.read().decode('utf-8').splitlines()
            
            for line in csvfile:
                try:
                    if cityName.upper() in line:
                        row = line.split(',')
                        #print(f'{m}/{y}', "Tm: ", str(row[4]), ", P: ", str(row[14]))
                        tempData = ClimateData(m, y, row[4], row[14], row[1], row[2])
                        climateDataArr.append(tempData)
                        print(tempData)
                except:
                    print('ERROR: City not found')
                    pass

for i in range(len(climateDataArr)):
    if i < 12:
        climateDataArrY1.append(climateDataArr[i])
    if i > 12 and i < 24:
        climateDataArrY2.append(climateDataArr[i])
    if i > 24 and i < 36:
        climateDataArrY3.append(climateDataArr[i])

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
Mean Temperature Tm (°C),,,{','.join([a.temp for a in climateDataArrY1])},
Total Precipitation P (mm),,,{','.join([a.precip for a in climateDataArrY1])},
,,,,,,,,,,,,,,,
Year,{climateDataArrY2[0].year},,
Mean Temperature Tm (°C),,,{','.join([a.temp for a in climateDataArrY2])},
Total Precipitation P (mm),,,{','.join([a.precip for a in climateDataArrY2])},
,,,,,,,,,,,,,,,
Year,{climateDataArrY3[0].year},,
Mean Temperature Tm (°C),,,{','.join([a.temp for a in climateDataArrY3])},
Total Precipitation P (mm),,,{','.join([a.precip for a in climateDataArrY3])},
,,,,,,,,,,,,,,,
NOTES:,,,,,,,,,,,,,,,''')