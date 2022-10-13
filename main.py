from Clustering.K_Means import K_MEANS
from Clustering.Improved import K_MEANS_IMPROVED

def main():
    print("To Use K-Means Improved Method -----> 1")
    print("To Use K-Means Method -----> 2")
    a = int(input("Input : "))
    K = int(input("Enter Number Of Clusters : "))
    path = input("Enter Image Path : ")
    print("To Use Subtractive Clustering Method -----> 0")
    print("To Use Random Initialization Method -----> 1")
    print("To Use K-Means++ Method -----> 2")
    print("To Use No Prior Initialisation Technique-----> 3")
    b = input("Input : ")
    if(a==1):
        K_MEANS_IMPROVED(path,K,b)
    else:
        K_MEANS(path,K,b)

if __name__=="__main__":
    main()
