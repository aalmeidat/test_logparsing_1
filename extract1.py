#extracting cartID, plateID and time boundaries
import numpy

print("MJD limits extraction")

unit_cartIDplateID = open("/Users/aalmeida/Documents/LCO_LUI_Project/cartIDplateID_output.txt")

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

cartIDplateID_sorted.close()
