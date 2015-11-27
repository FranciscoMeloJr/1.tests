##Module for math:
import math

#array to list:
import numpy as np

def calc_square_sum(list_a, list_b, list_h):
    "Function Do lists:"
    #[a][b][h]
    metric_list = []
    max = len(list_a)
    x = 0
    while x < max:
        #print data['executions'][x] #line 1
        aux = 0
        a1 = list_a[x]
        a2 = list_b[x]
        a3 = list_h[x]
        aux = ((a1**2) + (a2**2) + (a3**2))
        metric_list.append(math.sqrt(aux))
        x += 1
    
    print(metric_list)
    return metric_list

#This fuction calculates the man of
def mean_metric(list_full, metric):

    temp = []
    #print("Mean Metric:")
    for each in list_full:
        try:
            aux = each[metric]
            if aux is not None:
                temp.append(aux)
        except:
            pass

    aux = 0
    x = 0
    for each in temp:
            aux+= each
            x+=1

    arr = np.array(temp)
    #print(numpy.mean(arr, axis=0))
    print("Mean is and the std is:")
    print(aux/x)
    print(np.std(arr, axis=0))
    
    return aux/x

#Tests:
calc_square_sum([1,2,3],[1,2,3],[1,2,3])
