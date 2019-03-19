import csv
from time import sleep
'''
import urllib.request

url = 'http://climate.weather.gc.ca/prods_servs/cdn_climate_summary_report_e.html?intYear=2019&intMonth=2&prov=&dataFormat=csv&btnSubmit=Download+data'  
 
contents = urllib.request.urlopen(url)
print(contents.read())
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

for i in range(yearXrange, yearYrange+1):
    for j in range(1,13):
        with open(f'.\sheets\eng-climate-summaries-Manitoba-{j},{i}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                try:
                    if row[0] == cityName.upper():
                        sleep(0.1)
                        print(f'{j}/{i}', "Tm: ", row[4], ", P: ", row[14])
                except:
                    pass

f = open("demofile.csv", "w")
f.write('''"Environment and Climate Change Canada"
"Monthly Values for January - 1956"

"Legend"
"Stn_Name","Station Name"
"Lat","Latitude (North + , degrees)"
"Long","Longitude (West - , degrees)"
"Prov","Province"
"Tm","Mean Temperature (°C)"
"DwTm","Days without Valid Mean Temperature"
"D","Mean Temperature difference from Normal (1981-2010) (°C)"
"Tx","Highest Monthly Maximum Temperature (°C)"
"DwTx","Days without Valid Maximum Temperature"
"Tn","Lowest Monthly Minimum Temperature (°C)"
"DwTn","Days without Valid Minimum Temperature"
"S","Snowfall (cm)"
"DwS","Days without Valid Snowfall"
"S%N","Percent of Normal (1981-2010) Snowfall"
"P","Total Precipitation (mm)"
"DwP","Days without Valid Precipitation"
"P%N","Percent of Normal (1981-2010) Precipitation"
"S_G","Snow on the ground at the end of the month (cm)"
"Pd","Number of days with Precipitation 1.0 mm or more"
"BS","Bright Sunshine (hours)"
"DwBS","Days without Valid Bright Sunshine"
"BS%","Percent of Normal (1981-2010) Bright Sunshine"
"HDD","Degree Days below 18 °C"
"CDD","Degree Days above 18 °C"
"Clim_ID","Climate Identifier"
"NA","Not Available"

