import numpy as np

unit_guideRMS = open("/Users/aalmeida/Documents/LCO_LUI_Project/guideRMS_output.txt")
unit_cartIDplateID = open("/Users/aalmeida/Documents/LCO_LUI_Project/cartIDplateID_sorted.txt")

data_guideRMS = unit_guideRMS.read()
lines_guideRMS = data_guideRMS.splitlines()
data_cartIDplateID = unit_cartIDplateID.read()
lines_cartIDplateID = data_cartIDplateID.splitlines()

lenght_guideRMS = len(lines_guideRMS)
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
	pass_file = open('guideRMS_cart'+cartID+'_'+'plate'+plateID+'_'+mjd+'.txt',"w")
	while True:
	 chunk2 = lines_guideRMS[count1].split()
	 if init_time < chunk2[0] and end_time > chunk2[0]:
	 	pass_file.write(chunk2[0]+" "+chunk2[1]+"\n")
	 	count1 = count1 + 1
	 else:
	 	count2 = count2 +1
	 	pass_file.close()
	 	break