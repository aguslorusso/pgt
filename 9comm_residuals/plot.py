#Plots FPT from waitlnpdf data
#Makes all plots over the same graph. Frankly really messy.
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['text.usetex'] = True
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
#Fonts
# Set font for labels in coming figures
font16 = {'family': 'serif',
          'color':  'black',
          'weight': 'normal',
          'size': 16,
          }

# Set font for labels in coming figures
font20 = {'family': 'serif',
          'color':  'black',
          'weight': 'normal',
          'size': 20,
          }

path_eigens = os.getcwd()+'/data/list/'
path_t = os.getcwd()+'/data/temps'
path_pic = os.getcwd()
run = '144.4.'
neigs = 84
sinks = 1
plt_lim = 0
color_map = {'C':(255/255, 91/255, 71/255),'A':(60/255,179/255,113/255),'B':(148/255,0,211/255), 'D':(25/255,25/255,112/255)}

#Table with all temperature to pool from
temperatures = []
filename = path_t
with open(filename, 'r') as FPTf:
	for line in FPTf.readlines():
		temperatures.append(line)
temperatures= np.array(temperatures, dtype='float')

#Eigenvalues
evalues = np.empty((len(temperatures),neigs-sinks))
eerrors = np.empty((len(temperatures),neigs-sinks))

for i in range(len(temperatures)):
	for j in range(neigs-sinks):
		evalues[i,j] = np.nan
		eerrors[i,j] = np.nan
for i in range(len(temperatures)):
	filename = run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_eigens, filename), 'r') as vector:
		for line in vector.readlines():
			try:
				eindexs = line.split()[0]
				evalues[i, int(eindexs)-1] = line.split()[1]
				eerrors[i, int(eindexs)-1] = line.split()[3]
				if eerrors[i,int(eindexs)-1] == 0:
					eerrors[i,int(eindexs)-1] = 2.2e-16/84
			except:
				print('error')
eerrors = eerrors*84
#Single frame plot
#fig, ax = plt.subplots()
#ax.plot(1/temperatures[plt_lim:], abs(evalues[plt_lim:,0]), '+', color=color_map['A'], label=r"$\lambda_S$", ms=10)
#ax.plot(1/temperatures[plt_lim:], abs(evalues[plt_lim:,-1]), '+', color=color_map['B'], label=r"$\lambda_1$", ms=10)
#ax.plot(1/temperatures[plt_lim:], abs(evalues[plt_lim:,-8]), '+', color=color_map['C'], label=r"$\lambda_8$", ms=10)
#ax.set_title(r"Temperatures exponentially affect eigenmodes", font20, pad=20)
#ax.set_xlabel(r"$T^{-1} [k_B/\varepsilon]$", font20)
#ax.set_ylabel(r"$| \lambda_l |$", font20)
#ax.set_xlim(0,10)
#ax.set_yscale('log')
#ax.set_yticks([1,10.0**(-20),10.0**(-40),10.0**(-60),10.0**(-80),10.0**(-100)])
#ax.set_ylim(10**4,10.0**(-120))
#ax.set_xticks([0, 2, 4, 6, 8, 10])
#ax.legend()
#
#plt.tight_layout()
#filesavename="9c_eigenvalues.eps"
#plt.savefig(os.path.join(path_pic, filesavename), format='eps')
#plt.close()

#Paper Plot: Plot MFPT (relative error) for DGEEV & PIGT + DGEEV and PIGT + DGEEV & PIGT + DSAUPD
fig, axes = plt.subplots(1, 2, figsize=(13,6), sharex=True)

ax = axes[1]
ax.plot(1/temperatures[plt_lim:], abs(eerrors[plt_lim:,-1]), '-', color=color_map['D'], label=r"$l=1$", ms=10, lw=4)
ax.plot(1/temperatures[plt_lim:], abs(eerrors[plt_lim:,-2]), '-', color=color_map['C'], label=r"$l=2$", ms=10, lw=4)
ax.plot(1/temperatures[plt_lim:], abs(eerrors[plt_lim:,-5]), '-', color=color_map['B'], label=r"$l=5$", ms=10, lw=4)
ax.plot(1/temperatures[plt_lim:], abs(eerrors[plt_lim:,-8]), '-', color=color_map['A'], label=r"$l=8$", ms=10, lw=4)

ax.legend(framealpha=1, fontsize=15)
ax.set_title(r"Weighted residuals for slow decay modes (PIGT)", font20, pad=20)
ax.set_xlabel(r"$T^{-1}$", font20)
ax.set_ylabel(r"$R_w$", font20)
ax.set_xlim(0,10)
ax.set_yscale('log')
ax.set_yticks([1,10.0**(-4),10.0**(-8),10.0**(-12),10.0**(-16)])
ax.set_ylim(10.0**(-16),10**2)
ax.set_xticks([0, 2, 4, 6, 8, 10])

ax = axes[0]
ax.plot(1/temperatures[plt_lim:], abs(eerrors[plt_lim:,-10]), '-', color=color_map['D'], label=r"$l=10$", ms=10, lw=4)
ax.plot(1/temperatures[plt_lim:], abs(eerrors[plt_lim:,-20]), '-', color=color_map['C'], label=r"$l=20$", ms=10, lw=4)
ax.plot(1/temperatures[plt_lim:], abs(eerrors[plt_lim:,-50]), '-', color=color_map['B'], label=r"$l=50$", ms=10, lw=4)
ax.plot(1/temperatures[plt_lim:], abs(eerrors[plt_lim:,-80]), '-', color=color_map['A'], label=r"$l=80$", ms=10, lw=4)
ax.legend(framealpha=1, fontsize=15)
ax.set_title(r"Weighted residuals for fast decay modes (ARPACK)", font20, pad=20)
ax.set_xlabel(r"$T^{-1}$", font20)
ax.set_ylabel(r"$R_w$", font20)
ax.set_xlim(0,10)
ax.set_yscale('log')
ax.set_yticks([1,10.0**(-4),10.0**(-8),10.0**(-12),10.0**(-16)])
ax.set_ylim(10.0**(-16),10**2)
ax.set_xticks([0, 2, 4, 6, 8, 10])

#ax.plot(1/temperatures[plt_lim:], np.log(abs(evalues[plt_lim:,-1])), '-', color=color_map['A'], label=r"$\lambda_1$", ms=10)
#ax.plot(1/temperatures[plt_lim:], np.log(abs(evalues[plt_lim:,-5])), '-', color=color_map['B'], label=r"$\lambda_5$", ms=10)
#ax.plot(1/temperatures[plt_lim:], np.log(abs(evalues[plt_lim:,-8])), '-', color=color_map['C'], label=r"$\lambda_8$", ms=10)
#ax.plot(1/temperatures[plt_lim:], np.log(abs(evalues[plt_lim:,-10])), '-', color=color_map['D'], label=r"$\lambda_{10}$", ms=10)
#ax.legend(framealpha=1, fontsize=15)
#ax.set_title(r"Arrhenius plot for slow eigenvalues", font20, pad=20)
#ax.set_xlabel(r"$T^{-1} [k_B/\varepsilon]$", font20)
#ax.set_ylabel(r"$\ln | \lambda_l |$", font20)
#ax.set_xlim(0,10)
#ax.set_yticks([0,-50,-100,-150,-200,-250])
#ax.set_ylim(-250,np.log(10**4))
#ax.set_xticks([0, 2, 4, 6, 8, 10])

plt.subplots_adjust(left=0.10, right=0.99, top = 0.9, bottom = 0.15, wspace = 0.27)
filesavename="9c_eigenvalues.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.close()
