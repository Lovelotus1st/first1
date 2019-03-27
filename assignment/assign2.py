
'''4) Write a Python program to find the list in a list of lists whose sum of elements is
the highest and then print each element as a separate entity.'''
        
lis = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
sum_lis=[]
i=0
while (i<len(lis)):
    sum_lis.append(sum(lis[i]))
    i+=1
print(lis[sum_lis.index(max(sum_lis))])
for y in lis[sum_lis.index(max(sum_lis))]:
    print(y)
## now by importing Library#############    
print(max(lis, key=sum))
for x in max(lis, key=sum):
    print (x)
    
 '''result-----   
[10, 11, 12]
10
11
12
Result using library
[10, 11, 12]
10
11
12 -----'''

'''1) You already given a list of elements then you have to alter the list
   with user inputs and sort the list in increment order also find the mea &amp; median.
   from statistics import mean, median'''

lis =[5,4,3,2,1,0,33,22]
i = 0
while (i<len(lis)):
    lis[i] = eval(input("Enter new Value: "))
    i+=1   
print("Altered_list",lis)
​
''' RESULT
s_list = sorted(lis)
print("Sorted List: ",s_list)
print("Mean: ",mean(s_list))
print("Median",median(s_list))
Enter new Value: 4
Enter new Value: 46
Enter new Value: 784
Enter new Value: 89
Enter new Value: 95
Enter new Value: 985
Enter new Value: 12
Enter new Value: 1000
Altered_list [4, 46, 784, 89, 95, 985, 12, 1000]
Sorted List:  [4, 12, 46, 89, 95, 784, 985, 1000]
Mean:  376.875
Median 92.0'''
   
'''3) Write a Python program to alter the place of every n-th value with the (n+1)th
   place in a list and find the mean of each consecutive pair ,store in list and then
   sort the mean in increasing order.'''
   
from statistics import mean, median
lis =[0,1,2]
x =lis[2:]+lis[:2]
print(x)
z=[]
i = 0
while i<(len(x)-1):
    z.append((x[i]+x[i+1])/2)
    i+=1
print(z)
print(sorted(z))
''' RESULT
[2, 0, 1]
[1.0, 0.5]
[0.5, 1.0]'''
​
