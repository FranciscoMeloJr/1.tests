#args:
import sys

#This will execute a json comparison and give the groups:
from main_module import *


def main(argv):
    if sys.argv[1] is not None:
        name = sys.argv[1]
    else:
        name = 'open1000.json'
        
    dic_groups = func_do_script(name)
    print(len(dic_groups['A']))
    print(len(dic_groups['B']))
    print(len(dic_groups['C']))
    print(len(dic_groups['D']))

    dic_groups = func_do_script('open1001.json')
    print(len(dic_groups['A']))
    print(len(dic_groups['B']))
    print(len(dic_groups['C']))
    print(len(dic_groups['D']))

if __name__ == "__main__":
   main(sys.argv[1:])
