# input =
import matplotlib.pyplot as plt
import ast
import re
import numpy as np
import time

test = []
with open('Gan200.txt', 'r') as fh:
    for line in fh:
        p1 = re.compile(r'[[](.*?)[]]', re.S)
        test += re.findall(p1, line)


# print(test)
d_loss_avg=[]
d_loss =[]
g_loss_avg = []
g_loss = []
epoch = []

new_epoch=False
for ele in test:
    if ele.startswith( 'Epoch ' ):
        tem=ele.replace('Epoch ' ,'')
        tem=tem.split('/')
        tem=tem[0]


        if tem in epoch:
            print("already in it")
            new_epoch=False
        else:
            print("not in it")
            new_epoch=True
            epoch.append(tem)

        if new_epoch:
            if  len(d_loss) !=0:
                d_loss_avg.append(np.average(d_loss))
                g_loss_avg.append(np.average(g_loss))
            else:
                pass

        
            d_loss =[]
            g_loss = []

    
    if ele.startswith( 'D loss: ' ):
        a = float(ele.replace('D loss: ' ,''))
        d_loss.append(a)

    if ele.startswith( 'G loss' ):
        a = float(ele.replace('G loss: ' ,''))
        g_loss.append(a)

    if ele == test[-1]:
        if  len(d_loss) !=0:
            d_loss_avg.append(np.average(d_loss))
            g_loss_avg.append(np.average(g_loss))
        else:
            d_loss_avg.append(0)
            g_loss_avg.append(0)       



plt.figure(figsize=(20,5))
plt.plot(epoch, d_loss_avg)
plt.show()