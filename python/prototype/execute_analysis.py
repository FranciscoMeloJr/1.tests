#args:
import sys

#This will execute a json comparison and give the groups:
from main_module import *


def main(argv):
    print("Main Execute Analysis")
    print(argv)
    if len(argv)== 0:
        Json = 'data/open1000.json'
        Csv = 'data/test.csv'
    else:
        Json = argv[0]
        Csv = argv[1]
        
    dic_groups = func_do_script(Json,Csv)

    print(len(dic_groups['A']))
    print(len(dic_groups['B']))
    print(len(dic_groups['C']))
    print(len(dic_groups['D']))
    
    #test2 = 'data/open1001.json'
    #csv2 = 'data/test2.csv'
    #dic_groups = func_do_script(test2,csv2)

if __name__ == "__main__":
   main(sys.argv[1:])
