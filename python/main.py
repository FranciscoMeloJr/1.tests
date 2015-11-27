##Main

#3D test:
from test_3D import hello, function3D, function3D_args
from final_version import *
from math_module import *


#Do the same but for h - wait-blocked: a for duration
#hello()
#Function for 3D modules: function3D_args([1,2,3,4,5,6,7,8,9,10],[5,6,7,3,3,5,7,9,11,8],[2,3,3,3,5,7,9,11,9,10])

metric = ['a','b','h']
dictionary = do_lists_full()
function3D_args(dictionary['a'],dictionary['b'],dictionary['h'],metric)
calc_square_sum(dictionary['a'],dictionary['b'],dictionary['h'])

metric = 'a' #which is the duration
lista = do_lists(metric)
print(len(lista))

svm_ovo()

#Do the graph:
do_graph(lista,"bar")

#Do histogram:
histogram = do_histogram(lista)

#Do an array:
array = create_array(histogram)
print(array)

#Plot the graph:
print_graph(array)

#SVM:
a=[19,0]
b=[21,0]
new_list = SVM(a,b,array,metric)

#Show:
print("Optimal group")
print(new_list['OPT'])

print("Not optimal group:")
print(new_list['NOPT'])

#Show all metrics:
all_metrics = do_list_full()
print(len(all_metrics))

#Function that grabs a list of a specific metric:
list_result_opt = search_list(all_metrics, new_list['OPT'],metric)
print("Info about the Opt list")
print(list_result_opt)

#Shows list_result which is the list of the metric NOPT
list_result_nopt = search_list(all_metrics, new_list['NOPT'],metric)
print("Info about the nopt list")
print(list_result_nopt)

# ----Second Analysis:
#Take a list of a specific metric:
#0679 01013429-8
#166 963 538-44

metric = ['h','a','b']
list_dimension_x = search_list_in_list(list_result_opt,metric[0])
len(list_dimension_x)

list_dimension_y = search_list_in_list(list_result_opt,metric[1])
len(list_dimension_y)

list_dimension_z = search_list_in_list(list_result_opt,metric[2])
len(list_dimension_z)
#Plot
#function3D_args(list_dimension_x,list_dimension_y,list_dimension_z,metric)

#Does a mean of a specific metric:
#wait-blocked
mean_metric(list_result_opt,metric[0])
mean_metric(list_result_nopt,metric[0])
#duration
mean_metric(list_result_opt,metric[1])
mean_metric(list_result_nopt,metric[1])
#timestamp
mean_metric(list_result_opt,metric[2])
mean_metric(list_result_nopt,metric[2])

#samples:
list_samples(list_result_opt)
