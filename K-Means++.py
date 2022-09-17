import math as m
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def code():

    image = plt.imread("/home/smit/Desktop/Image_segmentation/Trial.jpg")
    image1 = np.copy(image)
    plt.imshow(image)
    plt.show()

    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    K = int(input("Enter Number Of Clusters To Be Formed : "))
    count = K
    x = random.randint(0,h+1)
    y = random.randint(0,w+1)
    pixel = np.zeros(c,float)
    pixel1 = np.zeros(c,float)
    
    for k in range(c):
        pixel[k] = image[x,y,k]
    
    initial_centroid = []
    initial_centroid.append(pixel)
    distance = []
    clust_x = []
    clust_y = []
    min_distance = []

    while(count>0):
        
        for i in range(h):
            for j in range(w):
                
                for chan in range(c):
                    pixel1[chan] = image[i,j,chan]
                
                for k in range(len(initial_centroid)):
                    distance.append(m.sqrt(np.sum((pixel1 - initial_centroid[k])**2)))
                
                mdis = min(distance)
                distance = []

                min_distance.append(mdis)
                clust_x.append(i)
                clust_y.append(j)
        
        maximum = max(min_distance)
        index = min_distance.index(maximum)
        
        for chan in range(c):
            pixel[chan] = image[ clust_x[index] , clust_y[index] , chan ]

        initial_centroid.append(pixel)
        count = count - 1

    print(initial_centroid)

code()