#parsing1
#trying to get important information from a file
#importing important packages
from astropy.time import Time
print("Attempt of extracting information from Guider and put them into different files.")	

#Open file to read
unit_guider = open('/Users/aalmeida/Documents/LCO_LUI_Project/guider/guiderJuly.rtf')

#Create destination files
output_cartIDplateID = open('cartIDplateID_output.txt',"w")
output_guideRMS = open('guideRMS_output.txt',"w")
output_RCguideRMS = open('RCguideRMS_output.txt',"w")
output_seeing = open('seeing_output.txt',"w")
output_fwhm = open('fwhm_output.txt',"w")


data_guider = unit_guider.read()
lines_guider = data_guider.splitlines()

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
print("la concha la loraaaa")
