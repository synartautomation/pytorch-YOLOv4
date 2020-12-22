import os
import re
import sys
from matplotlib import pyplot as plt
if len(sys.argv) <2:
    print("Usage: \n python plotLoss.py path_to_logfile")
    exit()

losslist=[]
steplist=[]
xylosslist=[]
whlosslist=[]
clslosslist=[]
objlosslist=[]
with open(sys.argv[1]) as f:
    for line in f:
        if "train.py[line:353]" in line.split():
            steplist.append(int(re.search("step_(.*): loss",line).group(1)))
            losslist.append(round(float(re.search("loss : (.*),loss xy",line).group(1)),2))
            xylosslist.append(round(float(re.search("loss xy : (.*),loss wh",line).group(1)),2))
            whlosslist.append(round(float(re.search("loss wh : (.*),loss obj",line).group(1)),2))
            clslosslist.append(round(float(re.search("loss cls : (.*),loss l2",line).group(1)),2))
            objlosslist.append(round(float(re.search("loss obj : (.*)，loss cls",line).group(1)),2))
fig = plt.figure(1)
plt.plot(steplist,losslist)
fig.suptitle('Loss')
plt.xlabel('Step')
plt.ylabel('Loss')
fig.savefig('loss.jpg')


fig = plt.figure(2)
plt.plot(steplist,xylosslist)
fig.suptitle('xy Loss')
plt.xlabel('Step')
plt.ylabel('xy Loss')
fig.savefig('xyloss.jpg')


fig = plt.figure(3)
plt.plot(steplist,whlosslist)
fig.suptitle('wh Loss')
plt.xlabel('Step')
plt.ylabel('wh Loss')
fig.savefig('whloss.jpg')


fig = plt.figure(4)
plt.plot(steplist,clslosslist)
fig.suptitle('cls Loss')
plt.xlabel('Step')
plt.ylabel('cls Loss')
fig.savefig('clsloss.jpg')

fig = plt.figure(5)
plt.plot(steplist,objlosslist)
fig.suptitle('obj Loss')
plt.xlabel('Step')
plt.ylabel('obj Loss')
fig.savefig('objloss.jpg')
print("All plots saved!")
plt.show()