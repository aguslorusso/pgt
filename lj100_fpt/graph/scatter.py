import numpy as np
import matplotlib.pyplot as plt

def color_map_mfpt(values,min_m,max_m,m):
	output = np.zeros((229,4))
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
edges = np.loadtxt("scatter.edges.tsv",dtype=int)

# Load colors
rgba = color_map_mfpt(mfpt,5,53,1)

# Create scatter plot
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("black")

ax.scatter(x, y, z, c=rgba, s=25)

ax.view_init(elev=4, azim=45, roll=0)

# Edges
for i, j in edges:
	ax.plot(
		[x[i], x[j]],
		[y[i], y[j]],
		[z[i], z[j]],
		linewidth=0.5,
		alpha=0.3,
		color="white"
	)

ax.set_axis_off()

# Optional: make the plot look cleaner
plt.tight_layout()

# Display
plt.show()
