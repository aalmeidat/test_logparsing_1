#Consolidate of previous scripts.
from astropy.time import Time

#get info from super files.
#opening guider master file
unit_guider = open('/home/andres/Documents/LCO_LUI_Project/guider_august.txt')

#opening tcc master file
unit_tcc = open('/home/andres/Documents/LCO_LUI_Project/tcc_august.txt')

#preparing files where important info will be stored
output_cartIDplateID = open('cartIDplateID_output.txt',"w")
output_guideRMS = open('guideRMS_output.txt',"w")
output_RCguideRMS = open('RCguideRMS_output.txt',"w")
output_seeing = open('seeing_output.txt',"w")
output_fwhm = open('fwhm_output.txt',"w")
output_Focus = open('Focus_output.txt',"w")
output_ThreadPosition = open('ThreadPosition_output.txt',"w")
output_TrussTemp = open('TrussTemp_output.txt',"w")
output_AirMass = open('AirMass_output.txt',"w")
output_AxisErr = open('AxisErr_output.txt',"w")

#splitting master guider list in lines
data_guider = unit_guider.read()
lines_guider = data_guider.splitlines()

#testing if everything is right
lines_with_cartIDplateID = [line for line in lines_guider if 'cartridgeLoaded=' in line]
lenght_cartIDplateID = len(lines_with_cartIDplateID)
print('Number of cartIDplateID:' + str(lenght_cartIDplateID))

lines_with_guideRMS = [line for line in lines_guider if 'guideRMS=' in line]
lenght_guideRMS = len(lines_with_guideRMS)
print('Number of guideRMS:' + str(lenght_guideRMS))

lines_with_RCguideRMS = [line for line in lines_guider if 'guideRMS:' in line]
lenght_RCguideRMS = len(lines_with_RCguideRMS)
print('Number of RCguideRMS:' + str(lenght_RCguideRMS))

lines_with_seeing = [line for line in lines_guider if 'seeing' in line]
lenght_seeing = len(lines_with_seeing)
print('Number of seeing:' + str(lenght_seeing))

lines_with_fwhm = [line for line in lines_guider if 'fwhm' in line]
lenght_fwhm = len(lines_with_fwhm)
print('Number of fwhm:' + str(lenght_fwhm))

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

#begin extraction
masterCount = 0

#cartID plate ID data extraction
while(masterCount < lenght_cartIDplateID):
  one_line = lines_with_cartIDplateID[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  cartID = (chunks[6].split("=")[1]).split(",")[0]
  plateID = chunks[7].split(",")[0]
  output_cartIDplateID.write(ttt+" "+cartID+" "+plateID+"\n")
  masterCount = masterCount + 1

output_cartIDplateID.close()

masterCount = 0

#guideRMS data extraction
while(masterCount < lenght_guideRMS):
  one_line = lines_with_guideRMS[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  guideRMS = chunks[7].split(",")[1]
  output_guideRMS.write(ttt+" "+guideRMS+"\n")
  masterCount = masterCount + 1

output_guideRMS.close()

masterCount = 0

#RCguideRMS data extraction
while(masterCount < lenght_RCguideRMS):
  one_line = lines_with_RCguideRMS[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  RCguideRMSc = chunks[9]
  RCguideRMS = RCguideRMSc[:-3]
  output_RCguideRMS.write(ttt+" "+RCguideRMS+"\n")
  masterCount = masterCount + 1

output_RCguideRMS.close()

masterCount = 0

#seeing data extraction
while(masterCount < lenght_seeing):
  one_line = lines_with_seeing[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  seeing = (chunks[6].split("=")[1]).split("'")[0]
  output_seeing.write(ttt+" "+seeing+"\n")
  masterCount = masterCount + 1

output_seeing.close()

masterCount = 0

#fwhm data extraction
while(masterCount < lenght_fwhm):
  one_line = lines_with_fwhm[masterCount]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  fwhm = chunks[7].split(",")[0]
  output_fwhm.write(ttt+" "+fwhm+"\n")
  masterCount = masterCount + 1

output_fwhm.close()

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
unit_tcc.close()
unit_guider.close()

#sort plate ID, initial time and ending time
unit_cartIDplateID = open("/home/andres/Documents/LCO_LUI_Project/August/cartIDplateID_output.txt")

cartIDplateID_sorted = open('cartIDplateID_sorted.txt',"w")

data_cartIDplateID = unit_cartIDplateID.read()
lines_cartIDplateID = data_cartIDplateID.splitlines()

lenght_cartIDplateID = len(lines_cartIDplateID)

count1 = 0
first_read = True #track first read
init_time = 0.0
end_time = 0.0
cartID = None
plateID = None

while(count1 < lenght_cartIDplateID):
 chunk = lines_cartIDplateID[count1].split()

 if int(chunk[1]) != -1:
 	 if first_read:
 	 	init_time = chunk[0]
 	 	first_read = False
 	 	cartID = chunk[1]
 	 	plateID = chunk[2]
 	 else:
 	    if cartID != chunk[1]:
 	       end_time = chunk[0]
 	       cartIDplateID_sorted.write(init_time+" "+end_time+" "+cartID+" "+plateID+"\n")
 	       init_time = chunk[0]
 	       cartID = chunk[1]
 	       plateID = chunk[2]	



 count1 = count1 + 1

unit_cartIDplateID.close()

#generate list with RCguideRMS per plate
unit_RCguideRMS = open("/home/andres/Documents/LCO_LUI_Project/August/RCguideRMS_output.txt")
unit_cartIDplateID = open("/home/andres/Documents/LCO_LUI_Project/August/cartIDplateID_sorted.txt")

data_RCguideRMS = unit_RCguideRMS.read()
lines_RCguideRMS = data_RCguideRMS.splitlines()
data_cartIDplateID = unit_cartIDplateID.read()
lines_cartIDplateID = data_cartIDplateID.splitlines()

lenght_RCguideRMS = len(lines_RCguideRMS)
lenght_cartIDplateID = len(lines_cartIDplateID)

count1 = 0
count2 = 0

while(count2 < lenght_cartIDplateID):
	chunk1 = lines_cartIDplateID[count2].split()
	init_time = chunk1[0]
	end_time = chunk1[1]
	cartID = chunk1[2]
	plateID = chunk1[3]
	mjd = end_time.split(".")[0]
	pass_file = open('cart'+cartID+'_'+'plate'+plateID+'_'+mjd+'.txt',"w")
	while True:
	 chunk2 = lines_RCguideRMS[count1].split()
	 if init_time < chunk2[0] and end_time > chunk2[0]:
	 	pass_file.write(chunk2[0]+" "+chunk2[1]+"\n")
	 	count1 = count1 + 1
	 else:
	 	count2 = count2 +1
	 	pass_file.close()
	 	break

print("la concha la loraaaa")

