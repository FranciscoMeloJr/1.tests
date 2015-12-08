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

#warning:
import warnings
warnings.filterwarnings("ignore")


#pprint(data)
#for each1 in data['executions']:
#    for each2 in each1:
#        print each2
##This function takes a character as argument and return a list:
##for each json info it creates a list
##{u'a': 28,u'b': 1446538515159875,u'h': 28,u'samples': {u'84': 28, u'85': 28, u'86': 28}}
##gives you: lista a: [28], list b = [1446538515159875],

#Defines a json:
class trace_analysis:

    def __init__(self,jsName,identification,withgraph):
        self.jsonName = jsName
        self.id = identification
        self.defineJson()
        self.graph = withgraph
        
    def defineJson(self):
        with open(self.jsonName) as data_file:    
            self.data = json.load(data_file)

    def do_lists_full(self):
        "Function Do lists:"
        x = 0
        max = len(self.data['executions'])
        ##Couting a:
        a_list = []
        b_list = []
        h_list = []
        e_list = []
        g_list = []
        #shows:
        while x < max:
            #print data['executions'][x] #line 1
            #temp_a = data['executions'][x]['a']#put in a array:
            #temp_b = data['executions'][x]['b']#put in a array:
            #temp_h = data['executions'][x]['h']#put in a array:
            try:
                val = self.data['executions'][x]['a']#put in a array:
                if val is not None:#put in a array:
                    a_list.append(self.data['executions'][x]['a'])#put in a array:
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
                val = self.data['executions'][x]['b']#put in a array:
                if val is not None:#put in a array:
                    b_list.append(self.data['executions'][x]['b'])#put in a array:
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
                val = self.data['executions'][x]['h']#put in a array:
                if val is not None:#put in a array:
                    h_list.append(self.data['executions'][x]['h'])#put in a array:
                else:
                    val = 0
                    h_list.append(val)
            except:
                    val = 0
                    h_list.append(val)#put in a array:
            x += 1
        x = 0
        while x < max:
            #print data['executions'][x] #line 1
            #temp_a = data['executions'][x]['a']#put in a array:
            #temp_b = data['executions'][x]['b']#put in a array:
            #temp_h = data['executions'][x]['h']#put in a array:
            try:
                val = self.data['executions'][x]['e']#put in a array:
                if val is not None:#put in a array:
                    e_list.append(self.data['executions'][x]['e'])#put in a array:
                else:
                    val = 0
                    e_list.append(val)
            except:
                    val = 0
                    e_list.append(val)#put in a array:
            x += 1
        x = 0
        while x < max:
            #print data['executions'][x] #line 1
            #temp_a = data['executions'][x]['a']#put in a array:
            #temp_b = data['executions'][x]['b']#put in a array:
            #temp_h = data['executions'][x]['h']#put in a array:
            try:
                val = self.data['executions'][x]['g']#put in a array:
                if val is not None:#put in a array:
                    g_list.append(self.data['executions'][x]['g'])#put in a array:
                else:
                    val = 0
                    g_list.append(val)
            except:
                    val = 0
                    g_list.append(val)#put in a array:
            x += 1
        #Return a dictionary:
        return {'a':a_list,'b':b_list,'h':h_list,'e':e_list,'g':g_list}

    def do_lists(self, arg):
        "Function Do lists:"
        x = 0
        max = len(self.data['executions'])
        ##Couting a:
        a_list = []
        #shows:
        while x < max:
            #print data['executions'][x] #line 1
            a_list.append(self.data['executions'][x]['a'])#put in a array:
            x += 1
            
        #print(len(a_list))
        #print(a_list)

        ##Couting b:
        x = 0
        b_list = []
        #shows:
        while x < max:
            #print data['executions'][x]['b'] #line 1
            b_list.append(self.data['executions'][x]['b'])#put in a array:
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
                val = self.data['executions'][x]['h']
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
                val = self.data['executions'][x]['f']
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
        
        if(arg is 'e'):
            print("run")
            return e_list

        if(arg is 'h'):
            return h_list
        
        if(arg is 'f'):
            return f_list
           
        return arg

        #print len(item_dict['executions'][1]['a'])
    #This function takes a metric as argument and relate with timestamp
    def do_lists_timestamp(self, metric):
        "Function Do lists:"
        x = 0
        max = len(self.data['executions'])
        ##Couting a:
        metric_list = []
        #shows:
        while x < max:
            #print data['executions'][x] #line 1
            temp = []
            
            temp.append(self.data['executions'][x]['b'])#timestamp
            temp.append(self.data['executions'][x][metric])#a: duration, b, timestamp, 
            metric_list.append(temp)#put in a array, metric can be 
            x += 1
            
        #print(len(a_list))
        #print(metric_list)

        return metric_list

    #This function takes a list and a metric and makes a list
    def do_list_from_list(self, list_full, metric):
        "Function Do lists:"
        x = 0
        max = len(self.data['executions'])
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
    def do_list_full(self):
        "Function does list full:"
        x = 0
        max = len(self.data['executions'])
        ##Couting a:
        full_list = []
        #shows:
        while x < max:
            #print data['executions'][x] #line 1
            temp = []
            for metric in self.data['executions'][x]:
                temp.append(self.data['executions'][x][metric])#timestamp
                
            full_list.append(temp)#put in a array, metric can be 
            x += 1
            
        #print(len(a_list))
        #print(full_list)
        return full_list

    ##This function takes a list as argument and plots:
    def do_graph(self,a,kind):
        "Function Do lists:"
        #a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
        counts = Counter(a)
        df = pd.DataFrame.from_dict(counts, orient='index')
        #plt.figure();
        #df.plot(kind=kind)
        #plt.show()
            
        # saves the current figure into a pdf page

    ##This function takes a list as argument and returns a histogram:
    def do_histogram_withTimestamp(self, lista): #[[a,b],[a,b]]
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
    def do_histogram(self, a):
        "Function Do histogram:"
        #a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
        counts = Counter(a)
        #df = pd.DataFrame.from_dict(counts, orient='index')
        #df.plot(kind='barh')
        #plt.show()
        #print(counts)
        return counts

    #this function takes a histogram and creates a csv file:
    def create_csf(self, mylist, fname):
        #print("Creating a CSV File")
        with open(fname, "wb") as f:
            writer = csv.writer(f)

            #writer.writeheader()
            #writer.writeheader("Value","Quantity")
            writer.writerows(mylist)

    #this function creates a array:
    def create_array(self, mylist):
        p = []
        for letter in mylist:
            a = [letter, mylist[letter]]
            p.append(a)
        print p
        return p #p is an array of arrays: [[4,7],[85,1] ...]


    #this function open a csv file:
    def open_csf(self,fname):
        #print("Open CSV File")
        with open(fname) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')

            lines = []
            for row in readCSV:
                value = row[0]
                quantity = row[1]
                
                print(value + " " + quantity)
        
    #this function plot the histogram as graph:
    def print_graph(self, lista):
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
        
        #plt.scatter(x,y)
        #plt.show()
        
    #This function creates a SVC and classify:
    def SVM(self, a,b,lista,x_axis):
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
        #plt.plot(lista),# linewidth=5.0)
        #plt.subplot(1, 1, 1)
        #plt.ylabel('Quantity')
        #plt.xlabel(x_axis)
        #plt.title('SVM')

        #plt.scatter(lista[:, 0], lista[:, 1], c = y)
        #plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')

        #plt.plot([21, 21], [0, 400], 'k-', lw=2)
        #plt.legend()

        #plt.savefig("myfig.jpg") save in jpg
        #plt.show()

        
        return {'OPT':opt_list, 'NOPT':nopt_list} #return the two lists for later analysis
    #This function creates a SVC and classify:
    def SVM_2(self, a, b, lista, x_axis):
        X = [[0,0], [50,0], [2,5], [200,0]] #X = [[150,0],[151,0]] #an array X of size [n_samples, n_features] holding the training samples
        y = [0, 1, 2, 3]#y = ["OPT","NOPT"] # of class labels (strings or integers)
        clf = svm.SVC(decision_function_shape='ovo') #clf = svm.SVC(kernel='linear', C=1.0) #svm.SVC(kernel='rbf')#
        clf.fit(X, y)
        
        clf.decision_function_shape = "ovr"
        dec = clf.decision_function([[1,0]])
        dec.shape[1]#4 classes
        
        print("Lista:")
        print(lista)
        #plt.plot(lista),# linewidth=5.0)
        #plt.subplot(1, 1, 1)
        plt.ylabel('Quantity')
        #plt.xlabel(x_axis)
        plt.title('SVM')

        #plt.scatter(lista[:, 0], lista[:, 1], c = y)
        #plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')

        #plt.plot(lista)
        #plt.legend()
        #plt.show()
        #plt.savefig("myfig.jpg") in jpg
        
        return {'MOPT':mopt_list,'OPT':opt_list, 'NOPT':nopt_list} #return the two lists for later analysis
    #Function svc shape ovo example
    def svm_ovo(self):
        X = [[0,0], [1,0], [0,1], [1,1]]
        Y = ['A','B','C','D']
        clf = svm.SVC(decision_function_shape='ovo')
        clf.fit(X, Y) 
        
        #dec = clf.decision_function([[1]])

        point = [1,0]
        ans = clf.predict(point)

        #print"Prediction %s" % ans

        if ans == 'A':
            color = 'r'
        if ans == 'B':
            color = 'c'
        if ans == 'C':
            color = 'y'
        if ans == 'D':
            color = 'm'
            
        #plot_point_color(point[0], point[1], color, 500) # tem que mandar todos de uma vez, se mandar cada um da problema - plot_point_color(point[1], point[0], 'm', 500)
        #print(dec.shape[2]) # 4 classes: 4*3/2 = 6
        
        #clf.decision_function_shape = "ovr"
        #dec = clf.decision_function([[2]])
        #print(dec.shape[2])
        
    def svm_ovo_applied(self, list_x, list_y, list_points):
        "Function svc shape ovo applied"
        X = list_x#[list_x[0], list_x[1], list_x[2],list_x[3]] #[[0,0],[1,0],[0,1],[1,1]]
        Y = list_y#[list_y[0],list_y[1],list_y[2],list_y[3]] #['A','B','C','D']
        clf = svm.SVC(kernel='rbf')
        clf.fit(X, Y) 
        
        #dec = clf.decision_function([[1]])

        #predict list of points
        #print(list_points)
        ans = clf.predict(list_points)

        if ans == 'A':
            color = 'r'
        if ans == 'B':
            color = 'c'
        if ans == 'C':
            color = 'y'
        if ans == 'D':
            color = 'm'
        #print(ans)
        return color

    #plot a point and color
    def plot_point_color(self,axis_x, axis_y, choose_color,s):
        # Generate data...
        colors = ['b', 'c', 'y', 'm', 'r']
        x = 0
        sc = 0
        for each in colors:
            if each is choose_color:
                sc = x
            x+=1
        
        #example = plt.scatter(axis_x, axis_y, marker='x', color=x,s=s)

        #plt.show()

    #print a list and color:
    def plot_point_color(self,liste): #[[1,2,'color'],[1,2,'color']]
        # Generate data...
        #[[x,y],[x,y],[x,y]]
        colors = ['b', 'c', 'y', 'm', 'r']
        x = 0
        sc = 0

        #print("Liste")
        #print(liste)
        for each in liste: #[[1],[2]]
            print(each)
            #plt.scatter(each[0], each[1], marker='o', color=each[2],s=200)#,s=s)
        
        #plt.show()
                                        
                                                                
    #search a list inside another:
    def show_list(self,list_metric):
        list_selected = []

        for each in list_metric: 
            list_selected.append(each[0][0]) #returns
         
        return list_selected;

    #search a list inside another:
    def search_list(self,list_full, list_metric,metric):
        list_selected = []

        comparing_list = show_list(list_metric)

        max = len(self.data['executions'])
        for each in comparing_list:
            #print (each)
            #rodar a lista completa
            x = 0
            while x < max:
                #comparar
                aux = self.data['executions'][x][metric]
                #print aux
                if each is aux: #can b 
                    #pegar oq eh igual com each:
                    list_selected.append(self.data['executions'][x])
                
                x+=1
             
        return list_selected;

    #takes this list and brings a list:
    def search_list_in_list(self,list_metric,metric):

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


    #This fuction calculates the mean of
    def list_samples(self,list_result_opt):

        x = 0
        #print(data['stacks'])
        for each in self.data['stacks']:
            print(self.data['stacks']['151']['f'])
            x+=1
                
        return list_result_opt

    #this function creates a list of metrics inside the json:
    def do_list_metrics(self):
        "Function does list full:"
        x = 0
        max = len(data['executions'])
        ##Couting a:
        metrics_list = []
        temp = []
        while x < max:
            for metric in self.data['executions'][x]:
                if not metric in metrics_list:
                    metrics_list.append(metric)
            x+=1
        
        return metrics_list

    #this function creates a function of 2 metrics:
    def merge_metrics(self,list1, list2, list3):
        list_result = []
        #print(list1)
        #print(list2)
        #print(list3)

        if len(list3) > 0:
            x = 0
            while x < len(list1):
                list_result.append([list1[x], list2[x],list3[x]])
                x+=1
        else:
            x = 0
            while x < len(list1):
                list_result.append([list1[x], list2[x]])
                x+=1
                
        return list_result
            
    def print_function(self,list, metric):
        print (metric)
        print list[metric];
        
    def takes_list_gives_svm_ovo_result(self, list_x, list_y, example):
        "This function takes a list and gives the svm result "
        temp = []
        for each in example:
            ans = 0
            ans = self.svm_ovo_applied(list_x,list_y,each)
            #ans_color = translate_group_color(ans)
            temp.append([each[0],each[1],ans])
            
        for each in temp:
            print(each)
            
        return temp

    #Build dictionary from a generic list:
    def build_groups(self,temp):
        dic ={}
        list_a =[]
        list_b =[]
        list_c =[]
        list_d =[]
        for each in temp:
            if each[2] == 'r':
                list_a.append([each[0],each[1]])
            if each[2] == 'c':
                list_b.append([each[0],each[1]])
            if each[2] == 'y':
                list_c.append([each[0],each[1]])
            if each[2] == 'm':
                list_d.append([each[0],each[1]])

        return {'A':list_a,'B':list_b,'C':list_c,'D':list_d}
    
    def write_csv(self,file,info):
        with open(file, 'wb') as testfile:
            csv_writer = csv.writer(testfile)
            list_a = info['A']
            list_b = info['B']
            list_c = info['C']
            list_d = info['D']
            
            for row in list_a:
                csv_writer.writerow(row)
                
            for row in list_b:
                csv_writer.writerow(row)
                
            for row in list_c:
                csv_writer.writerow(row)
                
            for row in list_d:
                csv_writer.writerow(row)
            
    #test function:        
    def write(self, file, save):
        
        #save = [['A','B','C','D'],['1092','6','1','0'],['13','15','13','15']]
        length = len(save[0])

        with open(file, 'wb') as testfile:
            csv_writer = csv.writer(testfile)
            for y in range(length):
                csv_writer.writerow([x[y] for x in save])

    def write_groups_csv(self, csv, ans,y):
        aux = []
        aux.append(len(ans['A']))
        aux.append(len(ans['B']))
        aux.append(len(ans['C']))
        aux.append(len(ans['D']))
    
        list_groups = []
        if y is not 'N':
            list_groups.append(['A','B','C','D'])
        list_groups.append(aux)

        #print(list_groups)
        self.write(csv,list_groups)
    
        #print aux
        
    
                
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
#tests unitario:
#Classes:
analysis = trace_analysis('data/prototipo.json',1,'N')
teste = analysis.do_lists('a')
print(len(teste))

print(analysis.merge_metrics([1,2,3],[5,6,7],[]))
#plot_point_color(3,2,'b',50)
#svm_ovo()
#define the groups of test
list_x = [[0,0],[50,0],[150,0],[6,6],[10,10],[100,0],[100,10],[0,5],[0,10],[350,0],[250,0],[359,10],[340,10]]
list_y = ['A','A','A','B','B','B','B','C','C','D','D','D','D']
#define the test to be applied
example = [[0, 0], [5, 5], [8, 8], [5, 5], [6, 6], [5, 5], [350, 0],[150,0],[300,10],[310,10]]
ans = analysis.takes_list_gives_svm_ovo_result(list_x, list_y, example)
#print the ans
analysis.plot_point_color(ans)# which call for color_list([[1,2,'A'],[1,2,'A']])) -< [1,2,'b']
ans = analysis.build_groups(ans)
#analysis.write_csv("data/test.csv",analysis.build_groups(ans))
analysis.write_groups_csv("data/test.csv", ans,'N')
