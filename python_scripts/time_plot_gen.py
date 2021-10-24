import matplotlib.pyplot as plt
from readfile import read_file
from plot_properties import *
import sys


def time_plot_generator(topo):

    coeus_path = "evaluation_results/coeus/".__add__(topo).__add__("-op-time.txt")
    cupid_path="evaluation_results/cupid/".__add__(topo).__add__("-op-time.txt")

    results_Coeus = read_file(coeus_path)
    results_Cupid =read_file(cupid_path)

    Coeus_400=list([r.update_time/1000 for r in results_Coeus if r.number_of_flows==400].__reversed__())
    Coeus_200=list([r.update_time/1000 for r in results_Coeus if r.number_of_flows==200].__reversed__())
    Coeus_100=list([r.update_time/1000 for r in results_Coeus if r.number_of_flows==100].__reversed__())

    Cupid_100=list([r.update_time/1000 for r in results_Cupid if r.number_of_flows==100].__reversed__())
    Cupid_200=list([r.update_time/1000 for r in results_Cupid if r.number_of_flows==200].__reversed__())
    Cupid_400=list([r.update_time/1000 for r in results_Cupid if r.number_of_flows==400].__reversed__())

    x=[1,1.25,1.6,2,2.5,3,4]
    #
    fig = plt.figure(1)
    plt.rc('font',**{'family':'serif','serif':['Times']})
    plt.rc('text', usetex=True)
    l1,= plt.plot(x,Coeus_100,'tab:green',marker="s",linestyle='dashed')
    l2,= plt.plot(x,Coeus_200,'tab:green',marker="^",linestyle='dashed')
    l3,= plt.plot(x,Coeus_400,'tab:green',marker=".",linestyle='dashed')

    l7,= plt.plot(x,Cupid_100,'tab:blue',linestyle=':',marker="s")
    l8,= plt.plot(x,Cupid_200,'tab:blue',linestyle=':',marker="^")
    l9,= plt.plot(x,Cupid_400,'tab:blue',linestyle=':',marker=".")
    plt.xticks(x)
    plt.grid()
    plt.yticks(range(1,int(max(max([Coeus_400,Cupid_400])))+2,2))
    plt.xlabel(r"Arrival Rate- $\lambda$ (1/s)")
    plt.ylabel("Completion Time(s)")
    legend=plt.figlegend( handles=[red_circle,blue_triangle,green_dot,Coeus_line,Cupid_line], loc = 'upper center', ncol=6, labelspacing=0.0,prop={'size': 7} )
    f = legend.figure
    f.canvas.draw()
    # bbox = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    # f.savefig('../plots/number_of_operations_time_legend.pgf', bbox_inches=bbox)
    path_to_store = "manuscripts/figures/experiments_results_figures/".__add__(topo).__add__("/").__add__(topo).__add__("_time.eps")
    plt.savefig(path_to_store,format='eps')
# plt.rc('eps', texsystem='xelatex')


if __name__ == '__main__':
    t = str(sys.argv[1])
    time_plot_generator(t)
