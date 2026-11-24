#Plots FPT from waitlnpdf data
#Makes all plots over the same graph. Frankly really messy.
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['text.usetex'] = True


path = os.getcwd()+'/waitlnpdf'
path_pic = os.getcwd()

for filename in os.listdir(path):
	FPTdata = []
	with open(os.path.join(path, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			FPTdata.append(line.split())
	FPTdata = np.array(FPTdata, dtype='float')

	plt.plot(FPTdata[:,0],FPTdata[:,1],color='b')

plt.title(r"FPT distributions")
plt.xlabel(r"ln $ \theta$")
plt.ylabel(r"${\mathcal{P}}($ln $ \theta)$")
plt.tight_layout()
filesavename="FPT"+".eps"
plt.savefig(os.path.join(path_pic,filesavename), format='eps')
plt.close()
