#Panda:
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
#from mpl_toolkits.mplot3d import axes3d

from collections import Counter

# import SVM
from sklearn import svm
style.use("ggplot")

#CSV:
import csv

#Json:
import json
from pprint import pprint

#test svc:
import random as rd

with open('test3.json') as data_file:    
    data = json.load(data_file)

#pprint(data)
#for each1 in data['executions']:
#    for each2 in each1:
#        print each2
##This function takes a character as argument and return a list:
##for each json info it creates a list
##{u'a': 28,u'b': 1446538515159875,u'h': 28,u'samples': {u'84': 28, u'85': 28, u'86': 28}}
##gives you: lista a: [28], list b = [1446538515159875],
def do_lists_full():
    print("Function Do lists:")
    x = 0
    max = len(data['executions'])
    ##Couting a:
    a_list = []
    b_list = []
    h_list = []
    #shows:
    while x < max:
        #print data['executions'][x] #line 1
        #temp_a = data['executions'][x]['a']#put in a array:
        #temp_b = data['executions'][x]['b']#put in a array:
        #temp_h = data['executions'][x]['h']#put in a array:
        try:
            val = data['executions'][x]['a']#put in a array:
            if val is not None:#put in a array:
                a_list.append(data['executions'][x]['a'])#put in a array:
            else:
                val = 0
                a_list.append(val)
        except:
                val = 0
                a_list.append(val)#put in a array:
        x += 1
    x =0
    while x < max:
        #print data['executions'][x] #line 1
        #temp_a = data['executions'][x]['a']#put in a array:
        #temp_b = data['executions'][x]['b']#put in a array:
        #temp_h = data['executions'][x]['h']#put in a array:
        try:
            val = data['executions'][x]['b']#put in a array:
            if val is not None:#put in a array:
                b_list.append(data['executions'][x]['b'])#put in a array:
            else:
                val = 0
                b_list.append(val)
        except:
                val = 0
                b_list.append(val)#put in a array:
        x += 1
    x = 0
    while x < max:
        #print data['executions'][x] #line 1
        #temp_a = data['executions'][x]['a']#put in a array:
        #temp_b = data['executions'][x]['b']#put in a array:
        #temp_h = data['executions'][x]['h']#put in a array:
        try:
            val = data['executions'][x]['h']#put in a array:
            if val is not None:#put in a array:
                h_list.append(data['executions'][x]['h'])#put in a array:
            else:
                val = 0
                h_list.append(val)
        except:
                val = 0
                h_list.append(val)#put in a array:
        x += 1
    #Return a dictionary:
    return {'a':a_list,'b':b_list,'h':h_list}

def do_lists(arg):
    "Function Do lists:"
    x = 0
    max = len(data['executions'])
    ##Couting a:
    a_list = []
    #shows:
    while x < max:
        #print data['executions'][x] #line 1
        a_list.append(data['executions'][x]['a'])#put in a array:
        x += 1
        
    #print(len(a_list))
    #print(a_list)

    ##Couting b:
    x = 0
    b_list = []
    #shows:
    while x < max:
        #print data['executions'][x]['b'] #line 1
        b_list.append(data['executions'][x]['b'])#put in a array:
        x += 1
        
    #print(len(b_list))
    #print(b_list)

    ##Couting h:
    x = 0
    h_list = []
    #shows:
    while x < max:
        #print data['executions'][x]['a'] #line 1
        try:
            val = data['executions'][x]['h']
            if val is not None:#put in a array:
                h_list.append(val)
        except:
            pass
        x += 1
        
    #print(len(h_list))
    #print(h_list)

    ##Couting f:
    x = 0
    f_list = []
    #shows:
    while x < max:
        #print data['executions'][x]['a'] #line 1
        try:
            val = data['executions'][x]['f']
            if val is not None:#put in a array:
                f_list.append(val)
        except:
            pass
        x += 1
    #print(f_list)        
    #print(len(f_list))

    if(arg is 'a'):
        print("List Duration")
        return a_list
    
    if(arg is 'b'):
        print("Timestamp")
        return b_list
    
    if(arg is 'h'):
        return h_list
    
    if(arg is 'f'):
        return f_list
       
    return arg

    #print len(item_dict['executions'][1]['a'])
