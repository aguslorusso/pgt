#Plots FPT from waitlnpdf data
#Makes all plots over the same graph. Frankly really messy.
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['text.usetex'] = True

#Fonts
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16

#Fonts
# Set font for labels in coming figures
font22 = {'family': 'serif',
          'color':  'black',
          'weight': 'normal',
          'size': 25,
          }
#linestyle = ['-','-.','--',':']
linestyle = ['-','-','-','-']
path = os.getcwd()
path_pic = os.getcwd()
T2=['1.00','1.50','2.00','2.50']
fig, axes = plt.subplots(ncols=1, figsize=(7,6), sharey=False)
lowest_t = float(T2[0])
highest_t = float(T2[-1])
count = -1
for temperature in T2:
    count += 1
    path_fpt = path + '/'
    filename = 'waitlnpdfAB.'+temperature+'0000'
    FPTdata = []
    with open(os.path.join(path_fpt, filename), 'r') as FPTf:
        for line in FPTf.readlines():
            FPTdata.append(line.split())
    FPTdata = np.array(FPTdata, dtype='float')
    temperature_f = float(temperature)
    axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color=((-np.log10(lowest_t)+np.log10(temperature_f))/(-np.log10(lowest_t) + np.log10(highest_t)),0,1-(-np.log10(lowest_t)+np.log10(temperature_f))/(-np.log10(lowest_t)+np.log10(highest_t))),lw=3,ls=linestyle[count])
axes.set_xlabel(r"$\ln\theta$",font22)
axes.set_ylabel(r"${\mathcal{P}}(\ln \theta)$",font22)
axes.set_xlim(20,140)
axes.set_ylim(0,0.30)
axes.spines[['top','right']].set_visible(False)
axes.legend(loc='upper right', frameon=False, fontsize=16)

plt.tight_layout()
filesavename="lj100_592.eps"
plt.savefig(os.path.join(path_pic,filesavename), format='eps')
plt.close()
