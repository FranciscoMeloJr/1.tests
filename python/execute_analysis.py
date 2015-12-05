from main_module import *

def execute():
    dic_groups = func_do_script('open1000.json')
    print(len(dic_groups['A']))
    print(len(dic_groups['B']))
    print(len(dic_groups['C']))
    print(len(dic_groups['D']))

    dic_groups = func_do_script('open1001.json')
    print(len(dic_groups['A']))
    print(len(dic_groups['B']))
    print(len(dic_groups['C']))
    print(len(dic_groups['D']))
execute()
