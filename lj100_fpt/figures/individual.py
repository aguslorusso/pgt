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
linestyle = ['-','-','--','-','--','-']
path = os.getcwd()
path_pic = os.getcwd()
T=['B','C','D','E','F','G']
T2=[37.4, 62.6, 87.4, 98.7, 143.15, 143.74]
q1 = 8/3
q2 = 1/3
lowest_t = -5.0
highest_t = 145.0
fig, axes = plt.subplots(ncols=1, figsize=(14,6), sharey=False)
#axes = axess[0]
axes.set_xlabel(r"$\ln\theta$",font22)
axes.set_ylabel(r"${\mathcal{P}}(\ln \theta)$",font22)
axes.set_xlim(-5,150)
#axes.set_ylim(10**(-24),1.00)
axes.set_ylim(0.0,0.40)
#axes.set_yscale('log')

x1, x2, y1, y2 = 135, 150, 10**(-29), 10**(-19)  # subregion of the original image
axins = axes.inset_axes(
    [0.55, 0.25, 0.35, 0.6],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yscale='log')

count = -1
for i in range(len(T)):
    temperature = str(T[i])
    count += 1
    path_fpt = path + '/'
    filename = 'waitlnpdfA.'+temperature
    FPTdata = []
    with open(os.path.join(path_fpt, filename), 'r') as FPTf:
        for line in FPTf.readlines():
            FPTdata.append(line.split())
    FPTdata = np.array(FPTdata, dtype='float')
    temperature_f = float(T2[i])
    r2 = 3*(temperature_f - lowest_t)/(highest_t - lowest_t)
    if (0.0 < r2 <= 1.0):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$\mathcal{A}\leftarrow\mathcal{"+temperature+"}$", color = ((q1-r2)/q1, r2/2, 0),lw=5,ls=linestyle[count])
        axins.plot(FPTdata[:,0],FPTdata[:,1],label=r"$\mathcal{A}\leftarrow\mathcal{"+temperature+"}$", color = ((q1-r2)/q1, r2/2, 0),lw=5,ls=linestyle[count])
    if (1.0 < r2 <= 1.5):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$\mathcal{A}\leftarrow\mathcal{"+temperature+"}$", color = (0.625-(r2-1.0)/1.25, 0.50, 0),lw=5,ls=linestyle[count])
        axins.plot(FPTdata[:,0],FPTdata[:,1],label=r"$\mathcal{A}\leftarrow\mathcal{"+temperature+"}$", color = (0.625-(r2-1.0)/1.25, 0.50, 0),lw=5,ls=linestyle[count])
    if (1.5 < r2 <= 2.0):
       axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$\mathcal{A}\leftarrow\mathcal{"+temperature+"}$", color = (0 , 0.5, 0.625+(r2-2.0)*1.25),lw=5,ls=linestyle[count])
       axins.plot(FPTdata[:,0],FPTdata[:,1],label=r"$\mathcal{A}\leftarrow\mathcal{"+temperature+"}$", color = (0 , 0.5, 0.625+(r2-2.0)*1.25),lw=5,ls=linestyle[count])
    if (2.0 < r2 <= 3.0):
       axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$\mathcal{A}\leftarrow\mathcal{"+temperature+"}$", color = (0, (3.0-r2)/2.0, (r2-q2)/q1),lw=5,ls=linestyle[count])
       axins.plot(FPTdata[:,0],FPTdata[:,1],label=r"$\mathcal{A}\leftarrow\mathcal{"+temperature+"}$", color = (0, (3.0-r2)/2.0, (r2-q2)/q1),lw=5,ls=linestyle[count])
   
axes.set_title(r"FPT Distributions starting from different kinetic traps", font22,pad=20)
axes.spines[['top','right']].set_visible(False)
axes.legend(loc='upper left', frameon=False, fontsize=16)
axes.indicate_inset_zoom(axins, edgecolor="black")

#plt.tight_layout()
filesavename="lj100_traps.eps"
plt.savefig(os.path.join(path_pic,filesavename), format='eps')
plt.close()
