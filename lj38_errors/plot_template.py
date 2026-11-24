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

path_t = os.getcwd()+'/LAPACK/iBP/temps'
path_ngt = os.getcwd()+'/LAPACK/NGT'
path_eig = os.getcwd()+'/LAPACK/QR'
path_la_ibp = os.getcwd()+'/LAPACK/iBP'
path_ar_ibp = os.getcwd()+'/ARPACK/iBP'
path_ar_qr = os.getcwd()+'/ARPACK/QR'
path_pic = os.getcwd()

color_map = {'C':(255/255, 91/255, 71/255),'A':(60/255,179/255,113/255),'B':(148/255,0,211/255), 'D':(25/255,25/255,112/255)}
run = '.456.'
run_2 = '456.'
plt_lim = 0

#Table with all temperature to pool from
temperatures = []
filename = path_t
with open(filename, 'r') as FPTf:
	for line in FPTf.readlines():
		temperatures.append(line)
temperatures= np.array(temperatures, dtype='float')

#Extract eigenmodes from QG results
MFPT_laqr = []
for i in range(len(temperatures)):
	filename = run_2+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_eig, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_laqr.append(line.split())
MFPT_qr = np.array(MFPT_laqr, dtype='float')

#Extract eigenmodes from QG results
MFPT_arqr = []
for i in range(len(temperatures)):
	filename = run_2+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ar_qr, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_arqr.append(line.split())
MFPT_arqr = np.array(MFPT_arqr, dtype='float')

amps_ar_pi = []
for i in range(len(temperatures)):
	filename = 'amps'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ar_ibp, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			amps_ar_pi.append(line.split())
amps_arpi = np.array(amps_ar_pi, dtype='float')
amps_arpi = 1 - amps_arpi
for i in range(len(amps_arpi)):
	if amps_arpi[i] == 0.0:
		amps_arpi[i] = 10**(-16)

amps_la_pi = []
for i in range(len(temperatures)):
	filename = 'amps'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_la_ibp, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			amps_la_pi.append(line.split())
amps_lapi = np.array(amps_la_pi, dtype='float')
amps_lapi = 1 - amps_lapi
for i in range(len(amps_lapi)):
	if amps_lapi[i] == 0.0:
		amps_lapi[i] = 10**(-16)

MFPT_la_pi = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_la_ibp, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_la_pi.append(line.split())
MFPT_lapi = np.array(MFPT_la_pi, dtype='float')

MFPT_ar_pi = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ar_ibp, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_ar_pi.append(line.split())
MFPT_arpi = np.array(MFPT_ar_pi, dtype='float')

gtmfpt = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ngt, filename), 'r') as vector:
		for line in vector.readlines():
			gtmfpt.append(line.split())
gtmfpt = np.array(gtmfpt, dtype='float')

#Paper Plot: Plot MFPT (relative error) for DGEEV & PIGT + DGEEV and PIGT + DGEEV & PIGT + DSAUPD
fig, axes = plt.subplots(1, 2, figsize=(13,6), sharex=True)
ax = axes[1]
plt_lim = 0
ax.plot(1/temperatures[plt_lim:], abs(amps_arpi[plt_lim:,0]), '+', color=color_map['A'], label='ARPACK Hybrid', ms=10)
plt_lim = 0
ax.plot(1/temperatures[plt_lim:], abs(amps_lapi[plt_lim:,0]), 'x', color = color_map['B'], label='LAPACK Hybrid', ms=10)
ax.legend(framealpha=1)
ax.set_yscale('log')
ax.set_yticks([100,10**(-2),10**(-6),10**(-10),10**(-14),10**(-18)])
ax.set_ylim(10**(-18),100)
ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel('', font20)
ax.set_title(r"Relative Numerical Error in FPT Integral", font20,pad=20)
ax.set_xlim(0,50)
ax.set_xticks([0, 10, 20, 30, 40, 50])
ax.legend(framealpha=1, fontsize=15)
ax = axes[0]
plt_lim = 8
ax.plot(1/temperatures[plt_lim:], abs((MFPT_qr[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), 'v', color = color_map['C'], label='LAPACK', ms=10)
plt_lim = 7
ax.plot(1/temperatures[plt_lim:], abs((MFPT_arqr[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), 's', color = color_map['D'], label='ARPACK', ms=10)
plt_lim = 0
ax.plot(1/temperatures[plt_lim:], abs((MFPT_lapi[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), 'x', color = color_map['B'], label='LAPACK Hybrid', ms=10)
ax.plot(1/temperatures[plt_lim:], abs((MFPT_arpi[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), '+', color = color_map['A'], label='ARPACK Hybrid', ms=10)
ax.legend(framealpha=1)
ax.set_yscale('log')
ax.set_yticks([10000,1,10**(-4),10**(-8),10**(-12)])
ax.set_ylim(10**(-12),10000)
ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel('', font20)
ax.set_title(r"Relative Numerical Error in MFPT", font20,pad=20)
ax.set_xlim(0,50)
ax.set_xticks([0, 10, 20, 30, 40, 50])
ax.legend(framealpha=1, fontsize=15)
plt.subplots_adjust(left=0.10, right=0.99, top = 0.9, bottom = 0.15, wspace = 0.27)
#plt.tight_layout()
filesavename="lj38_bench_paper.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.close()
