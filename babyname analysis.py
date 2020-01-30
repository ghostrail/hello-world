#import the namelist file
file_path='D:/babyname list/yob1880.txt'
file_context=open(file_path,'r')#以只读形式打开文件
raw_data=file_context.readlines()
#以字典形式逐行读取信息
babyname=[]
linenumber=0
sum=0
women_list=[]
men_list=[]
for line in raw_data:
    #split()函数分割单行
    dict={}
    babyname.append(dict)
    babyname[linenumber]['name']=line.split(',')[0]
    babyname[linenumber]['gender']=line.split(',')[1]
    babyname[linenumber]['number']=int(line.split(',')[2])
    if babyname[linenumber]['gender']=='F':
        women_list.append(babyname[linenumber])
    else:
        men_list.append(babyname[linenumber])
    sum=sum+int(line.split(',')[2])
    linenumber = linenumber + 1

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

#男女前10的新生儿姓名
top10men_name=[]
top10men_number=[]
top10women_name=[]
top10women_number=[]
for x in range(10):
    top10men_name.append(men_list[x]['name'])
    top10men_number.append(men_list[x]['number']/sum)
    top10women_name.append(women_list[x]['name'])
    top10women_number.append(women_list[x]['number'] / sum)

label_list=['No.1','No.2','No.3','No.4','No.5','No.6','No.7','No.8','No.9','No.10']
x = np.arange(len(label_list))  # the label locations
fig, ax = plt.subplots()
width = 0.2  # the width of the bars
rects_m = ax.bar(x-width, top10men_number, width, label='Men')
rects_f = ax.bar(x+width, top10women_number, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('频率')
ax.set_title('1880年新生儿姓名top10')
ax.set_xticks(x)
ax.set_xticklabels(label_list)
ax.legend()

for x,y in zip(x,top10men_number):
    plt.text(x-0.2,y+0.001,top10men_name[x-1], ha='center', va='bottom')
x = np.arange(len(label_list))
for x,y in zip(x,top10women_number):
    plt.text(x+0.2,y+0.001,top10women_name[x-1], ha='center', va='bottom')

fig.tight_layout()
plt.show()

file_context.close()
