# input =
import matplotlib.pyplot as plt
import ast
import re

test = []
with open('Gan1000.txt', 'r') as fh:
    for line in fh:
        p1 = re.compile(r'[[](.*?)[]]', re.S)
        test += re.findall(p1, line)


# print(test)
d_loss =[]
g_loss = []
epoch = []
for ele in test:
    if ele.startswith( 'Epoch ' ):
        epoch.append(ele.replace('Epoch ' ,''))
    elif ele.startswith( 'D loss: ' ):
        a = float(ele.replace('D loss: ' ,''))
        d_loss.append(a)

    elif ele.startswith( 'G loss' ):
        a = float(ele.replace('G loss: ' ,''))
        g_loss.append(a)
# print(d_loss)

numbers = range(len(epoch))
plt.figure(figsize=(20,5))
plt.plot(g_loss)
plt.show()