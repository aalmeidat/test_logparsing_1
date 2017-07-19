#parsing1
#trying to get important information from a file
#importing important packages
from astropy.time import Time
print("Attempt of extracting information from TCC and put them into different files.")	

#Open file to read
unit_tcc = open('/Users/aalmeida/Documents/LCO_LUI_Project/tcc/tccJuly.rtf')

#Create destination files
output_Focus = open('Focus_output.txt',"w")
output_ThreadPosition = open('ThreadPosition_output.txt',"w")
output_TrussTemp = open('TrussTemp_output.txt',"w")
output_AirMass = open('AirMass_output.txt',"w")
output_AxisErr = open('AxisErr_output.txt',"w")

#
data_tcc = unit_tcc.read()
lines_tcc = data_tcc.splitlines()

lines_with_secFocus = [line for line in lines_tcc if 'secFocus' in line]
lenght_secFocus = len(lines_with_secFocus)
print('Number of secFocus:' + str(lenght_secFocus))

lines_with_secTrussTemp = [line for line in lines_tcc if 'secTrussTemp' in line]
lenght_secTrussTemp = len(lines_with_secTrussTemp)
print('Number of secTrussTemp:' + str(lenght_secTrussTemp))

lines_with_axisErr = [line for line in lines_tcc if 'axisErr' in line]
lenght_axisErr = len(lines_with_axisErr)
print('Number of axisErr:' + str(lenght_axisErr))

lines_with_airMass = [line for line in lines_tcc if 'airmass' in line]
lenght_airMass = len(lines_with_airMass)
print('Number of airMass:' + str(lenght_airMass))

lines_with_ThreadRingPos = [line for line in lines_tcc if 'DesThreadRingPos' in line]
lenght_ThreadRingPos = len(lines_with_ThreadRingPos)
print('Number of ThreadRingPos:' + str(lenght_ThreadRingPos))

masterCount = 0

#focus data extraction
while(masterCount < lenght_secFocus):
  one_line = lines_with_secFocus[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  secFocus = (chunks[6].split("=")[1]).split("'")[0]
  output_Focus.write(ttt+" "+secFocus+"\n")
  masterCount = masterCount + 1

output_Focus.close()

masterCount = 0

#airMass data extraction
while(masterCount < lenght_airMass):
  one_line = lines_with_airMass[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  airMass = (chunks[6].split("=")[1]).split("'")[0]
  output_AirMass.write(ttt+" "+airMass+"\n")
  masterCount = masterCount + 1

output_AirMass.close()

masterCount = 0

#thread Ring data extraction
while(masterCount < lenght_ThreadRingPos):
  one_line = lines_with_ThreadRingPos[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  ThreadRingPos = (chunks[6].split("=")[1]).split("'")[0]
  output_ThreadPosition.write(ttt+" "+ThreadRingPos+"\n")
  masterCount = masterCount + 1

output_ThreadPosition.close()

masterCount = 0

#Truss Temp data extraction
while(masterCount < lenght_secTrussTemp):
  one_line = lines_with_secTrussTemp[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  secTrussTemp = (chunks[6].split("=")[1]).split("'")[0]
  output_TrussTemp.write(ttt+" "+secTrussTemp+"\n")
  masterCount = masterCount + 1

output_TrussTemp.close()

masterCount = 0

#axisErr data extraction
while(masterCount < lenght_axisErr):
  one_line = lines_with_axisErr[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  axisErr = (chunks[6].split("=")[1]).split("'")[0]
  output_AxisErr.write(ttt+" "+axisErr+"\n")
  masterCount = masterCount + 1

output_AxisErr.close()

print("la concha la loraaaa")
