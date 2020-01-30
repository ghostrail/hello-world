#import the namelist file
file_path='D:/babyname list/yob1880.txt'
file_context=open(file_path,'r')#以只读形式打开文件
raw_data=file_context.readlines()
#以字典形式逐行读取信息
babyname=[]
linenumber=0
sum=0
import linecache
for line in raw_data:
    #split()函数分割单行
    dict={}
    babyname.append(dict)
    babyname[linenumber]['name']=line.split(',')[0]
    babyname[linenumber]['gender']=line.split(',')[1]
    babyname[linenumber]['number']=int(line.split(',')[2])
    sum=sum+int(line.split(',')[2])
    linenumber = linenumber + 1

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

label_list=[]
value_list=[]
num_list=[]
for x in range(9):
    label_list.append(babyname[x]['name'])
    value_list.append(babyname[x]['number'])
    num_list.append(babyname[x]['number']/sum)
#选择前10位婴儿姓名和名字数量作为横纵坐标

x = np.arange(len(label_list))  # the label locations
fig, ax = plt.subplots()
width = 0.4  # the width of the bars
rects = ax.bar(x , num_list, width, label='Men')

ax.set_ylabel('频率')
ax.set_title('1880年新生儿姓名top10')
ax.set_xticks(x)
ax.set_xticklabels(label_list)
ax.legend()

'''
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects)
'''
plt.show()

file_context.close()
