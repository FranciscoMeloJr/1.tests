from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

def test_3D():
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

test_3D()
