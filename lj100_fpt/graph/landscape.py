import numpy as np
import matplotlib.pyplot as plt

# Settings
N_small = 15
N_large = 100

def color_map_mfpt(values,min_m,max_m,m):
	output = np.zeros((len(values),4))
	q1 = 8/3
	q2 = 1/3
	for i in range(len(values)):	
		value = values[i]
		r2 = 3*(value - min_m)/(max_m - min_m)
		if (0.0 < r2 <= 1.0):
			output[i,:] =  [(q1-r2)/q1, r2/2, 0, m]
		if (1.0 < r2 <= 1.5):
			output[i,:] =  [0.625-(r2-1.0)/1.25, 0.50, 0, m]
		if (1.5 < r2 <= 2.0):
			output[i,:] =  [0 , 0.5, 0.625+(r2-2.0)*1.25, m]
		if (2.0 < r2 <= 3.0):
			output[i,:] =  [0, (3.0-r2)/2.0, (r2-q2)/q1, m]
	return output


# Load the data
xy = np.loadtxt("scatter.xy.tsv")
x = xy[:,0]
y = xy[:,1]
z = np.loadtxt("scatter.z.tsv")
mfpt = np.loadtxt("scatter.mfpt.tsv")
ts = np.loadtxt("scatter.ts.tsv")
ts_mfpt = np.zeros((len(ts)))
ts_important = np.zeros(len(z))
tau = np.loadtxt("scatter.tau.tsv")
groups = np.loadtxt("scatter.groups.tsv",dtype=int)

# Create scatter plot
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")

# Load colors
rgba = color_map_mfpt(mfpt,5,53,0.95)

# Plot minima
ax.scatter(x,y,z,c=rgba,s=40,alpha=0.95)

#Edge conversion into ts
for i in range(len(ts)):
	start = int(ts[i,0])
	finish = int(ts[i,1])
	branching = ts[i,2]
	# Filter out transitions within the same group
	if ((groups[start] == groups[finish])):
		ts[i,0] = np.nan
		ts[i,1] = np.nan
		ts[i,2] = np.nan
		ts_mfpt[i] = np.nan
		# But connect them with an edge
		ts_important[start] += 1
		ts_important[finish] += 1
		if (groups[start] < 3) or (groups[finish] < 3):
			N = N_small
		else:
			N = N_large
		if ts_important[start] > N:
			continue	
		ax.plot(
			[x[start], x[finish]],
			[y[start], y[finish]],
			[z[start], z[finish]],
			linewidth=0.5,
			alpha=0.7,
			color=rgba[start]
		)
	else:
		# Determine if the transition in question is important. They are already sorted, which is good
		ts_important[start] += 1
		ts_important[finish] += 1
		if (groups[start] < 3) or (groups[finish] < 3):
			N = N_small
		else:
			N = N_large
		if ts_important[start] > N:
			ts[i,0] = np.nan
			ts[i,1] = np.nan
			ts[i,2] = np.nan
			ts_mfpt[i] = np.nan
			continue	
		rate = branching * tau[start]
		transition_state = z[start] - 3.00*np.log(rate) + 3.00*np.log(3.00*1.0e5)
		ts[i,2] = transition_state
		ts[i,0] = (x[finish]+x[start])/2
		ts[i,1] = (y[finish]+y[start])/2
		ts_mfpt[i] = (mfpt[start]+mfpt[finish])/2
		ax.plot(
			[x[start], ts[i,0]],
			[y[start], ts[i,1]],
			[z[start], ts[i,2]],
			linewidth=0.6,
			alpha=0.75,
			color=rgba[start]
		)
		ax.plot(
			[x[finish], ts[i,0]],
			[y[finish], ts[i,1]],
			[z[finish], ts[i,2]],
			linewidth=0.6,
			alpha=0.75,
			color=rgba[finish]
		)

# Plot ts
rgba_e = color_map_mfpt(ts_mfpt,5,53,0.5)
ax.scatter(ts[:,0],ts[:,1],ts[:,2], s=10,c='white',alpha=0.5)

ax.view_init(elev=20, azim=-90, roll=0)
ax.set_axis_off()
ax.set_facecolor("black")
ax.set_box_aspect([1, 1, 1], zoom=1.4)

plt.tight_layout()
plt.savefig('scatter.png',format='png',dpi=1000)
plt.show()	
