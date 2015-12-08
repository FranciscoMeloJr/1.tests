#This process here will save the content in a permanent file:
import sys
import csv


def read_csv(file):
    f = open(file, 'rt')

    line_list = []
    
    try:
        counter  = 1
        line = []
        reader = csv.reader(f)
        for row in reader:
            line.append(row)
            if (counter%4 == 0):
                write_csv('data/test.csv',line)
                line = []
            counter+=1
           
    finally:
        f.close()
    return line_list

def write_csv(file,info):
    
    numbers = []
    for each in info:
            if each[0] is not None:
                numbers.append(int(each[0]))
            else:
                numbers.append(int(each))
    print numbers
    
    with open(file, 'a') as testfile:
        resultFile = open(file,'a')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow(numbers)
               
def call(input, output):
    ans = read_csv(input)
    write_csv(output,ans)

def main(argv):
    if len(argv)== 0:
        output = 'data/test.csv'
        input = 'data/save.csv'
    else:
        input = argv[0]
        output = argv[1]
    call(input,output)#'data/test2.csv')

if __name__ == "__main__":
   main(sys.argv[1:])
