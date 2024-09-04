import time
import matplotlib.pyplot as plt
start=time.time()
def selectionsort(a):
    n=len(a)
    for i in range(n-2):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
                temp=a[i]
                a[i]=a[min]
                a[min]=temp
x=[50,87,98,65,45,12,32,49]
print("before sorting",x)
selectionsort(x)
print("after sorting",x)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("selectionsort time complexity")
plt.xlabel("input")
plt.ylabel("time")
plt.show()