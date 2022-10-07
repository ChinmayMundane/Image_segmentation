import numpy as np
import math as m
import random
import matplotlib.pyplot as plt

def calculations(array1,array2):
    difference = array1-array2
    square = difference**2
    sum = np.sum(square)
    root = m.sqrt(sum)
    return root

def trial():
    k=0
    xpoints = []
    ypoints = []
    clust_x = [[],[],[]]
    clust_y = [[],[],[]]

    while(k<200):
        x = random.randint(0,600)
        y = random.randint(0,600)
        xpoints.append(x)
        ypoints.append(y)
        k+=1

    plt.scatter(xpoints,ypoints)
    plt.show()

    dis = np.zeros(3,float)
    initial = np.zeros([3,2],float)
    new = np.zeros([3,2],float)

    for i in range(3):
        for j in range(2):
            initial[i,j]=random.randint(0,600)

    array = np.zeros(2,float)
    flag = 1

    while(flag == 1):
        for i in range(len(xpoints)):
            array[0] = xpoints[i]
            array[1] = ypoints[i]
            for l in range(3):
                dis[l] = calculations(array,initial[l])

            mdis = min(dis) 
            for j in range(3):
                if(mdis == dis[j] ):
                clust_x[j].append(xpoints[i])
                clust_y[j].append(ypoints[i])

        for j in range(3):
            cluster1 = np.sum(clust_x[j]) / len(clust_x[j])
            cluster2 = np.sum(clust_y[j]) / len(clust_y[j])
            new[j] = [cluster1,cluster2]
        print("Iteration Complete")
        if((new-initial).all() < 1 and (new-initial).all()>-1):
            array_check = True
        else:
            array_check =False

        if (array_check == True):
            flag = 0
        else:
            flag=1
            for p in range(3):
                inital[p] = new[p]

    vocabulary = 1
    my_colors = {1:'red',2:'green',3:'blue'}
    for j in range(3):
        plt.scatter(clust_x[j],clust_y[j],color = my_colors.get(vocabulary))
        vocanulary += 1

    plt.show()

trial()