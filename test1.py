from astropy.time import Time
print('maybe this will work...')
unit = open('2017-05-03T22:44:11.log')
output = open('output.txt',"w")
data = unit.read()
lines = data.splitlines()
lines_with_guiderms = [line for line in lines if 'guideRMS' in line]
lenght = len(lines_with_guiderms)
count = 0

while(count < lenght):
  one_line = lines_with_guiderms[count]
  chunks = one_line.split()
  day = chunks[0]
  hour = chunks[1]
  t = Time(day + ' ' + hour)
  tt = t.mjd
  ttt = str(tt)
  frame, rms = chunks[7].split(",")[0:2]
  output.write(ttt+" "+frame+" "+rms+"\n")
  count = count + 1

output.close()
print('worked?')





 