#This function takes a metric as argument and relate with timestamp
def do_lists_timestamp(metric):
    "Function Do lists:"
    x = 0
    max = len(data['executions'])
    ##Couting a:
    metric_list = []
    #shows:
    while x < max:
        #print data['executions'][x] #line 1
        temp = []
        
        temp.append(data['executions'][x]['b'])#timestamp
        temp.append(data['executions'][x][metric])#a: duration, b, timestamp, 
        metric_list.append(temp)#put in a array, metric can be 
        x += 1
        
    #print(len(a_list))
    print(metric_list)

    return metric_list

#This function takes a list and a metric and makes a list
def do_list_from_list(list_full, metric):
    "Function Do lists:"
    x = 0
    max = len(data['executions'])
    ##Couting a:
    metric_list = []
    #shows:
    while x < max:
        #print data['executions'][x] #line 1
        temp = []
        
        temp.append(list_full['executions'][x]['b'])#timestamp
        #temp.append(list_full['executions'][x][metric])#a: duration, b, timestamp, 
        metric_list.append(temp)#put in a array, metric can be 
        x += 1
        
    #print(len(a_list))
    print(metric_list)

    return metric_list

#This function takes the json and do a list for each [b,a,h] - waitblocked and samples []
def do_list_full():
    "Function does list full:"
    x = 0
    max = len(data['executions'])
    ##Couting a:
    full_list = []
    #shows:
    while x < max:
        #print data['executions'][x] #line 1
        temp = []
        for metric in data['executions'][x]:
            temp.append(data['executions'][x][metric])#timestamp
            
        full_list.append(temp)#put in a array, metric can be 
        x += 1
        
    #print(len(a_list))
    #print(full_list)
    return full_list

##This function takes a list as argument and plots:
def do_graph(a,kind):
    "Function Do lists:"
    #a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
    counts = Counter(a)
    df = pd.DataFrame.from_dict(counts, orient='index')
    #plt.figure();
    df.plot(kind=kind)
    plt.show()

##This function takes a list as argument and returns a histogram:
def do_histogram_withTimestamp(lista): #[[a,b],[a,b]]
    "Function Do histogram:"
    #a = [[timetamp, metric],[timestamp,metric],[timestamp,metric]
    aux = []
    for line in lista:
        aux.append(line[1])
        
    counts = Counter(aux)
    print(counts)
    #print(counts)
    return counts

##This function takes a list as argument and returns a histogram:
def do_histogram(a):
    "Function Do histogram:"
    #a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
    counts = Counter(a)
    #df = pd.DataFrame.from_dict(counts, orient='index')
    #df.plot(kind='barh')
    #plt.show()
    #print(counts)
    return counts

#this function takes a histogram and creates a csv file:
def create_csf(mylist, fname):
    print("Creating a CSV File")
    with open(fname, "wb") as f:
        writer = csv.writer(f)

        #writer.writeheader()
        #writer.writeheader("Value","Quantity")
        writer.writerows(mylist)

#this function creates a array:
def create_array(mylist):
    p = []
    for letter in mylist:
        a = [letter, mylist[letter]]
        p.append(a)
    print p
    return p #p is an array of arrays: [[4,7],[85,1] ...]

#this function open a csv file:
def open_csf(fname):
    print("Open CSV File")
    with open(fname) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        lines = []
        for row in readCSV:
            value = row[0]
            quantity = row[1]
            
            print(value + " " + quantity)
    
#this function plot the histogram as graph:
def print_graph(lista):
    print("Plot")
    print(lista)

    x = []
    y = []
    for line in lista:
        x.append(line[0])
        y.append(line[1])
        #print line[1]

    #print(x)
    #print(y)
    
    plt.scatter(x,y)
    plt.show()
    
