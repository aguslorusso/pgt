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

path_t = os.getcwd()+'/LAPACK/QR/temps'
path_ngt = os.getcwd()+'/NGT'
path_eig = os.getcwd()+'/LAPACK/QR'
path_la_ibp_mfpt = os.getcwd()+'/LAPACK/iBP/mfpt'
path_la_ibp_amps = os.getcwd()+'/LAPACK/iBP/amps'
path_ar_ibp = os.getcwd()+'/ARPACK/iBP'
path_ar_qr = os.getcwd()+'/ARPACK/QR'
path_PIGT = os.getcwd()+'/ARPACK/PIGT'
path_pic = os.getcwd()
run = '.144.4.'
run_1 = '144.4.'
plt_lim = 0
amp_lim = 20

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
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_eig, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			MFPT_laqr.append(line.split())
MFPT_qr = np.array(MFPT_laqr, dtype='float')

#Extract eigenmodes from QG results
MFPT_arqr = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
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
	filename = run_1+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_la_ibp_amps, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			amps_la_pi.append(line.split())
amps_lapi = np.array(amps_la_pi, dtype='float')
amps_lapi = 1 - amps_lapi
for i in range(len(amps_lapi)):
	if amps_lapi[i] == 0.0:
		amps_lapi[i] = 10**(-16)

MFPT_la_pi = []
for i in range(len(temperatures)):
	filename = run_1+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_la_ibp_mfpt, filename), 'r') as FPTf:
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

num_arpi = []
for i in range(len(temperatures)):
	filename = 'num'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ar_ibp, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			num_arpi.append(line.split())
num_pi = np.array(num_arpi, dtype='float')

gtmfpt = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ngt, filename), 'r') as vector:
		for line in vector.readlines():
			gtmfpt.append(line.split())
gtmfpt = np.array(gtmfpt, dtype='float')

evalues = np.empty((len(temperatures),amp_lim))
amptdes = np.empty((len(temperatures),amp_lim))
for i in range(len(temperatures)):
	for j in range(amp_lim):
		evalues[i,j] = np.nan
		amptdes[i,j] = np.nan
for i in range(len(temperatures)):
	filename = 'amps'+run+'{0:.3f}'.format(temperatures[i])
	count = 0
	with open(os.path.join(path_PIGT, filename), 'r') as vector:
		for line in vector.readlines():
			count += 1
			evalues[i, count-1] = line.split()[0]
			amptdes[i, count-1] = line.split()[3]
evalues_ar = evalues
amptdes_ar = amptdes

