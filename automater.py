import csv
import shutil
import tempfile
from time import sleep

import urllib.request 
 
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
'''
cityName = input("Enter city name (ex: BRANDON A): ")
yearXrange = int(input("Enter starting range (in years): "))
yearYrange = int(input("Enter ending range (in years): "))
print(f"Pulling data for {cityName} from {yearXrange} to {yearYrange}...")

'''
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

'''
class ClimateData:
  def __init__(self, month, year, temp, precip):
    self.month = month
    self.year = year
    self.temp = temp
    self.precip = precip
'''

    

for y in range(yearXrange, yearYrange+1):
    for m in range(1,13):
        url = f'http://climate.weather.gc.ca/prods_servs/cdn_climate_summary_report_e.html?intYear={y}&intMonth={m}&prov=MB&dataFormat=csv&btnSubmit=Download+data'
        #sleep(0.3)
        #with open(f'.\sheets\eng-climate-summaries-Manitoba-{j},{i}.csv', newline='') as csvfile:
        with urllib.request.urlopen(url) as response:
            csvfile = response.read().decode('utf-8').splitlines()
            for line in csvfile:
                try:
                    if cityName.upper() in line:
                        print(f'{m}/{y}', line)
                        #print(f'{m}/{y}', "Tm: ", row[4], ", P: ", row[14])
                except:
                    pass

#f = open("demofile.csv", "w")