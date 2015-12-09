#To be able to read csv formated files, we will first have to import the
#image:
import Image

#argv sys module
import sys

#csv module.
import csv

#plot:
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def read(file):
    line = []
    i = 0
    ans = []
    with open(file, 'rb') as f:    
        reader = csv.reader(f)
        for row in reader:
            ans.append(mod(i, row))
            i+=1
    return ans

def mod(c, line):
    #print c, line
    new_line = []
    aux = []
    #[[c,each],[c,each]]
    new_line.append([c,line])

    return new_line[0]

def draw(total):
    #total = [[2,[3,4,5,6]], [1,[13,14,15,16]]] #lista total  [[2,[3,4,5,6]], [2,[3,4,5,6]]]
    print total
    for cada in total:
        example = cada #[2,[3,4,5,6]] #each
        #print example

        color_group = 1
        
        max_point = []
        min_point = []
        max = 0
        min = 10000
        for each in example[1]:
            if(int(each) > max):
                max = each
                max_point = [example[0],each]
                
            if(each < min):
                min = each
                min_point = [example[0],each]
                
            if color_group%4 == 0:
                plt.plot(example[0], [each], 'ro', color = 'k')#, label='A')
            if color_group%4 == 1:
                plt.plot(example[0], [each], 'ro', color = 'b')#, label='B')
            if color_group%4 == 2:
                plt.plot(example[0], [each], 'ro', color = 'g')#, label='C')
            if color_group%4 == 3:
                plt.plot(example[0], [each], 'ro', color = 'm')#, label='D')
            color_group += 1
         #   print(example[0], [each])

    ##legend:
    plt.plot(0, 0, 'ro', color = 'k', label='A')
    plt.plot(0, 0, 'ro', color = 'b', label='B')
    plt.plot(0, 0, 'ro', color = 'g', label='C')
    plt.plot(0, 0, 'ro', color = 'm', label='D')

    plt.title('Classification groups x running with videos')
    
    plt.legend(loc='best')
    
    print(max_point)
    print(min_point)
    
    plt.ylabel('Quantities of each group: A, B,C and D')
    plt.xlabel('Each run')
    #plt.show()

    plt.savefig('testplot.png')
    Image.open('testplot.png').save('testplot.jpg','JPEG')
    
def main(argv):
    if len(argv)== 0:
        input = 'data/test.csv'
    else:
        input = argv[0]

    ans = read(input)
    draw(ans)

if __name__ == "__main__":
   main(sys.argv[1:])

