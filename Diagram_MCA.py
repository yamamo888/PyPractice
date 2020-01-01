# -*- coding: utf-8 -*-

import sys

import mca
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster, set_link_color_palette
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns
import pdb

fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryo.ttc')

# ----
# file path
filePath = "ディズニー.csv"
# sample score file path
scorefilePath = "DCls2.txt"
# ----

# ----
# loading csv for 布置図
df = pd.read_csv(filePath,index_col=0,header=0)
data = pd.read_csv(filePath,index_col=0)
# loading sample score csv for cluster
#df = pd.read_csv(scorefilePath,index_col=0)

# ----

# category name
rlabels = df.index
# sample naem
clabels = df.columns

# mca model
MCAmodel = mca.MCA(data,benzecri=False,TOL=1e-8)

# ----
# row score (category)
rows = pd.DataFrame(MCAmodel.fs_r(N=3))
print("カテゴリスコア:\n")
print(rows)

# columns score (sample)
cols = pd.DataFrame(MCAmodel.fs_c(N=3))
print("サンプルスコア:\n")
print(cols)
print("----\n")
# ----

# ----
# plot
sns.set()

# row score plot
plt.scatter(rows.iloc[:,0],rows.iloc[:,1],color="coral",s=20,marker="o")
for label,x,y in zip(rlabels,rows.iloc[:,0],rows.iloc[:,1]):
    plt.annotate(label,xy=(x,y),fontproperties=fp,fontsize=8)

plt.xlim(-1.5,2.0)
plt.ylim(-2.0,2.0)

plt.xlabel("1軸",fontproperties=fp,fontsize=10)
plt.ylabel("2軸",fontproperties=fp,fontsize=10)
#plt.title("サンプルの布置図 in 1&2 軸",fontproperties=fp,fontsize=12)
plt.grid(False)

#plt.show()
plt.close()

fig,ax = plt.subplots(figsize=(5,5))

# columns score plot
plt.scatter(cols.iloc[:,0],cols.iloc[:,2],color="gray",s=20,marker="o")
for label,x,y in zip(clabels,cols.iloc[:,0],cols.iloc[:,2]):
    plt.annotate(label,xy=(x,y),fontproperties=fp,fontsize=8)

plt.xlim(-1.5,2.0)
plt.ylim(-2.0,2.0)

ax.axhline(y=0,ls="--",color="khaki",linewidth=1)
ax.axvline(x=0,ls="--",color="khaki",linewidth=1)

plt.xlabel("1軸",fontproperties=fp,fontsize=10)
plt.ylabel("3軸",fontproperties=fp,fontsize=10)
#plt.title("カテゴリの布置図 in 1&2 軸",fontproperties=fp,fontsize=12)
plt.grid(False)
#plt.savefig("category12.png")
#plt.show()
# ----
#pdb.set_trace()
# ----
# 相関係数(未使用)
#corr = df.corr()
#print(corr)
# ----
"""
# ----
# 階層的クラスター
methodName = ["average","centroid","complete","median","single","ward","weighted"]
set_link_color_palette(['coral', 'lightgreen', 'lightskyblue', 'plum', 'gold', 'orangered'])

sns.set()

for method in methodName:
    z = linkage(df,method=method,metric="euclidean") 
    #dendrogram(z,labels=clabels,color_threshold=7.,above_threshold_color='black')
    #pdb.set_trace()
    dendrogram(z,labels=rlabels,,orientation="right")
    #plot(dendrogram(z,labels=rlabels)
        #,horiz=TRUE)
    #dendrogram(z)
    for l in plt.gca().get_yticklabels():
        l.set_fontproperties(fp)
        
    group = fcluster(z, 6, criterion='maxclust')
    plt.title(method)
    plt.grid(False)
    plt.rcParams["font.size"] = 6
    plt.subplots_adjust(wspace=0.7,hspace=0.7)
    plt.savefig(f"{method}.png",bbox_inches="tight")
    #plt.show()
    plt.close()
    
    print(method)
    print(group)
    print("----")

"""