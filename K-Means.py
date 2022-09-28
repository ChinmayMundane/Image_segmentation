import numpy as np
import math as m
import cv2
import time
K = int(input("Enter Number Of Clusters : "))
image=cv2.imread("tester5.png")
h,w,c=image.shape[0],image.shape[1],image.shape[2]
Clusters=np.random.randint(0,255,size=(K,c))
print('init clusters', Clusters)
#img=image.copy()
img = image.copy()
dist = np.zeros(K,int)
centd = np.zeros(K,int)
new_cent = np.zeros([K,c],float)
array_check = np.zeros([K,c],bool)
start = time.time()
R=0
while R==0:
    b = []
    b1 = []
    b2 =[]
    for y in range (K):
        b.append([])
        b1.append([])
        b2.append([])
    for i in range(h):
        for j in range(w):
            pnt=img[i][j]
            for l in range(K):
                dist[l]=np.sqrt(np.sum((Clusters[l]-pnt)**2))
                    #dist[chan] = img[i,j,chan]
            centd = min(dist)

            for k in range(K):
                if(centd==dist[k]):
                    b1[k].append(i)
                    b[k].append(j)
                    for chan in range(c):
                        b2[k].append(img[i,j,chan])
                        

    for m in range(K):
        arr = np.array(b2[m])
        for chan in range(c):    
            new_cent[m,chan]=(((np.sum(arr[chan : :c])) / ((len(arr))/c)))
    for t in range(K):
            for p in range(c):
                if((new_cent[t,p]-Clusters[t,p]<1) and (new_cent[t,p]-Clusters[t,p]>-1)):
                    array_check[t,p] = True


    if(array_check.all() == True):
        R=1
    else:
        R=0
        for q in range(K):
            Clusters[q]=new_cent[q]
            print("iterating")

key = np.zeros(c,float)
for t in range(K):
    for p in range(len(b1[t])):
        for chan in range(c):
            key[chan] = new_cent[t,chan]
            img[b1[t][p],b[t][p]] = key
end = time.time()
print("The time of execution of above program is :",(end-start), "s")

cv2.imshow('original_image',image)
cv2.imshow('cluster_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





















	