#This function creates a SVC and classify:
def SVM(a,b,lista,x_axis):
    X = [a, b] #an array X of size [n_samples, n_features] holding the training samples
    y = ["OPT","NOPT"] # of class labels (strings or integers)
    clf = svm.SVC(kernel='rbf')#clf = svm.SVC(kernel='linar', C=1.0)
    clf.fit(X, y)
    opt_list = []
    nopt_list = []
    temp = []
    for line in lista:
        aux = []
        result = clf.predict([[line[0], line[1]]])
        aux.append([line[0], line[1]])
        if 'OPT' in result:
            opt_list.append([[line[0], line[1]]])
        if 'NOPT'in result:
            nopt_list.append([[line[0], line[1]]])
        temp.append(aux)

    print("Lista:")
    print(lista)
    plt.plot(lista),# linewidth=5.0)
    #plt.subplot(1, 1, 1)
    plt.ylabel('Quantity')
    #plt.xlabel(x_axis)
    plt.title('SVM')

    #plt.scatter(lista[:, 0], lista[:, 1], c = y)
    #plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')

    plt.plot([21, 21], [0, 400], 'k-', lw=2)
    #plt.legend()

    #plt.savefig("myfig.jpg") save in jpg
    plt.show()

    
    return {'OPT':opt_list, 'NOPT':nopt_list} #return the two lists for later analysis
#Function svc shape ovo
def svm_ovo():
    X = [[0], [1], [2], [3]]
    Y = [0, 1, 2, 3]
    clf = svm.SVC(decision_function_shape='ovo')
    clf.fit(X, Y) 
    
    dec = clf.decision_function([[1]])
    dec.shape[1] # 4 classes: 4*3/2 = 6
    
    clf.decision_function_shape = "ovr"
    dec = clf.decision_function([[1]])
    dec.shape[1]

#search a list inside another:
def show_list(list_metric):
    list_selected = []

    for each in list_metric: 
        list_selected.append(each[0][0]) #returns
     
    return list_selected;

#search a list inside another:
def search_list(list_full, list_metric,metric):
    list_selected = []

    comparing_list = show_list(list_metric)

    max = len(data['executions'])
    for each in comparing_list:
        #print (each)
        #rodar a lista completa
        x = 0
        while x < max:
            #comparar
            aux = data['executions'][x][metric]
            #print aux
            if each is aux: #can b 
                #pegar oq eh igual com each:
                list_selected.append(data['executions'][x])
            
            x+=1
         
    return list_selected;

#takes this list and brings a list:
def search_list_in_list(list_metric,metric):

    temp = []
    print("Searc_list_in_list:")
    print(metric)
    for each in list_metric:
        try:
            aux = each[metric]
            if aux is not None:
                temp.append(aux)
        except:
            aux = 0
            temp.append(aux)

    print(temp)
    return temp
    #print(list_metric)
    
#This fuction calculates the man of
#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt


#This fuction calculates the man of
def list_samples(list_result_opt):

    x = 0
    #print(data['stacks'])
    for each in data['stacks']:
        print(data['stacks']['151']['f'])
        x+=1
            
    return list_result_opt


##This creates a list of all durations:    
#lista = do_lists('a')
    
##This correlates timestamp and duration (a and b):
#lista = do_lists_timestamp('a')
#print(len(lista))

#This do an histogram with timestamp
#do_histogram_withTimestamp(lista)

#This the graph:
#do_graph(lista,"bar")

#This function does the graph:
#histogram = do_histogram(lista)

#This function creates an array [value:quantity]:
#array = create_array(histogram)
#print(array)

#This function creates a csv with the array:
#create_csf(array,"test3x.csv")

#This function reads the csf:
#open_csf("test3x.csv")

#This function creates a graph: example - lista = [[1,5],[1.5,8],[1,9]]
#print_graph(array),#[2,8,1.8,8,0.6,11])


#This function creates a svm: example - lista = [[1,5],[1.5,8],[1,9]]
#do_svm(array),#[2,8,1.8,8,0.6,11])

#test:
#do_svm(array)

#Do the SVM and classify
#a=[19,0]
#b=[21,0]
#SVM(a,b,array,"Duration")
