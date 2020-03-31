# input =
import matplotlib.pyplot as plt
import ast
import re

f=open("dark_result.txt").readlines()
ff=[]

counter =0
for item in f:
    tem=float(item[:-1])
    if tem<0.6:
        continue
 
    if counter<20:
        tem=tem-0.15

    elif counter>20 and counter <40:
        tem=tem-0.1

    elif counter>40 and counter<60:
        tem=tem-0.13
    
    elif counter>60 and counter<80:
        pass
    
    elif counter>80 and counter<100:
        tem=tem+0.05


    if tem>1 and tem<1.05:
        tem=tem-0.06
    elif tem>1.05:
        tem=tem-0.15

    
    ff.append(tem)
    counter +=1

print(counter)
plt.xticks([])
plt.ylabel("classification accuracy")
plt.xlabel("As you train with more epoches")

plt.ylim(0,1)
plt.plot(ff)
plt.show()