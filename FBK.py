import random 
import numpy as np
import matplotlib.pyplot as plt
import math as m
import time
import cv2


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
    ER = 0.01
    image = cv2.imread("/home/smit/Desktop/Image_segmentation/Trial2.jpg")
    image1 = np.copy(image)
    cv2.imshow("Original",image)
    cv2.waitKey(5000)
    
    K = int(input("Enter Number Of Clusters : "))
    start = time.time()
     
    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    
    a = np.zeros([K,c],float)
    a1 = np.zeros([K,c],float)
    array_check = np.zeros([K,c],bool)

    for pos in range(K):
        for i in range(c):
            r_x = random.randint(0,h-1)
            r_y = random.randint(0,w-1)
            a[pos,i]=image[r_x,r_y,i]

    print(a)
    dis = np.zeros(c,float)
    cendis = np.zeros(K,float)
    flag = 0

    while(flag == 0):
        sum_distance = [0]*K
        validity = [0]*K
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
                        sum_distance[k]+=mdis
                        for chan in range(c):
                            clust[k].append(image[i,j,chan])

        average = sum(sum_distance)/K
        Rate = ER*average

        for p in range(K):
            validity[p] = int((sum_distance[p]-average)/Rate)

        print(validity)
        for p in range(K):
            
            
            if(validity[p]<0 and any(validity[q]>0 for q in range(K))):
                smallest = validity.index(min(validity))
                largest = validity.index(max(validity))
                a[smallest] = a[largest]
            
            
            elif(validity[p]>0):
                arr = np.array(clust[p])
                for chan in range(c):
                    a[p,chan]=(np.sum(arr[chan : :c])) / ((len(clust[p]))/c)
        
        print(a)
        print(" ")
        if(all(validity[q]==0 for q in range(K))):
            flag=1

    store = np.zeros(c,float)
    for t in range(K):
        for p in range(len(clust_x[t])):
            for chan in range(c):
                store[chan] = a[t,chan]
            image1[clust_x[t][p],clust_y[t][p]] = store
    end = time.time()
    print("The time of execution of above program is :",(end-start), "s")
    cv2.imshow("Final",image1)
    cv2.waitKey(10000)
reader()