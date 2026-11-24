from graph_tool.all import *
import pandas as pd
import numpy as np
import os
import pickle
#
# Parameters
#
N = 10
C_0 = 0.005
p_0 = 6
r_0 = 0
gamma_0 = 0.000000001
#
# Read file with full network sizes
#
def color_map_mfpt(value,min_m,max_m,m):
	q1 = 8/3
	q2 = 1/3
	r2 = 3*(value - min_m)/(max_m - min_m)
	if (0.0 < r2 <= 1.0):
		return (q1-r2)/q1, r2/2, 0, m
	if (1.0 < r2 <= 1.5):
		return 0.625-(r2-1.0)/1.25, 0.50, 0, m
	if (1.5 < r2 <= 2.0):
		return 0 , 0.5, 0.625+(r2-2.0)*1.25, m
	if (2.0 < r2 <= 3.0):
		return 0, (3.0-r2)/2.0, (r2-q2)/q1, m
#
# PATHS
#
#path_2 =[135, 164, 40, 82, 52, 80, 2,1,167,140,141,168,113,169,138,173,174]
path =[0,86,13,167,140,141,168,113,169,138,173,174]
path_2 =[0,43,11,40,164,135,89,1,167,140,141,168,113,169,138,173,174]
path_3 = [0,203,111,218,204,209,210,139,211,212,171,112,207,208,214,213]
#
# Load data
#
nodes_df = pd.read_csv("nodes_pi_229.tsv", sep=r'\s+')
edges_df = pd.read_csv("edges_229.tsv", sep=r'\s+')
mfpt_df = pd.read_csv("mfpt.tsv", sep=r'\s+')
groups_df = pd.read_csv("groups.tsv", sep=r'\s+')
#
# Create graph
#
g = Graph(directed=False)
g.add_vertex(len(nodes_df))
#
# Define node properties
#
pi_prop = g.new_vertex_property("double")
group_prop = g.new_vertex_property("int")
label_prop = g.new_vertex_property("int")
color_vert = g.new_vertex_property("vector<double>")
color_edge = g.new_vertex_property("vector<double>")
text_prop = g.new_vertex_property("string")
vorder_prop = g.new_vertex_property("double")
pin_prop = g.new_vertex_property("bool")
pos = g.new_vertex_property("vector<double>")

for i, row in nodes_df.iterrows():
	v = g.vertex(row['node_id'])
	pi_prop[v] = row['pi']
	label_prop[v] = row['label']
	if row['group'] == 'I':
		text_prop[v] = ''
		vorder_prop[v] = row['pi']
		pin_prop[v] = False
	else:
		#text_prop[v] = row['group']
		text_prop[v] =	''
		vorder_prop[v] = 1.0
		pin_prop[v] = True

for i, row in groups_df.iterrows():
	v = g.vertex(row['node_id'])
	group_prop[v] = int(row['group'])

# Define edge property
rate_prop = g.new_edge_property("double")
edge_filter = g.new_edge_property("bool")
edge_color = g.new_edge_property("vector<double>")

for _, row in edges_df.iterrows():
	e = g.add_edge(int(row['source']), int(row['target']))
	rate_prop[e] = row['branching']
	if (int(row['source']) == int(row['target'])):
		rate_prop[e] = np.nan

for i, row in mfpt_df.iterrows():
	v = g.vertex(row['node_id'])
	value = float(row['mfpt'])
	color_vert[v] = color_map_mfpt(value,4.9,52.9,0.85)
	color_edge[v] = color_map_mfpt(value,4.9,52.9,0.40)
	edges = list(v.out_edges())
	for e in edges:
		edge_color[e] = color_edge[v]

edge_filter.a = False

for v in g.vertices():
    edges = list(v.out_edges())

    edges.sort(
        key=lambda e: rate_prop[e],
        reverse=True
    )

    for e in edges[:N]:
        edge_filter[e] = True

path_edge = g.new_edge_property("bool")
path_edge_2 = g.new_edge_property("bool")
path_edge_3 = g.new_edge_property("bool")
path_edge.a = False
path_edge_2.a = False
path_edge_3.a = False

for u, v in zip(path[:-1], path[1:]):
	e = g.edge(u, v)

	if e is not None:
		path_edge[e] = True

for u, v in zip(path_2[:-1], path_2[1:]):
	e = g.edge(v, u)

	if e is not None:
		path_edge_2[e] = True

for u, v in zip(path_3[:-1], path_3[1:]):
	e = g.edge(v, u)

	if e is not None:
		path_edge_3[e] = True

for e in g.edges():
	if path_edge[e]:
		edge_color[e] = [0.20, 0.0, 1.00, 1.0]   # fluorescent purple
		#edge_color[e] = [0.85, 0.0, 0.85, 1.0]   # fluorescent purple
		#edge_color[e] = [1.0, 0.05, 0.45, 1.0]   # fluorescent red
		edge_filter[e] = True
	if path_edge_2[e]:
		edge_color[e] = [0.0, 0.55, 0.15, 1.0]   # fluorescent red
		edge_filter[e] = True
	if path_edge_3[e]:
		edge_color[e] = [0.0, 1.0, 1.0, 1.0]   # fluorescent cyan
		edge_filter[e] = True

# Store properties
g.vertex_properties['pi'] = pi_prop
g.vertex_properties['group'] = group_prop
g.vertex_properties['label'] = label_prop
g.edge_properties['branching'] = rate_prop
g.vertex_properties['color'] = color_vert
g.vertex_properties['text'] = text_prop
g.vertex_properties['vorder'] = vorder_prop


with open("layout_pos.pkl","rb") as f:
	pos_init = pickle.load(f)
for v in g.vertices():
	pos[v] = pos_init[v]

for e in g.edges():
	if path_edge[e] == True:
		rate_prop[e]=5*rate_prop[e]+3
	elif path_edge_2[e] == True:
		rate_prop[e]=5*rate_prop[e]+5
	elif path_edge_3[e] == True:
		rate_prop[e]=5*rate_prop[e]+3
	elif edge_filter[e] == True:
		rate_prop[e]=5*rate_prop[e]+2
	else:
		rate_prop[e]=0	

graph_draw(
	g,
	pos=pos,
	vorder = g.vertex_properties['vorder'],
	vertex_size=prop_to_size(g.vertex_properties['pi'],10,25,log=True, power=3),
	vertex_fill_color = g.vertex_properties['color'],
	vertex_text = g.vertex_properties['text'],
	vertex_font_size = 20,
	edge_pen_width=rate_prop,
	#edge_end_marker='arrow',
	edge_color=edge_color,
	bg_color='black',
	output='229.pdf'
)

#pos = sfdp_layout(g,C=C_0,p=p_0,r=r_0,groups=g.vertex_properties['group'],
#			gamma=gamma_0, 
			#pin=pin_prop,
#			eweight=g.edge_properties['branching'],
			#pos=pos
#) 

#with open("layout_pos.pkl","wb") as f:
#	pickle.dump(pos,f)
#printpos = pos.get_2d_array()
#for i in range(229):
#	print(printpos[0,i],printpos[1,i])
