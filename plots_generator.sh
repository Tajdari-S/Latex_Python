#!/bin/sh
python3 python_scripts/num_op_plot_gen.py "swan"
python3 python_scripts/num_op_plot_gen.py "mesh"
python3 python_scripts/time_plot_gen.py "swan"
python3 python_scripts/time_plot_gen.py "mesh"