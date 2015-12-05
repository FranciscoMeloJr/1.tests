#args:
import sys

#This will execute a json comparison and give the groups:
from main_module import *


def main(argv):
    if sys.argv[1] is not None:
        Json = sys.argv[1]
        if sys.argv[2] is not None:
            Csv= sys.argv[2]
    else:
        Json = 'data/open1000.json'
        Csv = 'data/test.csv'
        
    dic_groups = func_do_script(Json,Csv)

    print(len(dic_groups['A']))
    print(len(dic_groups['B']))
    print(len(dic_groups['C']))
    print(len(dic_groups['D']))
    
    func_save_csv(Json, Csv, dic_groups)

    test2 = 'data/open1001.json'
    dic_groups = func_do_script(test2)
    print(len(dic_groups['A']))
    print(len(dic_groups['B']))
    print(len(dic_groups['C']))
    print(len(dic_groups['D']))

if __name__ == "__main__":
   main(sys.argv[1:])
