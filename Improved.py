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
    
    image = plt.imread("/home/smit/Desktop/Image_segmentation/test.png")
    image1 = np.copy(image)
    plt.imshow(image)
    plt.show()
    
    K1 = input("Enter Number Of Clusters : ")
    K = int(K1)
    start = time.time()
    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    
    a = np.zeros([K,c],float) # Array To Store Old Cluster Centroids
    a1 = np.zeros([K,c],float) # Array To Store New Cluster Centroids
    array_check = np.zeros([K,c],bool) # Array To Check Difference In Old And New Cluster Centroids

    for pos in range(K): # To Randomly Select K Initial Cluster Centroid
        for i in range(c):
            r_x = random.randint(0,h-1)
            r_y = random.randint(0,w-1)
            a[pos,i]=image[r_x,r_y,i]

    dis = np.zeros(c,float)
    cendis = np.zeros(K,float)
    flag = 0

    count = 0
    sdis = [] # 1st Data Type To Store Inital Distance
    cluster = [] # 2nd Data Type To Store Cluster Label

    while(flag == 0):
        
        clust_x = []
        clust_y = []
        clust = []
        for y in range (K):
            clust_x.append([])
            clust_y.append([])
            clust.append([])
        counter = 0
        for i in range(h):
            for j in range(w):
                
                if(count!=0):

                    old_cluster = cluster[counter]
                    for chan in range(c):
                        dis[chan] = image[i,j,chan]
                    find = distance(dis , a[old_cluster] , c)
                    
                    if(find <= sdis[counter]):
                        cluster[counter] = old_cluster
                        sdis[counter] = find
                        clust_x[old_cluster].append(i)
                        clust_y[old_cluster].append(j)
                        for chan in range(c):
                            clust[old_cluster].append(image[i,j,chan])

                    else:
                        for l in range(K):
                            for chan in range(c):
                                dis[chan] = image[i,j,chan]
                            cendis[l] = distance(dis , a[l] , c )
                        sdis[counter]=min(cendis) # 1st Data Type To Store Inital Distance
                        mdis = min(cendis)

                        for k in range(K):
                            if(mdis == cendis[k]):
                                clust_x[k].append(i)
                                clust_y[k].append(j)
                                cluster[counter]=k # 2nd Data Type To Store Cluster Label
                                for chan in range(c):
                                    clust[k].append(image[i,j,chan])
                       
                else : 
                    
                    for l in range(K):
                        for chan in range(c):
                            dis[chan] = image[i,j,chan]
                        cendis[l] = distance(dis , a[l] , c )
                    sdis.append(min(cendis)) # 1st Data Type To Store Inital Distance
                    mdis = min(cendis)

                    for k in range(K):
                        if(mdis == cendis[k]):
                            clust_x[k].append(i)
                            clust_y[k].append(j)
                            cluster.append(k) # 2nd Data Type To Store Cluster Label
                            for chan in range(c):
                                clust[k].append(image[i,j,chan])
                    continue
                counter+=1

        count=1
        # To Find New Cluster Centroid By Taking Mean
        for m in range(K):
            arr = np.array(clust[m])
            for chan in range(c):
                a1[m,chan]=np.sum(arr[chan : :c]) / (len(clust[m])/c)
        
        # To Check Whether New Cluster Centroid Is Similar To Old One Or Not
        print("Iteration Complete")
        for t in range(K):
            for p in range(c):
                if((a1[t,p]-a[t,p])<0.01 and (a1[t,p]-a[t,p])>-0.01):
                    array_check[t,p] = True

        if(array_check.all()==True):
            flag = 1
        else:
            flag = 0
            for q in range(K):
                a[q]=a1[q]

    # To Print Final Image
    store = np.zeros(c,float)
    for t in range(K):
        for p in range(len(clust_x[t])):
            for chan in range(c):
                store[chan] = a1[t,chan]
            image1[clust_x[t][p],clust_y[t][p]] = store
    end = time.time()
    print("The time of execution of above program is :",(end-start), "s")
    plt.imshow(image1)
    plt.show()
    plt.imshow(image)
    plt.show()

reader()
