#import the namelist file
file_path='D:/babyname list/yob1880.txt'
file_context=open(file_path,'r')#以只读形式打开文件
raw_data=file_context.readlines()
#以字典形式逐行读取信息
babyname=[]
linenumber=0
import linecache
for line in raw_data:
    #solit()函数分割单行
    dict={}
    babyname.append(dict)
    babyname[linenumber]['name']=line.split(',')[0]
    babyname[linenumber]['gender']=line.split(',')[1]
    babyname[linenumber]['number']=int(line.split(',')[2])
    linenumber = linenumber + 1

'''
def exchange(small,large):
    temp=babyname[small]
    babyname[small]=babyname[large]
    babyname[large]=temp
    return babyname[small],babyname[large]

print(babyname[3],babyname[7])
exchange(3,7)
print(babyname[3],babyname[7])
'''
file_context.close()

