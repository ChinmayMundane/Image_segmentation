<<<<<<< HEAD
from random1 import RANDOM
from KMeans_Plus import K_MEANS_PLUS
from Subtractive_Clustering import SUBTRACTIVE
from K_Means import K_MEANS
from Improved import K_MEANS_IMPROVED
from pcs import PCS
=======
from K_Means import K_MEANS
from Improved import K_MEANS_IMPROVED
>>>>>>> 7d971bd1281c67ae8dfb42bc6c7a3001af64dcdb

def main():
    print("To Use K-Means Improved Method -----> 1")
    print("To Use K-Means Method -----> 2")
    a = int(input("Input : "))
    K = int(input("Enter Number Of Clusters : "))
    path = input("Enter Image Path : ")
    print("To Use Subtractive Clustering Method -----> 0")
    print("To Use Random Initialization Method -----> 1")
    print("To Use K-Means++ Method -----> 2")
    b = input("Input : ")
    if(a==1):
        K_MEANS_IMPROVED(path,K,b)
    else:
        K_MEANS(path,K,b)

if __name__=="__main__":
    main()