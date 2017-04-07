import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import statistics as st

from sklearn.cluster import KMeans

df=pd.read_excel('規律運動率.xlsx',index_col=0)

x = df.ix[:,0]



km = KMeans(n_clusters=5)            ##分群數

a = km.fit(np.reshape(x,(len(x),1))) ##引入資料及數量
          


c = km.cluster_centers_


lab = km.labels_

colors = ["g.","r.","y.","b.","c."]      ##分群數個別顏色

for i in c:                              ##引入中心設置為線
    plt.plot( [0, len(x)-1],[i,i],"k")    
    

for i in range(len(x)):                   
    plt.plot(i, x[i], colors[lab[i]], markersize = 20) ##設置顏色與點的大小
plt.savefig('K-means.jpg',dpi=100)
