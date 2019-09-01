# fileName = open(r'E:\na.txt','r') #r取消转义
#
# Fdir = 'C:\ntest'
# print(repr(Fdir)) #repr() 取消转义
#
# #列表生成式
# beforetax = [10000,15000,8000,4000,5000]
# aftertax = [int(one*0.9) for one in beforetax if one >=8000]
# print(aftertax)
#
# #99乘法表
# for i in range(1,10):#行
#     for j in range(1,i+1):#列
#         print(f'{j}*{i}={i*j}',end='\t')
#     print()

'''
请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。

请按下面算法的思路实现函数：

1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面
'''
lastList = [45,65,21,7,1,6]
def mySort(lastList):
    #定义一个空列表
    newList = []
    #循环6次
    for one in range(len(lastList)):
        print(one)
        #将最小的添加到newList
        newList.append(min(lastList))
        #添加完成之后将最小的元素在原来的列表中删除掉
        lastList.remove(min(lastList))
    return newList

print(mySort(lastList))


'''
    1.如果使用numbers 参数,传值的时候只能传列表或者元组
    2.如果使用*numbers参数,传值的时候可以传任意数量,返回的是一个元组
    3.如果使用*numbers参数,传值想传一个列表的时候,直接使用*[]或者*()展开元组或者列表
'''
def get_sum(*numbers):
    total = 0
    print(numbers)
    for i in numbers:
        print(i)
        total += i
    return total
#print(get_sum([1,2]))
#print(get_sum(1,2))
aList = [1,2,3]
print(get_sum(*aList))

def func(a,c=2,*args,**kwargs):
    print(a,c,args,kwargs)
func(1,3,4,5,6,7,name='tom',age = 100)#a=1 c=3 args是一个元组,kwargs是一个字典

dict1 = {'name':'tom','age':100}
func(1,3,4,5,6,7,**dict1)#与上面结果一样,但是字典展开必须要用 **变量名