from KMEANS1 import code
from pcs import pcs
import random 
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math as m
import time

# To Calculate Distance
def distance(array , array1 , a ):
    sum = 0
    for p in range(a):
        sum += (array[p] - array1[p])**2
    b = m.sqrt(sum)
    dis = (b)
    return dis



# Reading Image
def reader():
    path = "/home/smit/Desktop/Image_segmentation/test.jpg"
    image = plt.imread(path)
    image1 = np.copy(image)
    plt.imshow(image)
    plt.show()

    image2 = pcs(image)
    
    K1 = input("Enter Number Of Clusters : ")
    K = int(K1)
    start = time.time()
     
    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    
    # a = np.zeros([K,c],float)
    a = np.array(code(image2,K))
    a1 = np.zeros([K,c],float)
    array_check = np.zeros([K,c],bool)

    dis = np.zeros(c,float)
    cendis = np.zeros(K,float)
    flag = 0

    while(flag == 0):
        
        clust_x = []
        clust_y = []
        clust = []
        for y in range (K):
            clust_x.append([])
            clust_y.append([]) 
            clust.append([])
        
        for i in range(h):
            for j in range(w):
                for l in range(K):
                    for chan in range(c):
                        dis[chan] = image[i,j,chan]
                    cendis[l] = distance(dis , a[l] , c )
                mdis = min(cendis)

                for k in range(K):
                    if(mdis == cendis[k]):
                        clust_x[k].append(i)
                        clust_y[k].append(j)
                        for chan in range(c):
                            clust[k].append(image[i,j,chan])

        for m in range(K):
            arr = np.array(clust[m])
            for chan in range(c):
                a1[m,chan]=(((np.sum(arr[chan : :c])) / ((len(clust[m]))/c)))
        
        for t in range(K):
            for p in range(c):
                if((a1[t,p]-a[t,p])<1 and (a1[t,p]-a[t,p])>-1):
                    array_check[t,p] = True

        if(array_check.all()==True):
            flag = 1
        else:
            flag = 0
            for q in range(K):
                a[q]=a1[q]

    store = np.zeros(c,float)
    for t in range(K):
        for p in range(len(clust_x[t])):
            for chan in range(c):
                store[chan] = a1[t,chan]
            image1[clust_x[t][p],clust_y[t][p]] = store
    end = time.time()
    cv2.imwrite("/home/smit/Desktop/Image_segmentation/Images/Original1.jpg",image1)
    print("The time of execution of above program is :",(end-start), "s")
    plt.imshow(image1)
    plt.show()
    plt.imshow(image)
    plt.show()

reader()