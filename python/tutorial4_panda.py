#Panda:
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

from collections import Counter

#CSV:
import csv

#array to list:
import numpy as np

#Json:
import json
from pprint import pprint

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
def do_lists(arg):
    "Function Do lists:"
    x = 0
    max = len(data['executions'])
    ##Couting a:
    a_list = []
    #shows:
    while x < max:
        #print data['executions'][x]['a'] #line 1
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
        return a_list
    
    if(arg is 'b'):
        return b_list
    
    if(arg is 'h'):
        return h_list
    
    if(arg is 'f'):
        return f_list

       
    return arg

    #print len(item_dict['executions'][1]['a'])

##This function takes a list as argument and plots:
def do_graph(a):
    "Function Do lists:"
    #a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
    counts = Counter(a)
    df = pd.DataFrame.from_dict(counts, orient='index')
    df.plot(kind='bar')
    plt.show()
    
##This function takes a list as argument and returns a histogram:
def do_histogram(a):
    "Function Do histogram:"
    #a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
    counts = Counter(a)
    #df = pd.DataFrame.from_dict(counts, orient='index')
    #df.plot(kind='bar')
    #plt.show()
    print(counts)
    return counts

#this function takes a histogram and creates a csv file:
def create_csf(mylist):
    with open("test3x.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writeheader("Value","Quantity")
        writer.writerows(mylist)

#this function creates a array:
def create_array(mylist):
    p = []
    for letter in mylist:
        a = [letter, mylist[letter]]
        p.append(a)
    print p
    return p #p is an array of arrays: [[4,7],[85,1] ...]

lista = do_lists('a')
print(len(lista))

#do graph:
#do_graph(lista)
histogram = do_histogram(lista)

array = create_array(histogram)
print(array)

create_csf(array)








































