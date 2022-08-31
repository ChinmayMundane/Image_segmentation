from re import X
import numpy as np
import math as m
import cv2


image=cv2.imread("I:\image segmentation\image4.png")
K1 = input("No. Of Clusters : ")
K = int(K1)
h,w,c=image.shape
X = image.ndim

Clusters=np.random.randint(0,255,size=(K,3))
print('init clusters', Clusters)

img=image.copy()
diff = np.zeros(K,int)
a1 = np.zeros([K,X],int)
array_check = np.zeros([K,c],bool)


# initialized random K points forming K centroids
# and assigned each point of the image to that centroid
# based on the difference of the points to clusters 
# and assigning points to that centroid which has lowest
# distance between itself and points.

for i in range(h):
    for j in range(w):
        pnt=img[i][j]
    
        for l in range(K):
            diff[l]=np.sqrt(np.sum(Clusters[l]-pnt)**2)
            
        cent= np.argmin(diff)
        img[i][j]=Clusters[cent]

flag = 0

# Compute the centroids for the clusters by taking 
# the average of the all data points that belong to each cluster
# and assigning the points to that new cluster formed, if any.
while(flag == 0):
    for m in range(K):
        arr = np.array(Clusters[m])
        for c in range(X):
            a1[m,c]=int(((np.sum(arr[c: :X])) / ((len(Clusters[m]))/X)))

    


    for i in range(h):
        for j in range(w):
            pnt=img[i][j]
    
            for l in range(K):
                diff[l]=np.sqrt(np.sum(a1[l]-pnt)**2)
            
            cent= np.argmin(diff)
            img[i][j]=a1[cent]

    for t in range(K):
            for p in range(X):
                if((a1[t,p]-Clusters[t,p])<5):
                    array_check[t,p] = True

    if(array_check.all()==False):
        flag = 0
        for q in range(K):
            Clusters[q]=a1[q]
    else:
        break
        
            
    



if __name__ == '__main__':
	cv2.imshow('original_image',image)
	cv2.imshow('cluster_image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



















	

