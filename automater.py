import csv
import shutil
import tempfile
from time import sleep

import urllib.request


url = 'http://climate.weather.gc.ca/prods_servs/cdn_climate_summary_report_e.html?intYear=2019&intMonth=2&prov=MB&dataFormat=csv&btnSubmit=Download+data'  
 
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
cityName = "BRANDON A" #input("Enter city name (ex: BRANDON A): ")
yearXrange = 1956 #int(input("Enter starting range (in years): "))
yearYrange = 1958 #int(input("Enter ending range (in years): "))
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


with urllib.request.urlopen(url) as response:
    csvfile = response.read().decode('utf-8').splitlines()
    for line in csvfile:
        if "BRANDON A" in line:
            print(line)
    #reader = csv.reader(csvfile, delimiter=',')
    #print(type(reader))
    '''
    for row in reader:
        #print(str(row))
        try:
            if row == ["BRANDON A"]:
                print("Tm: ", row[4], ", P: ", row[14])
        except:
            pass
            '''
    


'''
for i in range(yearXrange, yearYrange+1):
    for j in range(1,13):
        #with open(f'.\sheets\eng-climate-summaries-Manitoba-{j},{i}.csv', newline='') as csvfile:
        with open(contents.read(), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                try:
                    if row[0] == cityName.upper():
                        sleep(0.1)
                        print(f'{j}/{i}', "Tm: ", row[4], ", P: ", row[14])
                except:
                    pass

#f = open("demofile.csv", "w")
'''