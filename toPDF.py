import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import re

file_name = open("/Users/aalmeida/Documents/LCO_LUI_Project/list_2")
data_file_name = file_name.read()
lines_file_name = data_file_name.splitlines()
lenght_file_name = len(lines_file_name)

file_name_RC = open("/Users/aalmeida/Documents/LCO_LUI_Project/list_1")
data_file_name_RC = file_name_RC.read()
lines_file_name_RC = data_file_name_RC.splitlines()
lenght_file_name_RC = len(lines_file_name_RC)

cont1 = 0

with PdfPages('Plots_guideRMS_July_2017_b.pdf') as pdf: 	
  while(cont1 < lenght_file_name):
   table1 = open("/Users/aalmeida/Documents/LCO_LUI_Project/"+lines_file_name[cont1])
   data_table1 = table1.read()
   lines_table1 = data_table1.splitlines()
   chunk1 = lines_file_name[cont1].split('_')
   table2 = open("/Users/aalmeida/Documents/LCO_LUI_Project/"+lines_file_name_RC[cont1])
   data_table2 = table2.read()
   lines_table2 = data_table2.splitlines()
   chunk2 = lines_file_name_RC[cont1].split('_')
   x1 = [row.split(' ')[0] for row in lines_table1]
   y1 = [row.split(' ')[1] for row in lines_table1]
   plt.scatter(x1,y1,s=1,alpha=1,c='red',label='Uncorrected guideRMS')
   x2 = [row.split(' ')[0] for row in lines_table2]
   y2 = [row.split(' ')[1] for row in lines_table2]
   plt.scatter(x2,y2,s=0.5,alpha=1,c='blue',label='Refraction Corrected guideRMS')
   cart_number = ''.join(str(x) for x in (re.findall(r'\d+',chunk1[1])))
   plate_number = ''.join(str(x) for x in (re.findall(r'\d+',chunk1[2])))
   plt.title("Plate " + plate_number + " ,Cart " + cart_number)
   plt.xlabel('MJD')
   plt.ylabel('Guide RMS')
   plt.legend(loc='upper left');
   plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
   pdf.savefig()
   plt.close()
   #plt.show()
   cont1 = cont1 + 1




