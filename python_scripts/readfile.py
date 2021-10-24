import random

from num_operation_and_time_results import Results


def read_file(fpath):
    results=[]
    file = open(fpath, 'r')
    lines = file.readlines()
    lines = lines[1:len(lines)]
    for line in lines:
        line=line.replace("\n","")
        line=line.split('\t')
        del line[1]
        results.append(Results(int(line[0]),int(float(line[1])),number_of_operations=int(line[3]),update_time=int(line[2])))

    return results