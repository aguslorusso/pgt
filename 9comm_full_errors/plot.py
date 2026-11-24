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

path_tem = os.getcwd()+'/TEMPS'
path_ngt = os.getcwd()+'/NGT'
path_lap_qr = os.getcwd()+'/LAPACK/QR'
path_lap_pi = os.getcwd()+'/LAPACK/PIGT'
path_arp_qr = os.getcwd()+'/ARPACK/QR'
path_arp_pi = os.getcwd()+'/ARPACK/PIGT'
path_pic = os.getcwd()
run = '/144.4.'
amp_lim = 0

color_map = {'C':(255/255, 91/255, 71/255),'A':(60/255,179/255,113/255),'B':(148/255,0,211/255), 'D':(25/255,25/255,112/255)}

#Table with all temperature to pool from
temperatures = []
filename = path_tem
with open(filename, 'r') as FPTf:
	for line in FPTf.readlines():
		temperatures.append(line)
temperatures= np.array(temperatures, dtype='float')

#Extract eigenmodes from QG results
MFPT_laqr = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_lap_qr, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_laqr.append(line.split())
MFPT_lap_qr = np.array(MFPT_laqr, dtype='float')


#Extract eigenmodes from QG results
MFPT_arqr = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_arp_qr, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_arqr.append(line.split())
MFPT_arp_qr = np.array(MFPT_arqr, dtype='float')

MFPT_la_pi = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_lap_pi, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_la_pi.append(line.split())
MFPT_lap_pi = np.array(MFPT_la_pi, dtype='float')

MFPT_ar_pi = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_arp_pi, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_ar_pi.append(line.split())
MFPT_arp_pi = np.array(MFPT_ar_pi, dtype='float')

gtmfpt = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ngt, filename), 'r') as vector:
		for line in vector.readlines():
			gtmfpt.append(line.split())
MFPT_gt = np.array(gtmfpt, dtype='float')

amps_ar_pi = []
for i in range(len(temperatures)):
	filename = 'amps'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_arp_pi, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			amps_ar_pi.append(line.split())
amps_arp_pi = np.array(amps_ar_pi, dtype='float')

amps_arp_pi = 1 - amps_arp_pi
for i in range(len(amps_arp_pi)):
	if amps_arp_pi[i] == 0.0:
		amps_arp_pi[i] = 10**(-16)

amps_la_pi = []
for i in range(len(temperatures)):
	filename = 'amps'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_lap_pi, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			amps_la_pi.append(line.split())
amps_lap_pi = np.array(amps_la_pi, dtype='float')
amps_lap_pi = 1 - amps_lap_pi
for i in range(len(amps_lap_pi)):
	if amps_lap_pi[i] == 0.0:
		amps_lap_pi[i] = 10**(-16)

#Paper Plot: Plot MFPT (relative error) for DGEEV & PIGT + DGEEV and PIGT + DGEEV & PIGT + DSAUPD
fig, axes = plt.subplots(1, 2, figsize=(13,6), sharex=True)
ax = axes[1]
plt_lim = 10
ax.plot(1/temperatures[plt_lim:], abs(amps_arp_pi[plt_lim:,0]), '+', color=color_map['A'], label='ARPACK Hybrid', ms=10)
plt_lim = 4
ax.plot(1/temperatures[plt_lim:], abs(amps_lap_pi[plt_lim:,0]), 'x', color = color_map['B'], label='LAPACK Hybrid', ms=10)
ax.legend(framealpha=1)
ax.set_yscale('log')
ax.set_yticks([1,10**(-3),10**(-6),10**(-9),10**(-12),10**(-15)])
ax.set_ylim(10**(-16),10)
ax.set_xlabel(r"$T^{-1}$", font20)
#ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel('', font20)
ax.set_title(r"(c) Error in FPT Integral, Complete Network", font20,pad=20)
ax.set_xlim(0,11)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.legend(loc='lower right', framealpha=1, fontsize=15)

ax = axes[0]
plt_lim = 35
ax.plot(1/temperatures[plt_lim:], abs((MFPT_lap_qr[plt_lim:,0]-MFPT_gt[plt_lim:,0])/MFPT_gt[plt_lim:,0]), 'v', color = color_map['C'], label='LAPACK', ms=10)
plt_lim = 42
ax.plot(1/temperatures[plt_lim:], abs((MFPT_arp_qr[plt_lim:,0]-MFPT_gt[plt_lim:,0])/MFPT_gt[plt_lim:,0]), 's', color = color_map['D'], label='ARPACK', ms=10)
plt_lim = 0
ax.plot(1/temperatures[plt_lim:], abs((MFPT_lap_pi[plt_lim:,0]-MFPT_gt[plt_lim:,0])/MFPT_gt[plt_lim:,0]), 'x', color = color_map['B'], label='LAPACK Hybrid', ms=10)
ax.plot(1/temperatures[plt_lim:], abs((MFPT_arp_pi[plt_lim:,0]-MFPT_gt[plt_lim:,0])/MFPT_gt[plt_lim:,0]), '+', color = color_map['A'], label='ARPACK Hybrid', ms=10)


ax.legend(framealpha=1)
ax.set_yscale('log')
ax.set_yticks([1,10**(-3),10**(-6),10**(-9),10**(-12)])
ax.set_ylim(10**(-12),10)
ax.set_xlabel(r"$T^{-1}$", font20)
#ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel('', font20)
ax.set_title(r"(a) Relative Error of MFPT, Complete Network", font20,pad=20)
ax.set_xlim(0,11)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.legend(loc='upper right', framealpha=1, fontsize=15)
plt.subplots_adjust(left=0.10, right=0.99, top = 0.9, bottom = 0.15, wspace = 0.27)
#plt.tight_layout()
filesavename="9c_bench_paper.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.close()