"Stn_Name","Lat","Long","Prov","Tm","DwTm","D","Tx","DwTx","Tn","DwTn","S","DwS","S%N","P","DwP","P%N","S_G","Pd","BS","DwBS","BS%","HDD","CDD","Clim_ID"
"BIRTLE","50.433","-101.050","MB","-18.6","0",NA,"-2.8","0","-37.2","0","38.3","0",NA,"39.5","0",NA,"","11","","",NA,"1133.3","0.0","5010240"
"BRANDON A","49.917","-99.950","MB","-18.9","0","-2.4","-2.8","0","-35.0","0","19.0","0","83.0","19.0","0","107.0","","6","","",NA,"1145.4","0.0","5010480"
"BRANDON CDA","49.867","-99.983","MB","-18.2","0","-1.7","-1.7","0","-37.2","0","26.1","0","148.0","26.1","0","146.0","","7","0.0","30.9583333333333333333333333333333333333",NA,"1122.7","0.0","5010485"
"CYPRESS RIVER","49.550","-99.083","MB","-18.4","2","-3.3","0.6","1","-37.2","2","24.2","0","110.0","24.2","0","110.0","","7","","",NA,"1056.7","0.0","5010640"
"DELORAINE","49.183","-100.500","MB","-18.0","0",NA,"1.1","0","-36.7","0","22.8","0",NA,"22.8","0",NA,"","5","","",NA,"1116.1","0.0","5010760"
"DELORAINE 2","49.167","-100.400","MB","-16.3","8",NA,"1.1","7","-36.7","6","10.1","0",NA,"10.1","0",NA,"","3","","",NA,"789.8","0.0","5010761"
"GOODLANDS CDA EPF","49.133","-100.600","MB","",,NA,"",,"",,"16.5","0",NA,"16.5","0",NA,"","4","","",NA,"","","5011080"
"HAMIOTA","50.183","-100.617","MB","-18.3","0",NA,"-4.4","0","-35.0","0","15.2","0",NA,"15.2","0",NA,"","3","","",NA,"1126.7","0.0","5011240"
"LYLETON","49.050","-101.183","MB","",,NA,"",,"",,"24.2","0",NA,"25.2","0",NA,"","6","","",NA,"","","5011600"
"MACDONALD A","50.083","-98.450","MB","-17.8","0",NA,"-3.3","0","-33.3","0","23.5","12",NA,"23.5","0",NA,"68.0","8","","",NA,"1110.7","0.0","5011680"
"MELITA","49.333","-101.000","MB","-18.1","0",NA,"1.7","0","-36.1","0","22.2","0",NA,"22.2","0",NA,"","7","","",NA,"1119.1","0.0","5011720"
"PIERSON","49.183","-101.267","MB","-18.0","0","-3.7","2.2","0","-34.4","0","15.2","0","63.0","15.2","0","66.0","","3","","",NA,"1115.6","0.0","5012080"
"PORTAGE LA PRAIRIE","49.967","-98.300","MB","-18.1","0",NA,"-3.3","0","-35.0","0","16.8","0",NA,"16.8","0",NA,"","5","","",NA,"1118.8","0.0","5012280"
"PORTAGE SOUTHPORT A","49.900","-98.267","MB","-17.2","0",NA,"-1.1","0","-32.8","0","36.0","0",NA,"36.6","0",NA,"56.0","6","","",NA,"1092.4","0.0","5012320"
"REGENT","49.317","-100.367","MB","-18.0","11",NA,"1.1","9","-36.7","10","19.1","28",NA,"19.1","28",NA,"","3","","",NA,"719.8","0.0","5012340"
"RESTON","49.550","-101.100","MB","-18.8","1",NA,"0.0","1","-35.0","0","10.6","0",NA,"10.6","0",NA,"","2","","",NA,"1103.3","0.0","5012400"
"RIVERS A","50.017","-100.317","MB","-17.9","0",NA,"-4.4","0","-34.4","0","32.4","0",NA,"33.2","0",NA,"45.0","9","0.0","30.9583333333333333333333333333333333333",NA,"1113.2","0.0","5012440"
"ST ALBANS","49.700","-99.550","MB","-18.5","0",NA,"1.1","0","-36.1","0","40.2","0",NA,"40.2","0",NA,"","11","","",NA,"1132.2","0.0","5012540"
"SHILO","49.783","-99.643","MB","-18.4","0",NA,"-1.7","0","-36.1","0","37.3","0",NA,"37.3","0",NA,"","9","","",NA,"1129.2","0.0","5012672"
"SILVERTON EXP ST","50.767","-101.150","MB","",,NA,"",,"",,"22.9","0",NA,"22.9","0",NA,"","4","","",NA,"","","5012680"
"SOURIS","49.617","-100.267","MB","-18.4","0",NA,"0.0","0","-37.8","0","15.3","0",NA,"15.3","0",NA,"","2","","",NA,"1129.9","0.0","5012720"
"WASKADA","49.033","-100.750","MB","-18.9","13",NA,"-3.3","12","-35.0","13","",,NA,"",,NA,"","","","",NA,"665.0","0.0","5013120"
"BOISSEVAIN 2","49.217","-100.083","MB","-16.6","0",NA,"1.1","0","-35.0","0","28.2","0",NA,"28.2","0",NA,"","4","","",NA,"1074.0","0.0","5020321"
"DEERWOOD","49.400","-98.317","MB","-17.5","0",NA,"1.7","0","-32.8","0","56.0","0",NA,"56.0","0",NA,"","10","","",NA,"1100.7","0.0","5020720"
"EMERSON","49.033","-97.183","MB","-17.4","0",NA,"-2.8","0","-32.8","0","40.5","0",NA,"40.5","0",NA,"","5","","",NA,"1097.5","0.0","5020880"
"GRAYSVILLE","49.500","-98.167","MB","-17.6","1",NA,"-1.1","0","-31.7","1","47.1","0",NA,"47.1","0",NA,"","8","","",NA,"1069.4","0.0","5021160"
"GRETNA (AUT)","49.030","-97.560","MB","-16.9","0",NA,"-2.2","0","-31.7","0","44.1","0",NA,"44.1","0",NA,"66.0","7","","",NA,"1083.1","0.0","5021220"
"MORDEN","49.183","-98.100","MB","-17.2","0",NA,"-0.6","0","-31.1","0","41.8","0",NA,"41.8","0",NA,"","9","","",NA,"1092.5","0.0","5021840"
"MORDEN CDA","49.183","-98.083","MB","-17.4","0","-2.8","2.2","0","-31.7","0","52.1","0","275.0","52.1","0","277.0","","9","0.0","30.9583333333333333333333333333333333333",NA,"1096.2","0.0","5021848"
"MORRIS","49.350","-97.367","MB","-16.6","0",NA,"-1.7","0","-32.8","0","64.5","0",NA,"64.5","0",NA,"","10","","",NA,"1073.2","0.0","5021920"
"NINETTE","49.400","-99.633","MB","-17.5","0",NA,"1.7","0","-37.2","0","46.8","0",NA,"46.8","0",NA,"","6","","",NA,"1099.4","0.0","5022040"
"PILOT MOUND","49.200","-98.883","MB","-16.7","3",NA,"2.2","3","-33.3","2","36.8","0",NA,"36.8","0",NA,"","8","","",NA,"970.9","0.0","5022120"
"ROLAND","49.417","-98.000","MB","-17.4","0",NA,"-2.8","0","-32.8","0","44.0","0",NA,"44.0","0",NA,"","9","","",NA,"1096.8","0.0","5022480"
"SPRAGUE","49.017","-95.600","MB","-15.5","0","0.7","-0.6","0","-36.7","0","51.2","0","193.0","51.2","0","193.0","","6","","",NA,"1039.8","0.0","5022760"
"STEINBACH","49.533","-96.767","MB","-18.1","19","-1.5","-4.4","19","-33.9","19","2.3","25",NA,"2.3","25",NA,"","1","","",NA,"433.6","0.0","5022780"
"VITA","49.133","-96.567","MB","-16.7","0",NA,"-1.1","0","-34.4","0","40.3","0",NA,"40.3","0",NA,"","4","","",NA,"1074.2","0.0","5023000"
"WINNIPEG CHARLESWOOD","49.850","-97.283","MB","",,NA,"",,"",,"32.8","0",NA,"32.8","0",NA,"","4","","",NA,"","","5023190"
"WINNIPEG E KILDONAN","49.933","-97.100","MB","",,NA,"",,"",,"34.3","0",NA,"34.3","0",NA,"","5","","",NA,"","","5023210"
"WINNIPEG INT'L A","49.917","-97.233","MB","-16.7","0","-0.4","-2.2","0","-34.4","0","44.2","0","186.0","44.2","0","222.0","89.0","11","0.0","30.9583333333333333333333333333333333333",NA,"1077.2","0.0","5023222"
"WINNIPEG ST BONIFACE","49.883","-97.100","MB","",,NA,"",,"",,"34.6","0",NA,"34.6","0",NA,"","8","","",NA,"","","5023230"
"WINNIPEG SHERBROOK ST","49.883","-97.150","MB","",,NA,"",,"",,"37.8","0",NA,"37.8","0",NA,"","5","","",NA,"","","5023250"
"ARBORG","50.933","-97.083","MB","",,"","",,"",,"40.6","0","241.0","40.6","0","241.0","","5","","",NA,"","","5030080"
"BEAUSEJOUR 2","50.033","-96.467","MB","",,"","",,"",,"41.9","0","172.0","41.9","0","170.0","","4","","",NA,"","","5030160"
"BERENS RIVER","52.350","-97.033","MB","-17.8","1",NA,"-2.2","1","-34.4","1","",,NA,"",,NA,"","","","",NA,"1072.7","0.0","5030200"
"GIMLI A","50.633","-97.050","MB","-17.1","0",NA,"-3.3","0","-32.2","0","31.4","0",NA,"31.4","0",NA,"57.0","9","","",NA,"1088.8","0.0","5031040"
"GREAT FALLS","50.467","-96.000","MB","-15.9","0",NA,"-2.8","0","-32.8","0","47.5","0",NA,"47.5","0",NA,"","11","","",NA,"1049.8","0.0","5031200"
"INDIAN BAY","49.617","-95.200","MB","-15.8","0","1.2","-1.1","0","-33.9","0","46.6","0","175.0","46.6","0","175.0","","7","","",NA,"1046.7","0.0","5031320"
"SEVEN SISTERS FALLS","50.117","-96.017","MB","-16.0","0",NA,"-2.8","0","-32.8","0","",,NA,"",,NA,"","","","",NA,"1054.9","0.0","5032640"
"ASHERN","51.133","-98.367","MB","",,NA,"",,"",,"33.0","0",NA,"33.0","0",NA,"","5","","",NA,"","","5040120"
"DAUPHIN A","51.100","-100.050","MB","-19.2","0","-3.8","-1.7","0","-35.6","0","53.5","0","323.0","53.5","0","391.0","89.0","11","0.0","30.9583333333333333333333333333333333333",NA,"1151.7","0.0","5040680"
"DURBAN CDA EPF","51.933","-101.400","MB","",,NA,"",,"",,"69.8","0",NA,"69.8","0",NA,"","11","","",NA,"","","5040840"
"GRANDVIEW CDA EPF","51.183","-100.800","MB","",,NA,"",,"",,"57.2","0",NA,"57.2","0",NA,"","9","","",NA,"","","5041120"
"KATRIME EXP ST","50.083","-98.683","MB","",,NA,"",,"",,"31.8","0",NA,"31.8","0",NA,"","6","","",NA,"","","5041400"
"KENVILLE EXP ST","52.000","-101.317","MB","",,NA,"",,"",,"52.2","0",NA,"52.2","0",NA,"","9","","",NA,"","","5041440"
"LENSWOOD EXP ST","52.533","-101.000","MB","",,NA,"",,"",,"38.0","0",NA,"38.0","0",NA,"","7","","",NA,"","","5041560"
"MOOSEHORN","51.300","-98.617","MB","-19.1","0",NA,"-4.4","0","-35.6","0","59.2","0",NA,"59.2","0",NA,"","10","","",NA,"1151.0","0.0","5041800"
"NEEPAWA A","50.233","-99.500","MB","-18.1","0",NA,"-2.2","0","-38.3","0","33.8","0",NA,"34.3","0",NA,"90.0","8","","",NA,"1120.3","0.0","5042000"
"FLIN FLON","54.767","-101.883","MB","-21.0","0","-2.1","-7.8","0","-38.9","0","33.0","0","188.0","33.0","0","188.0","","6","","",NA,"1208.2","0.0","5050920"
"THE PAS","53.817","-101.250","MB","-22.0","0",NA,"-8.3","0","-41.1","0","17.9","0",NA,"17.9","0",NA,"","5","","",NA,"1240.1","0.0","5052864"
"THE PAS A","53.967","-101.100","MB","-22.0","0","-2.9","-7.2","0","-40.0","0","34.6","0","152.0","34.6","0","205.0","113.0","8","0.0","30.9583333333333333333333333333333333333",NA,"1241.3","0.0","5052880"
"WANLESS","54.183","-101.367","MB","-21.3","0",NA,"-7.2","0","-44.4","0","11.6","0",NA,"11.6","0",NA,"","3","","",NA,"1217.0","0.0","5053080"
"BROCHET A","57.883","-101.683","MB","-26.2","0",NA,"-13.9","0","-46.7","0","18.3","0",NA,"18.3","0",NA,"47.0","4","","",NA,"1369.3","0.0","5060520"
"CHURCHILL A","58.737","-94.057","MB","-23.8","0","2.3","-10.0","0","-41.7","0","12.4","0","57.0","12.4","0","66.0","28.0","7","0.0","30.9583333333333333333333333333333333333",NA,"1294.7","0.0","5060600"
"GILLAM","56.350","-94.700","MB","-23.0","0",NA,"-5.6","0","-43.3","0","24.1","0",NA,"24.1","0",NA,"89.0","4","","",NA,"1271.1","0.0","5061000"
"LYNN LAKE","56.850","-101.033","MB","-25.7","0",NA,"-11.7","0","-45.6","0","25.4","0",NA,"25.4","0",NA,"","4","","",NA,"1354.3","0.0","5061640"
"WABOWDEN","54.917","-98.633","MB","-21.9","0",NA,"-5.0","0","-37.8","0","19.2","0",NA,"19.2","0",NA,"85.0","6","","",NA,"1238.4","0.0","5063040"''')