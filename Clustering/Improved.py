from random1 import RANDOM
from KMeans_Plus import K_MEANS_PLUS
from Subtractive_Clustering import SUBTRACTIVE
import numpy as np
import cv2
import math as m
import time

def distance(Datapoint , Initial , Channels ):
    """
    Description : The Given Function 'distance' Is Used To Generate Euclidean Distance Between All Datapoints (Pixel Intensity)
              And Initial Centroid.
    Parameters : The Following Function Has 3 Parameters 
                 Datapoint - It Returns The Value Of Each Datapoints Whenever Called 
                 Initial - It Returns The Value Of Initial Centroid Whenever Called
                 Channels - It Returns Number Of Channels Present In Image
    Formulae : Consider An RGB Format Of An Image Therefore Distance Is Calculated As :
               dis = sqrt((R1-R2)^2 + (G1-G2)^2 + (B1-B2)^2)
               where,
               R1,G1,B1 - RGB Pixel Intensity Of Given Datapoint
               R2,G2,B2 - RGB Pixel Intensity Of Initial Centroid Choosen
    Variables : sum - 'sum' Is Used To Store Square Of Difference Of Pixel Values Of Datapoints And Inital Cluster Centroid
                dis - 'dis' Is Used To Store Square Root Of Sum Calculated (Final Euclidean Distance)
    Returns : It Returns Variable 'dis' Which Returns The Final Calculated Euclidean Distance
    """
    sum = 0
    for p in range(Channels):
        sum += (Datapoint[p] - Initial[p])**2
    dis = m.sqrt(sum)
    return dis

def K_MEANS_IMPROVED(path,K,Initialiser = 2):
    """
    Description : Function 'K_MEANS_IMPROVED' Is Used To Generate Image On Which K-Clusters Are Generated Using K-Means Improved
                  Code.It Finally Displays Clustered Image Along With Time Taken For Iteration
    Parameters : The Following Function Has 3 Parameters 
                 path - It Returns The Path Of Image On Which Improved K-Means Clustering Is To Be Performed
                 K - It Returns The Number Of Cluster Which Are To Be Formed In Image
                 Initialiser - To Select Method To Decide Random Initial Centroid 
                               By Default We Will Be Using K-Means++ For Initial Initialisation 
    Formulae : We Have Utilised K-Means Improved Algorithm As Explained Earlier
    Variables : cluster_x - It Is A List Which Is Used To Store x Coordinate Of A Pixel In Its Respective Cluster
                cluster_y - It Is A List Which Is Used To Store y Coordinate Of A Pixel In Its Respective Cluster
                initial_centroids - It Is An Array Storing Initial Cluster Centroids
                final_centroids - It Is A n Array Storing Final Cluster Centroids
                h,w,c - Height , Width , Channels Of An Image
                center_distance - It Is An Array Which Stores Euclidean Distance Of A Pixel From Each Inital Centroids
                store - It Is Used To Store Pixel Value Of Each Pixel Of An Image
                flag,count,counter - Are Used As Flagging Variable
                array_check - It Is An Array Which Is Used For Stopping Continous Iteration For K-Means Clustering
                cluster_label - It Is A List Used For Storing Label/Part Of A Cluster To Which Pixel Belongs
                cluster - It Is A List Of Storing Pixel Values Of Datapoints In Its Respective Clusters
                initial_distance - It Is A List Used To Store Initial Distance
    Returns : The Following Function Generates Final Clustered Image. Hence No Value Is Returned.
    """
    
    image = cv2.imread(path)
    image1 = np.copy(image)

    start = time.time()
    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    
    initial_centroids = np.zeros([K,c],float)
    final_centroids = np.zeros([K,c],float)

    array_check = np.zeros([K,c],bool) # Array To Check Difference In Old And New Cluster Centroids

    if(Initialiser==0):
        initial_centroids = SUBTRACTIVE(image,K)
    elif(Initialiser==1):
        initial_centroids = RANDOM(K)
    else:
        initial_centroids = K_MEANS_PLUS(image,K)
    
    initial_centroids = np.array(initial_centroids)
    dis = np.zeros(c,float)
    center_distance = np.zeros(K,float)
    
    flag = 0
    count = 0
    
    initial_distance = [] 
    cluster_label = []

    while(flag == 0):
        
        cluster_x = []
        cluster_y = []
        cluster = []
        for y in range (K):
            cluster_x.append([])
            cluster_y.append([])
            cluster.append([])
        counter = 0
        for i in range(h):
            for j in range(w):
                
                if(count!=0):

                    old_cluster = cluster_label[counter]
                    for chan in range(c):
                        dis[chan] = image[i,j,chan]
                    find = distance(dis , initial_centroids[old_cluster] , c)
                    
                    if(find <= initial_distance[counter]):
                        cluster_label[counter] = old_cluster
                        initial_distance[counter] = find
                        cluster_x[old_cluster].append(i)
                        cluster_y[old_cluster].append(j)
                        for chan in range(c):
                            cluster[old_cluster].append(image[i,j,chan])

                    else:
                        for l in range(K):
                            for chan in range(c):
                                dis[chan] = image[i,j,chan]
                            center_distance[l] = distance(dis , initial_centroids[l] , c )
                        initial_distance[counter]=min(center_distance)
                        mdis = min(center_distance)

                        for k in range(K):
                            if(mdis == center_distance[k]):
                                cluster_x[k].append(i)
                                cluster_y[k].append(j)
                                cluster_label[counter]=k
                                for chan in range(c):
                                    cluster[k].append(image[i,j,chan])
                       
                else : 
                    
                    for l in range(K):
                        for chan in range(c):
                            dis[chan] = image[i,j,chan]
                        center_distance[l] = distance(dis , initial_centroids[l] , c )
                    initial_distance.append(min(center_distance))
                    mdis = min(center_distance)

                    for k in range(K):
                        if(mdis == center_distance[k]):
                            cluster_x[k].append(i)
                            cluster_y[k].append(j)
                            cluster_label.append(k)
                            for chan in range(c):
                                cluster[k].append(image[i,j,chan])
                    continue
                counter+=1

        count=1
        # To Find New Cluster Centroid By Taking Mean
        for m in range(K):
            arr = np.array(cluster[m])
            for chan in range(c):
                final_centroids[m,chan]=np.sum(arr[chan : :c]) / (len(cluster[m])/c)
        
        # To Check Whether New Cluster Centroid Is Similar To Old One Or Not
        for t in range(K):
            for p in range(c):
                if((final_centroids[t,p]-initial_centroids[t,p])<1 and (final_centroids[t,p]-initial_centroids[t,p])>-1):
                    array_check[t,p] = True

        if(array_check.all()==True):
            flag = 1
        else:
            flag = 0
            for q in range(K):
                initial_centroids[q]=final_centroids[q]

    # To Print Final Image
    store = np.zeros(c,float)
    for t in range(K):
        for p in range(len(cluster_x[t])):
            for chan in range(c):
                store[chan] = final_centroids[t,chan]
            image1[cluster_x[t][p],cluster_y[t][p]] = store
    end = time.time()
    print("The time of execution of above program is :",(end-start), "s")
    cv2.imshow("Final Image",image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()