#Plots FPT from waitlnpdf data
#Makes all plots over the same graph. Frankly really messy.
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['text.usetex'] = True

#Fonts
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
font24 = {'family': 'serif',
          'color':  'white',
          'weight': 'normal',
          'size': 24,
          }

path_pic = os.getcwd()
path = os.getcwd()
filename = 'waitlnpdf'
ylimit = 0.20

FPTdata = []
with open(os.path.join(path, filename), 'r') as FPTf:
	for line in FPTf.readlines():
		FPTdata.append(line.split())
FPTdata = np.array(FPTdata, dtype='float')

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

t1 = 0
t2 = 0
for i in range(len(FPTdata[:,0])):
	if FPTdata[i,0] < 20:
		t1 = i
	elif FPTdata[i,0] < 35:
		t2 = i
ax.plot(FPTdata[:t1,0],FPTdata[:t1,1],color=(0.0, 1.0, 1.0, 1.0),lw=5)
ax.plot(FPTdata[t1:t2,0],FPTdata[t1:t2,1],color=(0.20, 0.00, 1.00, 1.0),lw=5)
ax.plot(FPTdata[t2:,0],FPTdata[t2:,1],color=(0.0, 0.55, 0.15, 1.0),lw=5)

ax.set_xticks([])
ax.tick_params(axis='x',length=0,labelbottom=False)
ax.spines["bottom"].set_color("white")
ax.spines["bottom"].set_linewidth(1.5)

ax.set_yticks([])
ax.tick_params(axis="y", left=False, labelleft=False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

ax.set_ylim(-0.01,ylimit)
ax.set_xlim(0,60)
ax.set_xlabel(r"$\ln$ Time", font24,labelpad=10)

ax.annotate(
    "",
    xy=(1.02, -0.01),
    xytext=(0, -0.01),
    xycoords=("axes fraction", "data"),
    textcoords=("axes fraction", "data"),
    arrowprops=dict(
        arrowstyle="->",
        color="white",
        linewidth=1.5,
    ),
)

plt.tight_layout()
filesavename="peaks.png"
plt.savefig(os.path.join(path_pic,filesavename), 
	format='png', 
	transparent=True,
	dpi=600,
	facecolor='black',
	bbox_inches=None,
	pad_inches=0
)
plt.close()
