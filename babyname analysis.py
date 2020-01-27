#import the namelist file
file_path='D:/babyname list/yob1880.txt'
file_context=open(file_path,'r')#以只读形式打开文件
raw_data=file_context.readlines()
#以字典形式逐行读取信息
babyname=[]
dict={'name':'Allen','gender':'M','number':100}
linenumber=0
import linecache
for line in raw_data:
    linenumber = linenumber + 1
    #linecache输出特定行
    namelist=linecache.getline(file_path,linenumber).strip()
    #solit()函数分割单行
    dict['name']=namelist.split(',')[0]
    dict['gender']=namelist.split(',')[1]
    dict['number']=int(namelist.split(',')[2])
    babyname.append(dict)
print(babyname)

#file_context.close()

