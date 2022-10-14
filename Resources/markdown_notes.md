# Image_segmentation

## Abstract
Image segmentation is the classification of an image into different groups. Here we have use k-means clustering algorithm for image segmentation.K -means clustering algorithm is an unsupervised algorithm and it is used to segment the interest area from the background. 
But before applying K -means algorithm, first **partial stretching enhancement** is applied to the image to improve the quality of the image. 
Next, **Subtractive clustering** method is data clustering method where it generates the centroid based on the potential value of the data points. So subtractive cluster is used to generate the initial centers and these centers are used in **k-means algorithm** for the segmentation of image.
Then finally **medial filter** is applied to the segmented image to remove any unwanted region from the image



## Introduction

Image segmentation is one of the mostly used methods to classify the pixels of an image correctly in a decision oriented application.
There are different techniques used for image segmentation. They are:
*  threshold based
*  edge based
*  cluster based
*  neural network based.



Here, one of the most effective technique is clustering method. But, clustering method is also divided into following subtypes:
 * K -means clustering
 * Fuzzy C-means clustering
 * mountain clustering method
 * subtractive clustering method.


In this project, we are using K-means clustering due to its efficiency in computation as compared to hierarchical clustering. However, we need to find suitable number of clusters and their centroid for it to work perfectly.That's where subtractive clustering comes into play.
Image segmentation is a wonderful tool which is used to segment the cancer cells from normal cells and has many medical applications.





## Contrast Enhancement using Partial Contrast Stretching

Medical images which have been used for the analysis may have their own weakness such as blurred or low contrast.
So a contrast enhancement technique such as Partial Spatial Starching (PCS) is used to improve the image quality and
contrast of the image.
By applying this technique, the pixel range of
lower threshold value and upper threshold value will be mapped to a new pixel range and stretched linearly to a wide
range of pixels within new lower stretching value, and the remaining pixels will experience compression




## Subtractive Clustering Algorithm

To find the centroid centers of the clusters, subtractive clustering is used.It estimates the number and initial location of the cluster centers. It distribute the    data space into gridding point and compute the potential for each data point base on its distance to the actual data point (So the grid point with many data point nearby will have high potential value).

* And so this grid point with highest potential value will be choose as first cluster centre.
* After selecting the first cluster centre we will try to find the second cluster centre by calculating the highest potential value in the remaining grid points.
* As grid points near the first cluster center will reduce its potential value, the next cluster center will be grid with many data point nearby other than first cluster center grid point
* After calculating the revise potential of each data points, find the next highest potential as the next cluster center.
* So these processes continue until a sufficient number of cluster centre are obtained.





## K -Means Clustering Algorithm


* Specify number of clusters K.
* Initialize centroids by first shuffling the dataset and then randomly selecting K data points for the centroids without replacement.
* Keep iterating until there is no change to the centroids. i.e assignment of data points to clusters isn’t changing.
    * Compute the sum of the squared distance between data points and all centroids.
    * Assign each data point to the closest cluster (centroid).
    * Compute the new centroids for the clusters by taking the average of the all data points that belong to each cluster.
    





## Median Filter

Median filtering is used as a noise removal in order to obtain a noise free image. After segmentation is done, the
segmented image may still present some unwanted regions or noise. So to make the image a good and better quality,
the median filter is applied to the segmented image. We can use different neighborhood of n × n. But generally
neighborhood of n = 7 is used because large neighborhoods produce more severe smoothing




## Proposed Algorithm 

* Load the image to be segmented.
* Apply partial contrast stretching.
* Initialize number of cluster, k.
* Calculate the potential for every pixel value of the image.
* Find maximum potential in step 4 and set that point be first center cluster and its corresponding potential as maximum potential.
* Update the potential value of other remaining pixels based on the first cluster center.
* Again find the maximum potential in the step 5 and let that point be second point.
* Continue the process until it finds the k number of cluster
* Used k centre as initial centre in the k-means clustering algorithm
* Find the Euclidean distance of each centroid from every pixel of the image
* Assign the pixel with minimum distance with respect to centroid to its respective cluster of the centroid
* recalculate the new center location
* Repeat the steps 11–13, until it satisfies the tolerance or error value.
* Reshape the cluster into image.
* Median filter is applied to the segmented image to remove any unwanted noise or region.




## Reference 
https://www.sciencedirect.com/science/article/pii/S1877050915014143#:~:text=Subtractive%20clustering%20method%20is%20data,for%20the%20segmentation%20of%20image.




      














