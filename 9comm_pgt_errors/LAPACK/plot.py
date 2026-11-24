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

path_t = os.getcwd()+'/QR/temps'
path_ngt = os.getcwd()+'/NGT'
path_eig = os.getcwd()+'/QR'
path_ibp = os.getcwd()+'/iBP'
path_pic = os.getcwd()
run = '.144.4.'
plt_lim = 0

#Table with all temperature to pool from
run = '.144.4.'
temperatures = []
filename = path_t
with open(filename, 'r') as FPTf:
	for line in FPTf.readlines():
		temperatures.append(line)

#Define arrays
temperatures= np.array(temperatures, dtype='float')

#Extract eigenmodes from QG results
FPTdata = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_eig, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			FPTdata.append(line.split())
MFPT_qr = np.array(FPTdata, dtype='float')
FPTdata2 = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ibp, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			FPTdata2.append(line.split())
MFPT_pi = np.array(FPTdata2, dtype='float')
FPTdata3 = []
for i in range(len(temperatures)):
	filename = 'amps'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ibp, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			FPTdata3.append(line.split())
amps_pi = np.array(FPTdata3, dtype='float')
amps_pi = 1 - amps_pi
for i in range(len(amps_pi)):
	if amps_pi[i] == 0.0:
		amps_pi[i] = 10**(-16)
FPTdata4 = []
for i in range(len(temperatures)):
	filename = 'num'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ibp, filename), 'r') as FPTf:
		for line in FPTf.readlines():
			FPTdata4.append(line.split())
num_pi = np.array(FPTdata4, dtype='float')
gtmfpt = []
for i in range(len(temperatures)):
	filename = 'mfpt'+run+'{0:.3f}'.format(temperatures[i])
	with open(os.path.join(path_ngt, filename), 'r') as vector:
		for line in vector.readlines():
			gtmfpt.append(line.split())
gtmfpt = np.array(gtmfpt, dtype='float')

#Plot MFPT against 1/T for a quick evaluation
fig, axes = plt.subplots(1, 2, figsize=(11,5), sharex=True)
ax = axes[0]
ax.plot(1/temperatures[plt_lim:], np.log(abs(MFPT_qr[plt_lim:,0])), 's', label='DGEEV')
ax.plot(1/temperatures[plt_lim:], np.log(gtmfpt[plt_lim:,3]), 'x', label='NGT')
ax.plot(1/temperatures[plt_lim:], np.log(MFPT_pi[plt_lim:,0]), '+', label='PIGT+DGEEV')
ax.legend()
ax.set_title(r"Arrhenius plot of MFPT", font20)
ax.set_xlabel(r"$T^{-1}$", font20)
ax.set_ylabel(r"$\ln \mathcal{T}_\mathcal{AB}$", font20)

#Turns out these numbers are pretty close - this is a good sign!
#Calculate errors on a logarithmic scale
ax = axes[1]
ax.plot(1/temperatures[plt_lim:], abs((MFPT_qr[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), 's', label='DGEEV')
ax.plot(1/temperatures[plt_lim:], abs((MFPT_pi[plt_lim:,0]-gtmfpt[plt_lim:,3])/gtmfpt[plt_lim:,3]), '+', label='PIGT+DGEEV')
ax.legend()
ax.set_title(r"Relative Error in MFPT from eigendecomposition", font16)
ax.set_yscale('log')
ax.set_yticks([100,10**(-2),10**(-6),10**(-10),10**(-14)])
ax.set_ylim(10**(-14),100)
ax.set_xlabel(r"$T^{-1}$", font20)
ax.set_ylabel(r"Relative Error", font20)

plt.tight_layout()
filesavename="MFPT_error.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.show()

#Plot amplitudes
fig, axes = plt.subplots(1, 2, figsize=(11,5), sharex=True)
ax = axes[0]
ax.plot(1/temperatures[plt_lim:], np.log10(abs(amps_pi[plt_lim:,0])), '+', label='PIGT+DGEEV')
ax.legend()
ax.set_title(r"Error in FPT integral against $T^{-1}$", font20)
ax.set_xlabel(r"$T^{-1}$", font20)
ax.set_ylabel(r"$\log_{10} (\Sigma_l A_l - 1)$", font20)
ax.spines[['top','right']].set_visible(False)
ax = axes[1]
ax.plot(1/temperatures[plt_lim:], np.log10(abs(num_pi[plt_lim:,0])), '+', label='PIGT+DGEEV')
ax.legend()
ax.set_title(r"Arrhenius Plot of Conditioning Number", font20)
ax.set_xlabel(r"$T^{-1}$", font20)
ax.set_ylabel(r"$\log_{10} \kappa $", font20)
ax.spines[['top','right']].set_visible(False)

plt.tight_layout()
filesavename="amps_error.eps"
plt.savefig(os.path.join(path_pic, filesavename), format='eps')
plt.show()
