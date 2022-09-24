import numpy as np
dis = []
clust = []
K = int(input("Enter Number Of Clusters : "))
R = 0
while R <=10:
    Centers=np.random.randint(0,255,size=(K,3))
    clust.append(Centers)
    distance = 0
    for i in range(1,K):
        arr = np.sqrt(np.sum((Centers[i]-Centers[i-1])**2))
        distance += arr
    dis.append(distance)
    R +=1
max_value = max(dis)
index = dis.index(max_value)
centroid = clust[index]
print(centroid)
