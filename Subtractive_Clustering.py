import numpy as np
import cv2
import matplotlib.pyplot as plt
import math as m
import time

def calculations(array1,array2):
    difference = array1 - array2
    dif = np.array(difference)
    square = (-4)*(np.sum(dif**2))
    power = square / (ra**2)
    value = m.exp(power)
    return value

def subtractive():
    ra = 0.35
    rb = 1.5*ra
    t=0
    image = plt.imread("/home/smit/Desktop/Image_segmentation/test.jpg")
    image1 = np.copy(image)
    plt.imshow(image)
    plt.show()
    start = time.time()

    K = int(input("Enter Number Of Clusters : "))
    count = K
    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    data = image.reshape(-1,c)
    pot = np.zeros(h*w , float)
    pixel = np.zeros(c,float)
    pixel1 = np.zeros(c,float)
    clust_x = []
    clust_y = []
    initial = []
    centroid = np.zeros(c,float)
    trial = 0
    for i in range(h):
        for j in range(w):
            clust_x.append(i)
            clust_y.append(j)
            #pot.append([])
    print("loop1")
    for x in range(len(data)):
        potential = 0.0
        for y in range(x+1 , len(data)):
            value = calculations(data[x],data[y])
            pot[x] += value
            pot[y] += value
        t+=1
        print(t)
    print("Loop2")
    
    while(count>0):
        maximum = max(pot) 
        index = pot.index(maximum)
        initial.append(image[clust_x[index],clust_y[index]])
        for chan in range(c):
            centroid[chan]=image[clust_x[i],clust_y[i],chan]
        
        for j in range(len(pot)):
            potential = 0.0
            for i in range(len(pot)):
                for chan in range(c):
                    pixel1[chan] = image[clust_x[i],clust_y[i],chan]
                
                value = calculations(centroid,pixel1)
                potential = potential + value
            pot[j] = pot[j] - (maximum*potential)
        
        count -= 1
        print("loop3")
    end = time.time()
    print(initial)
    print("The time of execution of above program is :",(end-start), "s")

subtractive()