#Plot MFPT against 1/T for a quick evaluation
color_map = {'C':(255/255, 91/255, 71/255),'A':(60/255,179/255,113/255),'B':(148/255,0,211/255), 'D':(25/255,25/255,112/255)}
fig, axes = plt.subplots(1, 2, figsize=(13,5), sharex=True)
ax = axes[0]
ax.plot(1/temperatures[plt_lim:], np.log(abs(MFPT_qr[plt_lim:,0])), 'x', color = color_map['C'], label='DGEEV', ms=10)
ax.plot(1/temperatures[plt_lim:], np.log(gtmfpt[plt_lim:,3]), 's',color = color_map['A'] , label='NGT', ms=10)
ax.plot(1/temperatures[plt_lim:], np.log(MFPT_lapi[plt_lim:,0]), '+',color = color_map['B'] , label='PIGT+DGEEV', ms=10)
ax.legend(framealpha=1)
ax.set_title(r"Arrhenius plot of MFPT", font20, pad=10)
ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel(r"$\ln \mathcal{T}_\mathcal{AB}$", font20)
ax.set_xlim(0,10)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax = axes[1]
ax.plot(1/temperatures[plt_lim:], abs((MFPT_qr[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), 'x', color = color_map['C'], label='DGEEV', ms=10)
ax.plot(1/temperatures[plt_lim:], abs((MFPT_lapi[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), '+', color = color_map['B'], label='PIGT+DGEEV', ms=10)
ax.legend(framealpha=1)
ax.set_title(r"Relative Error in MFPT from eigendecomposition", font20, pad=10)
ax.set_yscale('log')
ax.set_yticks([100,10**(-2),10**(-6),10**(-10),10**(-14)])
ax.set_ylim(10**(-14),100)
ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel(r"Relative Error", font20)
ax.set_xlim(0,10)
ax.set_xticks([0, 2, 4, 6, 8, 10])

fig.suptitle(r"PIGT Stabilization recovers the MFPT for $T^{-1} < 10 $ or $\kappa < 10^{100}$", **font20)
plt.tight_layout()
filesavename="9c_bench_mfpt.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.close()

#Plot amplitudes
fig, axes = plt.subplots(1, 2, figsize=(13,6), sharex=True)
ax = axes[0]
ax.plot(1/temperatures[plt_lim:], np.log10(abs(amps_lapi[plt_lim:,0])), '+', color = color_map['B'], label='PIGT+DGEEV', ms=10)
ax.set_title(r"DGEEV + PIGT", font20, pad=10)
ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel(r"$\log_{10} (\Sigma_l A_l - 1)$", font20)
ax.spines[['top','right']].set_visible(False)
ax.set_xlim(0,10)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_ylim(-17,2)
ax.set_yticks([-15, -10, -5, 0])
ax = axes[1]
ax.plot(1/temperatures[plt_lim:], np.log10(abs(amps_arpi[plt_lim:,0])), '+', color=color_map['B'], label='PIGT+DSEUP', ms=10)
ax.set_title(r"DSYEVR + DSAUPD + DSEUPD + PI + PIGT", font20, pad=10)
ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel(r"$\log_{10} (\Sigma_l A_l - 1)$", font20)
ax.spines[['top','right']].set_visible(False)
ax.set_xlim(0,10)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_ylim(-17,2)
ax.set_yticks([-15, -10, -5, 0])

fig.suptitle(r"ARPACK* eigenvectors are more accurate than LAPACK", **font20)
plt.tight_layout()
filesavename="9c_bench_amps.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.close()

fig, ax = plt.subplots()
ax.plot(1/temperatures[plt_lim:], abs(num_pi[plt_lim:,0]), '+', color=color_map['D'], label='PIGT+DSEUPD', ms=10)
ax.set_title(r"Temperatures exponentially affects conditioning", font20, pad=20)
ax.set_xlabel(r"$T^{-1} [k_B/\varepsilon]$", font20)
ax.set_ylabel(r"Conditioning Number", font20)
ax.set_xlim(0,10)
ax.set_yscale('log')
ax.set_yticks([1,10.0**(20),10.0**(40),10.0**(60),10.0**(80),10.0**(100)])
ax.set_ylim(1,10.0**(100))
ax.set_xticks([0, 2, 4, 6, 8, 10])

plt.tight_layout()
filesavename="9c_bench_cond.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.close()

#Plot amplitudes
fig, axes = plt.subplots(1, 2, figsize=(13,6), sharex=True)
ax = axes[0]
ax.plot(1/temperatures[plt_lim:], amptdes_ar[plt_lim:,0], '+', color = color_map['D'], label='$l=1$', ms=10)
ax.plot(1/temperatures[plt_lim:], amptdes_ar[plt_lim:,1], '+', color = color_map['A'], label='$l=2$', ms=10)
ax.plot(1/temperatures[plt_lim:], amptdes_ar[plt_lim:,4], '+', color = color_map['B'], label='$l=5$', ms=10)
ax.plot(1/temperatures[plt_lim:], amptdes_ar[plt_lim:,8], '+', color = color_map['C'], label='$l=9$', ms=10)
ax.set_title(r"Eigenvectors (FPT Peak Heights)", font20, pad=1)
ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel(r"$ A_l $", font20)
ax.set_xlim(0,10)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.legend(framealpha=1)
ax = axes[1]
ax.plot(1/temperatures[plt_lim:], -np.log(evalues_ar[plt_lim:,0]), '+', color=color_map['D'],label='$l=1$', ms=10)
ax.plot(1/temperatures[plt_lim:], -np.log(evalues_ar[plt_lim:,1]), '+', color=color_map['A'],label='$l=2$', ms=10)
ax.plot(1/temperatures[plt_lim:], -np.log(evalues_ar[plt_lim:,4]), '+', color=color_map['B'],label='$l=5$', ms=10)
ax.plot(1/temperatures[plt_lim:], -np.log(evalues_ar[plt_lim:,8]), '+', color=color_map['C'],label='$l=9$', ms=10)
ax.set_title(r"Eigenvalues (FPT Peak Positions)", font20, pad=15)
ax.set_xlabel(r"$T^{-1}[k_B/\varepsilon]$", font20)
ax.set_ylabel(r"$-\ln | \lambda_l |$", font20)
ax.set_xlim(0,10)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.legend(framealpha=1)

fig.suptitle(r"FPT Distribution becomes unstable for $T^{-1} > 10 $ or $\kappa > 10^{100}$", **font20)
plt.tight_layout()
filesavename="9c_bench_fptd.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.close()

#Paper Plot: Plot MFPT (relative error) for DGEEV & PIGT + DGEEV and PIGT + DGEEV & PIGT + DSAUPD
fig, axes = plt.subplots(1, 2, figsize=(13,6), sharex=True)
ax = axes[1]
plt_lim = 0
ax.plot(1/temperatures[plt_lim:], abs(amps_arpi[plt_lim:,0]), '+', color=color_map['A'], label='ARPACK Hybrid', ms=10)
plt_lim = 0
ax.plot(1/temperatures[plt_lim:], abs(amps_lapi[plt_lim:,0]), 'x', color = color_map['B'], label='LAPACK Hybrid', ms=10)
ax.legend(framealpha=1)
ax.set_yscale('log')
ax.set_yticks([1,10**(-3),10**(-6),10**(-9),10**(-12),10**(-15)])
ax.set_ylim(10**(-16),10)
ax.set_xlabel(r"$T^{-1}$", font20)
ax.set_ylabel('', font20)
ax.set_title(r"(d) Error in FPT Integral, Reduced Network", font20,pad=20)
ax.set_xlim(0,11)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.legend(framealpha=1, fontsize=15)
ax = axes[0]
plt_lim = -30
ax.plot(1/temperatures[plt_lim:], abs((MFPT_qr[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), 'v', color = color_map['C'], label='LAPACK', ms=10)
plt_lim = -38
ax.plot(1/temperatures[plt_lim:], abs((MFPT_arqr[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), 's', color = color_map['D'], label='ARPACK', ms=10)
plt_lim = 0
ax.plot(1/temperatures[plt_lim:], abs((MFPT_lapi[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), 'x', color = color_map['B'], label='LAPACK Hybrid', ms=10)
ax.plot(1/temperatures[plt_lim:], abs((MFPT_arpi[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), '+', color = color_map['A'], label='ARPACK Hybrid', ms=10)
ax.legend(framealpha=1)
ax.set_yscale('log')
ax.set_yticks([1,10**(-3),10**(-6),10**(-9),10**(-12)])
ax.set_ylim(10**(-12),10)
ax.set_xlabel(r"$T^{-1}$", font20)
ax.set_ylabel('', font20)
ax.set_title(r"(b) Relative Error of MFPT, Reduced Network", font20,pad=20)
ax.set_xlim(0,11)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.legend(framealpha=1, fontsize=15)
plt.subplots_adjust(left=0.10, right=0.99, top = 0.9, bottom = 0.15, wspace = 0.27)
#plt.tight_layout()
filesavename="9c_bench_paper.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.close()
