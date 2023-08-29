############################################################
# Matplotlib Özellikleri
############################################################

# Matplotlib katmanlı bir şekilde görselleştirme imkanı sağlar.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
########################
# plot
########################
x = np.array([ 1, 8 ])
y = np.array([ 0, 150 ])
plt.plot(x, y, )
plt.show()

x = np.array([ 1, 8 ])
y = np.array([ 0, 150 ])
plt.plot(x, y, 'o')
plt.show()

x = np.array([ 2, 4, 6, 8, 10 ])
y = np.array([ 1, 3, 5, 7, 9 ])

plt.plot(x, y, 'o')
plt.show()

########################
# marker
########################
y = np.array([ 13, 28, 11, 100 ])

plt.plot(y, marker= 'o')
plt.show()


# Uygulanabilir markerlar;
# marker = ['o','*','.',',','x','X','+','P','s','D','d','p','H','h']

########################
# line
########################
y = np.array([ 13, 28, 11, 100 ])

plt.plot(y, linestyle = "dashdot", color = "r")
plt.show()
########################
# multiple line
########################

x = np.array([ 23, 18, 31, 10 ])
y = np.array([ 13, 28, 11, 100 ])

plt.plot(x)
plt.plot(y)
plt.show()
########################
# Labels
########################
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)
#Başlık
plt.title("Ana Başlık")
# X ekseni isimlendirme
plt.xlabel("X Ekseni")
# Y ekseni isimlendirme
plt.ylabel("Y Ekseni")
# Izgara ekleme
plt.grid()
plt.show()

########################
# Subplots
########################
# plot 1
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.subplot(1,2,1)
plt.title("1")
plt.plot(x,y)

# plot 2
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.subplot(1,2,2)
plt.title("2")
plt.plot(x,y)
plt.show()