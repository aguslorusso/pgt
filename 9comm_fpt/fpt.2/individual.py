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
linestyle = ['-','-','-','-','-','-']
path = os.getcwd()
path_pic = os.getcwd()
T=['0.75','0.85','1.00']
#T=['0.75','0.80','0.85','0.90','1.00']
T2=['0.10','0.15','0.20','0.30']
q1 = 8/3
q2 = 1/3
lowest_t = float(T[0])
highest_t = float(T[-1])
fig, axess = plt.subplots(ncols=2, figsize=(14,6), sharey=False)
axes = axess[0]
count = -1
for temperature in T:
    count += 1
    path_fpt = path + '/'
    filename = 'waitlnpdfAB.'+temperature+'0000'
    FPTdata = []
    with open(os.path.join(path_fpt, filename), 'r') as FPTf:
        for line in FPTf.readlines():
            FPTdata.append(line.split())
    FPTdata = np.array(FPTdata, dtype='float')
    temperature_f = float(temperature)
    r2 = 3*(highest_t - temperature_f)/(highest_t - lowest_t)
    if (0.0 <= r2 <= 1.0):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = ((q1-r2)/q1, r2/2, 0),lw=5,ls=linestyle[count])
    if (1.0 < r2 <= 1.5):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = (0.625-(r2-1.0)/1.25, 0.50, 0),lw=5,ls=linestyle[count])
    if (1.5 < r2 <= 2.0):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = (0 , 0.50, 0.625+(r2-2.0)*1.25),lw=5,ls=linestyle[count])
    if (2.0 < r2 <= 3.0):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = ((r2-2)*(r2-3), (3.0-r2)/2.0, (r2-q2)/q1),lw=5,ls=linestyle[count])
        #axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = (0, (3.0-r2)/2.0, (r2-q2)/q1),lw=5,ls=linestyle[count])

axes.set_xlabel(r"$\ln\theta$",font22)
axes.set_ylabel(r"${\mathcal{P}}(\ln \theta)$",font22)
axes.set_xlim(0,50)
axes.set_ylim(0,0.20)
axes.spines[['top','right']].set_visible(False)
axes.legend(loc='upper right', frameon=False, fontsize=16)
axes.set_title(r"(a) Well-conditioned $\mathcal{A}\leftarrow\mathcal{B}$", font22,pad=20)

lowest_t = float(T2[0])
highest_t = float(T2[-1])
axes = axess[1]
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
    r2 = 3*(highest_t - temperature_f)/(highest_t - lowest_t)
    if (0.0 <= r2 <= 1.0):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = ((q1-r2)/q1, r2/2, 0),lw=5,ls=linestyle[count])
    if (1.0 < r2 <= 1.5):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = (0.625-(r2-1.0)/1.25, 0.50, 0),lw=5,ls=linestyle[count])
    if (1.5 < r2 <= 2.0):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = (0 , 0.5, 0.625+(r2-2.0)*1.25),lw=5,ls=linestyle[count])
    if (2.0 < r2 <= 3.0):
        axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = (-(r2-2)*(r2-3)*3, (3.0-r2)/2.0, (r2-q2)/q1),lw=5,ls=linestyle[count])
        #axes.plot(FPTdata[:,0],FPTdata[:,1],label=r"$T^*$="+temperature,color = (0, (3.0-r2)/2.0, (r2-q2)/q1),lw=5,ls=linestyle[count])
axes.set_xlabel(r"$\ln\theta$",font22)
axes.set_ylabel(r"${\mathcal{P}}(\ln \theta)$",font22)
axes.set_xlim(0,250)
axes.set_ylim(0,0.20)
axes.spines[['top','right']].set_visible(False)
axes.legend(loc='upper right', frameon=False, fontsize=16)
axes.set_title(r"(b) Ill-conditioned $\mathcal{A}\leftarrow\mathcal{B}$", font22,pad=20)

plt.tight_layout()
filesavename="9comm_fpt.eps"
plt.savefig(os.path.join(path_pic,filesavename), format='eps')
plt.close()
