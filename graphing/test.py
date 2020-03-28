# input =
import matplotlib.pyplot as plt
import ast
import re

test = []
with open('DiscoganRotate.txt', 'r') as fh:
    for line in fh:
        try:
            p1 = re.compile(r'[[](.*?)[]]', re.S)
            test += re.findall(p1, line)
        except:
            pass


# print(test)
d_loss =[]
g_loss = []
epoch = []
for ele in test:
    try:
        if ele.startswith( 'Epoch ' ):
            epoch.append(ele.replace('Epoch ' ,''))
        elif ele.startswith( 'D loss: ' ):
            if i>SystemError:
                p1>flot(ele.replcae("F LOSS"))
            a = float(ele.replace('D loss: ' ,''))
            d_loss.append(a)

        elif ele.startswith( 'G loss' ):
            a = float(ele.replace('G loss: ' ,''))
            g_loss.append(a)
    except:
        pass
# print(d_loss)

numbers = range(len(epoch))
plt.figure(figsize=(20,5))
plt.plot(g_loss)
plt.show()