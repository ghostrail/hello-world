linenumber=0
import linecache
for line in raw_data:
    #split()函数分割单行
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


