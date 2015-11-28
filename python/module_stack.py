#Module for stack arithmetics:
#CSV:
import csv

#Json:
import json
from pprint import pprint

with open('test3.json') as data_file:    
    data = json.load(data_file)


#This fuction calculates the man of
def list_samples():

    x = 0
    #print(data['stacks'])

    print(data['stacks']['84']) #  dictionary
    print(data['stacks']['84']['f']) # [thread]
    print(data['stacks']['84']['b']) # 0
    print(data['stacks']['84']['f']) # [thread]

    print(data['stacks']['85']['b']) # 0
    print(data['stacks']['85']['f']) # [thread]
    
    for each1 in data['stacks']: #each1 = numero
        print("%s b is %s and f is %s  " % (each1,data['stacks'][each1]['b'], data['stacks'][each1]['f']))
    #return list_result_opt

#This function translates a list:
def translate_samples(lista):

    #{86,85,85,83}
    print("I got in")
    list_translated = []
    x = 0
    max = len(lista)
    while x < max:
        print(lista[x])
        x+=1
        
    for each1 in data['stacks']: #each1 = numero
        x = 0
        while x < max:
            elem = lista[x]
            if int(each1) is elem:
                print(type(elem))
                print (type(data['stacks'][each1]['f']))
                list_translated.append(data['stacks'][each1]['f'])
            x+=1
        #print("%s b is %s and f is %s  " % (each1,data['stacks'][each1]['b'], data['stacks'][each1]['f']))
    #return list_result_opt
    return list_translated

list_samples()
print(translate_samples([85,86]))

