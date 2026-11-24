#Plots FPT from waitlnpdf data
#Makes all plots over the same graph. Frankly really messy.
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['text.usetex'] = True

run = ''

path = os.getcwd()+'/waitlnpdf'+run
path_MFPT = os.getcwd()+'/MFPT.A'
path_pic = os.getcwd()

MFPTdata = []
MFPTindex = []
MFPT_min = -5.0
MFPT_max = 145.0

q1 = 8/3
q2 = 1/3

mode = 1

with open(path_MFPT, 'r') as MFPTf:
	for line in MFPTf.readlines():
		MFPTdata.append(line.split()[1])
		MFPTindex.append(line.split()[0])
MFPTdata = np.array(MFPTdata, dtype='float')
MFPTindex = np.array(MFPTindex, dtype='int')

for filename in os.listdir(path):
	marknode = MFPTdata[list(MFPTindex).index(int(filename.split('.')[1]))]
	marknode = (marknode - MFPT_min) / (MFPT_max - MFPT_min)
	r2 = 3.0*marknode

	FPTdata = []
	with open(os.path.join(path, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			FPTdata.append(line.split())
	FPTdata = np.array(FPTdata, dtype='float')

	if (0.0 < r2 <= 1.0):
		plt.plot(FPTdata[:,0],FPTdata[:,1], color = ((q1-r2)/q1, r2/2, 0), zorder=mode*(1-marknode) + (1-mode)*marknode)
	if (1.0 < r2 <= 1.5):
		plt.plot(FPTdata[:,0],FPTdata[:,1], color = (0.625-(r2-1.0)/1.25, 0.50, 0), zorder=mode*(1-marknode) + (1-mode)*marknode)
	if (1.5 < r2 <= 2.0):
		plt.plot(FPTdata[:,0],FPTdata[:,1], color = (0 , 0.5, 0.625+(r2-2.0)*1.25), zorder=mode*(1-marknode) + (1-mode)*marknode)
	if (2.0 < r2 <= 3.0):
		plt.plot(FPTdata[:,0],FPTdata[:,1], color = (0, (3.0-r2)/2.0, (r2-q2)/q1), zorder=mode*(1-marknode) + (1-mode)*marknode)

plt.title(r"FPT distributions for relaxation to closed GAG at 298 K")
plt.xlabel(r"ln $ \theta$")
plt.ylabel(r"${\mathcal{P}}($ln $ \theta)$")
plt.ylim(0,0.6)
plt.tight_layout()
filesavename="FPT_pgt_"+run+".eps"
plt.savefig(os.path.join(path_pic,filesavename), format='eps')
plt.close()
