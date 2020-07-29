import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import matplotlib
import analysis.data_functions as df

#根目录
rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))


matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=12


X,Y=df.get_cheat_ratio_difficulty()
print(X)
print(Y)
fig, ax=plt.subplots()

rect1=ax.plot(X,Y)

ax.set_title(u'题目难度与抄袭率的联系')
ax.set_xlabel('题目难度(1~5)')
ax.set_ylabel('抄袭率(%)')
ax.set_xticks(np.arange(1,6))


fig.tight_layout()
#根目录
rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
path=rPath+"/images/difficulty_cheat.png"
plt.savefig(path)
plt.show()