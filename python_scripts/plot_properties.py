import matplotlib.lines as mlines

red_circle = mlines.Line2D([], [], color='k', marker='s', linestyle='None', markersize=6, label='100 flows')
blue_triangle= mlines.Line2D([], [], color='k', marker='^', linestyle='None',markersize=6, label='200 flows')
green_dot = mlines.Line2D([], [], color='k', marker='.', linestyle='None',markersize=10, label='400 flows')
Coeus_line = mlines.Line2D([], [], color='tab:green', linestyle='dashed',markersize=10, label='Coeus')
Cupid_line = mlines.Line2D([], [], color='tab:blue', linestyle=':', markersize=10, label='Cupid')