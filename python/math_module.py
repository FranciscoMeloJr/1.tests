##Module for math:
import math

#array to list:
import numpy as np

#plt
import matplotlib.pyplot as plt
 

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

#This fuction calculates the mean of
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

#This fuction calculates the man of
def dif_next_term(list_a):
    metric_list = []
    max = len(list_a)
    x = 1
    while x < max:
        #print data['executions'][x] #line 1
        aux = list_a[x-1]
        
        metric_list.append(aux)
        x += 1
    
    print(metric_list)
    return metric_list

def dif_next_lists(list_a,list_b,list_h):
    list_one = dif_next_term(list_a)
    list_two = dif_next_term(list_b)
    list_three = dif_next_term(list_h)

    return [list_one, list_two, list_three]

def do_vector(list_x,list_y):#array
    pi = np.pi
    print(pi)

    #X, Y = np.mgrid[-pi:pi:10j, -pi:pi:10j]
    X = list_x#[[-3.14159265]]
    Y = list_y#[[-3.14159265]]

    print(X)
    print(Y)

    U = np.sin(X)
    V = np.cos(Y)
     
    plt.figure()
    plt.quiver(X, Y, U, V)
    plt.show()

#Tests:
calc_square_sum([1,2,3],[1,2,3],[1,2,3])
do_vector([[-3.14159265 -3.14159265 -3.14159265 -3.14159265 -3.14159265 -3.14159265
  -3.14159265 -3.14159265 -3.14159265 -3.14159265]],[[-3.14159265 -3.14159265 -3.14159265 -3.14159265 -3.14159265 -3.14159265
  -3.14159265 -3.14159265 -3.14159265 -3.14159265]])
print(dif_next_lists([1,2,3],[1,2,3],[1,2,3]))
