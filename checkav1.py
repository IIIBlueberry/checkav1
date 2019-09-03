import datetime
import subprocess
import os
from datetime import datetime
yto = subprocess.Popen(["youtube-dl", "-i", "-F", "PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-"], stdout=subprocess.PIPE)
abc, err = yto.communicate()

resDict  = {b'394': ['l144p', '144p', 0],
		    b'395': ['l240p', '240p', 0],
		    b'396': ['l360p', '360p', 0],
		    b'397': ['l480p', '480p', 0],
		    b'398': ['hd', '720p', 0],
		    b'399': ['fhd', '1080p', 0],
		    b'400': ['qhd', '1440p', 0],
		    b'401': ['uhd', '2160p', 0],
		    b'402': ['suhd', '4320p', 0]}

encodedArr = []

videoID = b''
for line in abc.splitlines():
	if b'[info] Available formats for' in line:
		videoID = line.split(b' ')[4].rstrip(b':').rstrip()

	codecID = line.split(b' ')[0]
	if codecID in resDict:
		resDict[codecID][2] += 1
		if videoID not in encodedArr:
			encodedArr.append(videoID)

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%y-%m-%d---%H.%M%p")

print(timestampStr)
f = open('%s-result.txt' % timestampStr,"w")

for id, data in resDict.items():
	print('%s : %d'  % (data[1], data[2]), file=f)
	print('%s : %d'  % (data[1], data[2]))

print('---')
print('---', file=f)
for elem in encodedArr:
	print('https://www.youtube.com/watch?v=' + elem.decode('utf-8'), file=f)
	print('https://www.youtube.com/watch?v=' + elem.decode('utf-8'))
f.close()