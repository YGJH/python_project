import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os 

font = FontProperties(fname=os.environ['WINDIR']+'\\Fonts\\kaiu.ttf', size=16)

data2 =np.array([['高','低','中','低','中'],['低','中','高','高','中'],['高','中','中','低','中']])


label= ['甲公司','乙公司','丙公司']
yll = ['低' , '中' , '高']
plt.figure(figsize=(10,5))
for i in range(3):
    plt.plot(np.arange(data2.shape[1]),data2[i,:],label=label[i])
plt.xticks(np.arange(data2.shape[1]),[i for i in range(109 , 114)],fontproperties=font)    
plt.yticks(np.arange(data2.shape[0]),yll,fontproperties=font)    
plt.legend(loc='lower right',prop=font)
plt.title('業績分析',fontproperties=font)
plt.xlabel('年',fontproperties=font)
plt.ylabel('業績',fontproperties=font)

plt.show()