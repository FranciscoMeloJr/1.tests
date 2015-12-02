from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

def function3D():
    fig = plt.figure()
    AX = fig.add_subplot(111, projection='3d')

    X = [1,2,3,4,5,6,7,8,9,10]
    Y = [5,6,7,3,3,5,7,9,11,8]
    Z = [2,3,3,3,5,7,9,11,9,10]

    AX.scatter(X,Y,Z,c='r', marker='o')

    AX.set_xlabel('x label')
    AX.set_ylabel('y label')
    AX.set_zlabel('z label')

    plt.show()
#Plot in 3d each axis:
def function3D_args(X,Y,Z,metric):
    fig = plt.figure()
    AX = fig.add_subplot(111, projection='3d')

    metric = translate(metric)
    
    #X = [1,2,3,4,5,6,7,8,9,10]
    #Y = [5,6,7,3,3,5,7,9,11,8]
    #Z = [2,3,3,3,5,7,9,11,9,10]

    AX.scatter(X,Y,Z,c='r', marker='o')

    AX.set_xlabel(metric[0])
    AX.set_ylabel(metric[1])
    AX.set_zlabel(metric[2])

    plt.show()

#Function that translate each metric in 
def translate(metric):

    new_metrics = metric
    i = 0
    for each in metric:
        if each is 'a':
            new_metrics[i] = 'duration'
        if each is 'b':
            new_metrics[i] = 'timestamp'
        if each is 'h':
            new_metrics[i] = 'wait-blocked'
        if each is 'f':
            new_metrics[i] = 'interrupted'
        if each is 'g':
            new_metrics[i] = 'wait-cpu'
        if each is 'e':
            new_metrics[i] = 'run'
        i+=1
    return new_metrics

def hello():
    print "Hello, World!"
