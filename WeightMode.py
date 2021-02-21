import csv
from collections import Counter
with open("HeightWeight.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))
n = len(newData)
data = Counter(newData)
getMode = dict(data)
mode = []
mode1 = []
mode2 = []
for a, v in getMode.items():
    a = float(a)
    if(75<a<105):
        if(v==max(list(data.values()))):
            mode.append(a)
    elif(105<a<145):
        if(v==max(list(data.values()))):
            mode1.append(a)
    elif(145<a<175):
        if(v==max(list(data.values()))):
            mode2.append(a)
if(len(mode)> len(mode1) and len(mode2)):
    print(mode)
elif(len(mode1)> len(mode) and len(mode2)):
    print(mode1)
elif(len(mode2)> len(mode) and len(mode1)):
    print(mode2)