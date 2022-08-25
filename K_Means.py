import random 
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math as m


# To Calculate Distance
def distance(array , array1 , a ):
    sum = 0
    for p in range(a):
        sum += (array[p] - array1[p])**2
    b = m.sqrt(sum)
    dis = int(b)
    return dis



# Reading Image
def reader():
    
    image = plt.imread("/home/smit/Desktop/Image_segmentation/Trial.jpg")
    image1 = np.copy(image)
    plt.imshow(image)
    plt.show()
    
    K1 = input("Enter Number Of Clusters : ")
    K = int(K1)
    
    c = image.ndim 
    h,w = image.shape[0],image.shape[1]
    
    a = np.zeros([K,c],int)
    a1 = np.zeros([K,c],int)
    array_check = np.zeros([K,c],bool)

    for pos in range(K):
        for i in range(c):
            r_x = random.randint(0,h-1)
            r_y = random.randint(0,w-1)
            a[pos,i]=image[r_x,r_y,i]

    dis = np.zeros(c,int)
    cendis = np.zeros(K,int)
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
                    for chan in range(c):
                        if(mdis == cendis[k]):
                            clust_x[k].append(i)
                            clust_y[k].append(j)
                            clust[k].append(image[i,j,chan])

        for m in range(K):
            arr = np.array(clust[m])
            for chan in range(c):
                a1[m,chan]=int(((np.sum(arr[chan : :c])) / ((len(clust[m]))/c)))
        
        print("Iteration Complete")
        for t in range(K):
            for p in range(c):
                if((a1[t,p]-a[t,p])<5 and (a1[t,p]-a[t,p])>-5):
                    array_check[t,p] = True

        if(array_check.all()==True):
            flag = 1
        else:
            flag = 0
            for q in range(K):
                a[q]=a1[q]

    store = np.zeros(c,int)
    for t in range(K):
        for p in range(len(clust_x[t])):
            for chan in range(c):
                store[chan] = a1[t,chan]
            image1[clust_x[t][p],clust_y[t][p]] = store

    plt.imshow(image1)
    plt.show()
    plt.imshow(image)
    plt.show()

reader()