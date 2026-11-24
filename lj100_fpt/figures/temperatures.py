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
T2=['1.00','0.80','0.60','0.40']
T=['3.00','2.50','2.00','1.50']
c = [(1.0, 0, 0.0), (0.2369655941662061, 0.8, 0.2630344058337939), (0.4150374992788438, 0, 0.5849625007211562),(0.0, 0, 1.0)]
lowest_t = float(T[-1])
highest_t = float(T[0])
fig, axess = plt.subplots(ncols=2, figsize=(14,6), sharey=False)
axes = axess[0]
count = -1
for i in range(len(T)):
    temperature = T[i]
    count += 1
    path_fpt = path + '/'
    filename = 'waitlnpdfAB.'+temperature+'0000'
    FPTdata = []
    with open(os.path.join(path_fpt, filename), 'r') as FPTf:
        for line in FPTf.readlines():
            FPTdata.append(line.split())
    FPTdata = np.array(FPTdata, dtype='float')
    temperature_f = float(temperature)
    axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T$="+temperature,color=c[i],lw=5,ls=linestyle[count])
axes.set_xlabel(r"$\ln\theta$",font22)
axes.set_ylabel(r"${\mathcal{P}}(\ln \theta)$",font22)
axes.set_xlim(10,90)
axes.set_ylim(0,0.30)
axes.set_title(r"(a) High Temperature $\mathcal{A}\leftarrow\mathcal{F}$ FPT", font22,pad=20)
axes.spines[['top','right']].set_visible(False)
axes.legend(loc='upper left', frameon=False, fontsize=16)

lowest_t = float(T2[-1])
highest_t = float(T2[0])
axes = axess[1]
count = -1
for i in range(len(T2)):
    temperature = T2[i]
    count += 1
    path_fpt = path + '/'
    filename = 'waitlnpdfAB.'+temperature+'0000'
    FPTdata = []
    with open(os.path.join(path_fpt, filename), 'r') as FPTf:
        for line in FPTf.readlines():
            FPTdata.append(line.split())
    FPTdata = np.array(FPTdata, dtype='float')
    temperature_f = float(temperature)
    axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T$="+temperature,color=c[i],lw=5,ls=linestyle[count])
axes.set_xlabel(r"$\ln\theta$",font22)
axes.set_ylabel(r"${\mathcal{P}}(\ln \theta)$",font22)
axes.set_xlim(30,300)
axes.set_ylim(0,0.40)
axes.spines[['top','right']].set_visible(False)
axes.legend(loc='upper left', frameon=False, fontsize=16)
axes.set_title(r"(b) Low Temperature $\mathcal{A}\leftarrow\mathcal{F}$ FPT", font22,pad=20)

plt.tight_layout()
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.25, hspace=None)
filesavename="lj100_592_2.eps"
plt.savefig(os.path.join(path_pic,filesavename), format='eps')
plt.close()
