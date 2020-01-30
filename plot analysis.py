John_value=[]
Mary_value=[]
Jacob_value=[]
Isabella_value=[]
years=[]

for year in range(1880, 2011):
    years.append(year)
    # import the namelist file
    file_path = 'D:/babyname list/babynames/yob' + str(year) + '.txt'
    file_context = open(file_path, 'r')  # 以只读形式打开文件
    raw_data = file_context.readlines()  # 逐行读取信息

    babyinfo = {}
    sum = 0
    for line in raw_data:
        # split()函数分割单行
        name = line.split(',')[0]
        value = int(line.split(',')[2])
        babyinfo[name] = value
        sum = sum + int(line.split(',')[2])
    '''
    找寻新生儿信息中特定名字的频率，
    同时利用异常处理语句防止该年份无此姓名
    '''
    try:
        babyinfo['John']
    except KeyError:
        John_value.append(0)
    else:
        John_value.append(babyinfo['John'] / sum)

    try:
        babyinfo['Mary']
    except KeyError:
        Mary_value.append(0)
    else:
        Mary_value.append(babyinfo['Mary'] / sum)

    try:
        babyinfo['Jacob']
    except KeyError:
        Jacob_value.append(0)
    else:
        Jacob_value.append(babyinfo['Jacob'] / sum)

    try:
        babyinfo['Isabella']
    except KeyError:
        Isabella_value.append(0)
    else:
        Isabella_value.append(babyinfo['Isabella'] / sum)
    file_context.close()

import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

plt.plot(years,John_value,linestyle=':',marker = 'o',markerfacecolor='c',markersize = 3)
#plt.plot(years,Mary_value,linestyle=':',marker = 'o',markerfacecolor='m',markersize = 3)
plt.plot(years,Jacob_value,linestyle=':',marker = 'o',markerfacecolor='y',markersize = 3)
#plt.plot(years,Isabella_value,linestyle=':',marker = 'o',markerfacecolor='k',markersize = 3)

plt.show()
