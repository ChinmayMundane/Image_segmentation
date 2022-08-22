import numpy as np
import cv2
import matplotlib.pyplot as plt
import math as m


# To Calculate Distance
def distance(x,y,z,x1,y1,z1):
    a = (x-x1)**2 + (y-y1)**2 + (z-z1)**2 
    b = m.sqrt(a)
    dis = round(b)#
    return dis



# Reading Image
def reader():
    
    image = plt.imread("/home/smit/Desktop/Image_segmentation/Trial.jpg")
    image1 = np.copy(image)
    plt.imshow(image)
    plt.show()
    K1 = input("Enter Number Of Clusters : ")
    K = int(K1)
    a = np.array([[94,135,199],[54,128,79],[1,150,232],[75,86,118]])
    a1 = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
    dis = np.zeros(K,int)
    cendis = np.zeros(K,int)
    flag = 0
    h,w = image.shape[0],image.shape[1]
    while(flag == 0):
        clust_x = [[],[],[],[]]
        clust_y = [[],[],[],[]]
        clust = [[],[],[],[]] 
        for i in range(h):
            for j in range(w):
                for l in range(K):
                    cendis[l] = distance(image[i,j,0],image[i,j,1],image[i,j,2],a[l,0],a[l,1],a[l,2])
                mdis = min(cendis)

                for k in range(K):
                    if(mdis == cendis[k]):
                        clust_x[k].append(i)
                        clust_y[k].append(j)
                        clust[k].append(image[i,j,0])
                        clust[k].append(image[i,j,1])
                        clust[k].append(image[i,j,2])
        for m in range(K):
            arr = np.array(clust[m])
            a1[m,0]=int(((np.sum(arr[ : :3])) / ((len(clust[m]))/3)))
            a1[m,1]=int(((np.sum(arr[ 1: :3])) / ((len(clust[m]))/3)))
            a1[m,2]=int(((np.sum(arr[ 2: :3])) / ((len(clust[m]))/3)))
        
        print("Iteration Complete")
        if(np.array_equal(a,a1)):
            flag = 1
        else:
            flag = 0
            for q in range(K):
                a[q]=a1[q]
    

    for t in range(K):
        for p in range(len(clust_x[t])):
            image1[clust_x[t][p],clust_y[t][p]] = [a1[t,0],a1[t,1],a1[t,2]]

    plt.imshow(image1)
    plt.show()
    plt.imshow(image)
    plt.show()

reader()