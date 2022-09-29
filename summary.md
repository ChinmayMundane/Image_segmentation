# About
For this project, we used many techniques to segment the image.First, we used kmeans algorithm which is a type of clustering based segmentation.
In later stages, to increase the time efficiency for segmenting the image, an improved version of kmeans was also used.

# Table of contents
 - [K-means clustering](#K-means-clustering)
   - [Steps](#Steps)
   - [Flowchart](#Flowchart)
   - [Disadvantages](#Disadvantages)
 - [Improved K-means](#Improved-K-means)
   - [Algorithm](#Algorithm)

- [Conclusion](#Conclusion)
- [References](#References)


# K-means clustering
Clustering is one of the most common exploratory data analysis technique used to get an intuition about the structure of the data.
clustering is nothing but identifying sub-groups(cluster) in the data which are very similar to each other.
For our project, we are using Kmeans which is considered as one of the most used clustering algorithms due to its simplicity.
Now you may ask what is kmeans?
Kmeans algorithm is an iterative algorithm that tries to partition the dataset into K pre-defined distinct non-overlapping subgroups (clusters) 
where each data point belongs to only one group. It tries to make the intra-cluster data points as similar as possible while also keeping the clusters 
as different (far) as possible. It assigns data points to a cluster such that the sum of the squared distance between the data points and the cluster’s 
centroid (arithmetic mean of all the data points that belong to that cluster) is at the minimum. The less variation we have within clusters,
the more similar the data points are within the same cluster.


## Steps
  Specify number of clusters K.\
  Initialize centroids by first shuffling the dataset and then randomly selecting K data points for the centroids without replacement.\
  Keep iterating until there is no change to the centroids. i.e assignment of data points to clusters isn’t changing.\
  Compute the sum of the squared distance between data points and all centroids.\
  Assign each data point to the closest cluster (centroid).\
  Compute the centroids for the clusters by taking the average of the all data points that belong to each cluster.

## Flowchart
![kmeans flowchart](https://user-images.githubusercontent.com/109454803/193004125-9cee19fc-4ee9-44c2-be0f-38b449c2cf90.png)



## Disadvantags
Though K-means is relatively simplier to implement, it has some disadvantages
1. It chooses k centroids manually.\
when we choose the centroids randomly , we are at a risk of 
increasing the runtime for our code. we solved this using some initialization method which are kmeans++, subtractive clustering,etc.
2. takes too much time.\
when appling kmeans we saw that it took too much time to run .So , we searched for some alternate ways.
finally we found improved kmeans which claimed to reduce time significantly.


# Improved K-means
while Kmeans takes a little too much of a time, improved kmeans is more time efficient and is more accurate.
The main idea of algorithm is to 
set two simple data structures to retain the labels of cluster and 
the distance of all the data objects to the nearest cluster during the 
each iteration, that can be used in next iteration, we calculate the 
distance between the current data object and the new cluster 
center, if the computed distance is smaller than or equal to the 
distance to the old center, the data object stays in it’s cluster that 
was assigned to in previous iteration. Therefore, there is no need 
to calculate the distance from this data object to the other k-1 clustering centers, saving the calculative time to the k-1 cluster 
centers. Otherwise, we must calculate the distance from the 
current data object to all k cluster centers, and find the nearest 
cluster center and assign this point to the nearest cluster center. 
And then we seperately record the label of nearest cluster center 
and the distance to it’s center. Because in each interation some 
data points still remain in the original cluster, it means that some 
parts of the data points will not be calculated, saving a total time 
of calculating the distance, thereby enhancing the efficiency of 
the algorithm. 

## Algorithm
1) Randomly select k objects from dataset D as initial cluster
centers.
2) Calculate the distance between each data object di (1 <=
i<=n ) and all k cluster centers cj (1<=j<=k) as Euclidean
distance d(di , cj) and assign data object di to the nearest cluster.
3) For each data object di, find the closest center cj and
assign di to cluster center j.
4) Store the label of cluster center in which data object di is
and the distance of data object di to the nearest cluster and store
them in array Cluster[ ] and the Dist[ ] separately.
Set Cluster[i] = j, j is the label of nearest cluster.
Set Dist[i]=d(di, cj), d(di, cj) is the nearest Euclidean
distance to the closest center.
5) For each cluster j (1<=j<=k), recalculate the cluster
center;
6) Repeat
7) For each data object di
Compute it’s distance to the center of the present nearest
cluster;
  a) If this distance is less than or equal to Dist[i], the data
object stays in the initial cluster;
  b) Else
  For every cluster center cj(1<=j<=k), compute the
  distance d(di, cj) of each data object to all the center, assign the data object di to the nearest center cj.\
  Set Cluster[i]=j\
  Set Dist[i]= d(di, cj);
8) For each cluster center j(1<=j<=k), recalculate the
centers, Until the convergence criteria is met.
9) Output the clustering results.

# Conclusion
To conclude , we applied two methods, mainly : kmeans and improved kmeans to segment the image.
The results for both can be seen at the mains's readme file.


# References
kmeans - https://www.sciencedirect.com/science/article/pii/S1877050915014143#:~:text=Subtractive%20clustering%20method%20is%20data,for%20the%20segmentation%20of%20image \
Improved kmeans - https://ieeexplore.ieee.org/document/5453745
