2017年10月23日
python 序列学习：

1. 序列是一块用于存放多个值的连续内存空间。
2. list ,内置可变序列，所有元素放在[],列表元素可修改，增加，删除，除非确实有必要，否则应该尽量从列表尾部进行元素的增加与删除工作，这样会大幅度提高列表处理速度
list中的元素可以同时包含整数，实数，字符串等基本类型，也可以是列表，元组，字典，集合等
['span', 2.9, [1, 2]]
3. list列表对象常用方法：
list.append(x)      #将元素x添加至列表尾部
list.extend(L)      #将列表L中所有元素添加到列表尾部
list.insert(index, x)       #在列表中指定位置index处添加元素x
list.remove(x)              #在列表中删除首次出现的指定元素
list.pop([index])       #删除并返回列表对象指定位置的元素，默认是最后一个元素
list.clear()            #删除列表中所有元素，但是保留列表对象，该方法在python2中没有
list.index(x)           #返回第一个值为x的元素的下表，若不存在，抛出异常
list.count(x)           #返回指定元素x在列表中出现的次数
list.reverse()          #对列表元素进行原地翻转
list.sort()             #列表元素原地排序
list.copy()             #返回列表对象的浅赋值，python2中没有

3. list创建与删除
 list()函数可以将tuple,range()对象，字符串或者其他类型可迭代对象数据转换为list，range()在2中返回是list,3中是对象
 list(range(10)),list('hello world'),将字符串拆分成单个字符
 python2 中提供的xrange()，返回的是可迭代对象，类似于python3中的range()函数，特点是惰性求值，不想range()函数一样返回列表
del list     #可以直接删除列表

4. 列表元素的增加
(1)使用+运算符实现元素添加到列表的功能，并不是真的为列表添加元素，而是创建一个新的列表，并将原列表中的元素和新元素依次复制到新列表的内存空间，大量元素时操作较慢
list_1 = [1, 2]
list_2 = [3]
list = list_1 + list_2
list则为[1, 2, 3]
(2)使用列表对象的append()方法，
查看运行时间：
import time

result = []
start = time.time()
for i in range(10000):
    result = result + [i]
print(len(result), ',', time.time() - start)

python 采用的是基于值的自动内存管理方式，当为对象修改值时，并不是真的修改变量的值，而是使变量指向新的值，这对所有类型的变量都是一样的
a = [1]
id(a)
a = [1, 2]
id(a)
会发现id是不一样的
对于列表而言，列表中包含的是元素值的引用，而不是直接包含元素值，如果是直接修改序列变量的值，则与python普通变量一样，如果通过下标来修改序列中元素的值或者通过可变序列对量
自身提供的方法来增加和删除元素，那么序列对象在内存中的起始地址是不变的，仅仅是被改变元素的地址发生了变化。
a = [1, 2, 3]
b = [1, 2]
id(a[0]) == id(b[0])        Ture  因为对应元素值相同，所以id相同，
a.remove(1)     #删除某个元素
(3) 通过extend()方法将另一个迭代对象所有元素添加到该列表尾部，通过extend()方法增加列表元素不改变内存首地址，属于原地操作。
a.extend([7, 4, 6])
(4) insert方法将元素添加到列表的指定位置
a.insert(3, 6)      在索引为3的位置添加元素6
pop()函数弹出列表非尾部元素，del删除非尾部元素，除非必要，应该尽量避免在列表中间位置插入和删除元素，因为涉及到元素的移动，会占用大量时间，应该优先考虑
append()和pop()方法
insert()速度查看：
import time

def Insert():
    a = []
    for i in range(10000):
        a.insert(0, i)
start = time.time()
for i in range(10):
    Insert()
print('Insert:',time.time() - start)
速度比append()慢很多
(5) 使用乘法来扩展列表对象，将列表与数字相乘，新列表是愿列表的重复，并不是愿列表的修改，实际上是创建了一个新的列表，id发生了变化，在使用*进行扩展的时候，
并不会创建元素的复制，而是创建已经有的元素的引用，修改其中一个值的时候，相应的引用也会被修改

a = [1]
a * 3  : [1, 1, 1]
x = [['a'] * 2] * 3
>>>x
[['a', 'a'], ['a', 'a'], ['a', 'a']]
x[0][0] = 'b'
>>>x
[['b, a], [b, a], [b, a]]
这一点需要注意

5.list元素的删除：
(1)del命令删除列表中指定位置上的元素或者整个列表
del a[0]
(2)pop()方法删除并返回指定(默认是最后一个)位置上的元素，如果给定的索引超出了范围，就抛出异常
a = [1, 2, 3]
a.pop()     表示删除最后一个元素并返回，之后a = [1, 2] ,返回3
a.pop(2)    表示删除索引为2的元素，3被删除，并返回3
(3)remove()方法删除首次出现的指定元素，如果列表中不存在，抛出异常
a = [1, 2, 1, 3]
a.remove(1)     #会删除a[0]上的1，是首次出现的1
如果要删除列表中指定元素的所有重复，由于列表的自动内存管理功能，删除元素后，会使得内存收缩并移动列表元素来保证所有元素之间没有空隙，元素位置后面所有
元素的索引都会改变，
从前向后删除：
x = [1, 2, 1, 2, 1, 1, 1]
for i in x[::]:
    if i == 1:
        x.remove(i)
从后往前删：
for i in range(len(x) - 1, -1, -1) :
    if x[i] == 1:
        del x[i]

6.列表元素访问与计数
可以使用下标直接访问列表中的元素，若指定下标不存在，抛出异常提示下标越界
a = [1, 2]
a[1]
index()方法可以获得指定元素首次出现的下标，语法为;index(value,[start,stop]),搜索范围可以指定，start 默认为0，stop默认为列表长度，不存在抛出异常
a.index(1)
用count()方法统计指定元素在列表中出现的次数：
a = [1, 2, 3, 2]
>>>a.count(2)           写入要统计的元素
2
该方法也可以用于tuple，字符串和range对象：
>>>range(10).count(1)
1
>>>(1, 2, 3, 1).count(1)
2
>>>'abbb'.count('b')
3

7.成员资格判断
(1)用count()方法判断是否存在，
(2)用关键字in, not in 判断是否在list 中，返回布尔结果
3 in list
a = [1 , 2]
b = [2, 3]
(1, 2) in zip(a, b)
Ture
for a, b in zip(a, b):
    print(a, b)
1 2
2 3
组合两个list

8.切片操作
切片用于列表，元组，字符串，range对象等类型，可以原地修改列表内容，列表元素的增加，删减，修改，检查和元素替换邓，不影响列表对象的内存地址
与使用下标访问列表元素不同，切片操作不会因为下标越界而抛出异常，而是返回空列表
a = [1, 2, 3, 3]
a[start:stop:step],不包括下标为stop的元素
a[::]       输出原序列
a[::-1]     逆序输出
a[::2]      每隔两个取一个
a[3:6]      省略step，默认为1，从下标为3取到6
a[100:]     返回空集合，不提示错误
a[len(a):]    返回空集合
a[len(a):] = [9]  此时在a的尾部增加元素9
a[:3] = [1, 2, 3]       修改元素相应位置的内容
a[:3] = []              删除指定位置内容
a[::2] = [0] * (len(a) // 2)  a的长度从0到len(a),如果是偶数插入0
del a[:3]   删除指定位置元素
切片返回的是列表元素的浅复制，和列表对象那个的直接赋值是不一样的
a = [1, 2]
b = a    #a和b指向同一块内存
b[1] = 0
>>>a
[1, 0]
>>>a == b
True
>>>id(a) == id(b)
a = [1, 2]
b = a[::]   #浅复制
>>>a == b
True
>>>id(a) == id(b)
False
使用切片复制其实就是新的list了，跟之前的list内容虽然一样，但是地址已经不一样的

9.列表排序：
(1)sort()方法的原地排序，对原列表进行操作
a = [1, 3, 2, 5]
import random
random.shuffle(a)      #打乱顺序
a.sort()        #默认升序排列
a.sort(reverse=True)    #降序排列
a.sort(key = lambda x: len(str(x)))     #自定义排序
(2)sorted()返回新列表，并不对原列表进行任何修改
sorted(a)
sorted(a, reverse=True)     #降序排序
(3)对list所有元素逆序排列，reverse()方法：
import random
a = [random.randint(50, 100) for i in range(10)]
a
a.reverse()
(4)reversed()函数不对原列表有任何修改，返回逆序列表
a = [1, 2]
a_new = reversed(a)
a_list = list(a_new)
for i in a_list:
    print(i, end='')
此时for 循环不会有内容输出，因为在之前list函数执行的时候，迭代对象已经遍历结束，需要重新创建迭代对象才能访问内容

10.用于序列操作的常用内置函数
(1)cmp(序列1， 序列2):对两个列表进行比较，如果第一个列表大返回1，否则等于0，小于 -1，类似于比较大小，但是和is,is not 不一样
>>>(1, 3) < (1, 4)
True
>>>cmp((1, 3), (1, 4))
-1
>>>cmp('a', 'A')
1
>>>'a'>'A'
True
python 3 不在支持cmp()函数，可以直接使用关系运算符来比较数值或者序列的大小
(2)len(list) 返回列表中的元素个数
(3)max(),min()：返回列表中的最大或者最下的元素，同样适用于元祖、字符串、集合、range对象、字典等，要求所有元素之间可以比较大小。字典中默认是对于键计算，
如果要对值进行计算，要用values()方法
a = {1:1, 2:4, 3:6}
>>>max(a)
3
>>>max(a.values())
6
(4)sum(列表)：对数值型列表的元素求和，非数值型列表运算会出错
a = {1:1, 2:4, 3:6}
>>>sum(a)
6
>>>sum(a.values())
11
(5)zip(列表1，列表2……),将多个列表或者tuple对应位置的元素组合为元组，并返回包含这些元组的列表（p2）或zip对象(p3)
python2:
a = [1]
b = [2]
c = [3]
d = zip(a , b, c)
>>>d
[(1, 2, 3)]
python3:
a = [1]
b = [2]
c = [3]
d = list(zip(a , b, c))
>>>d
[(1, 2, 3)]

(6)enumerate(列表)：枚举列表，元组或其他可迭代对象中的元素，返回枚举对象，对象中的每个元素是包含下表和元素值的元组，字符串，字典也可以
for item in enumerate(list):
    print(item)

(0, (1, 2, 3))
>>>for index, ch in enumerate('SDI'):
    print((index, ch), end=',')

a = {1: 1, 2: 4, 3: 6}
for i, v in enumerate(a):
    print(i,v,end='')

a = {1: 1, 2: 4, 3: 6}
for i, v in enumerate(a.values()):
    print(i,v)

11.列表推导式：python程序开发应用最多的技术之一。列表推导式使用非常简洁，可以快速生成满足特定需求的列表，代码具有非常高的可读性
a_list = [x ** 3 for x in range(10)]
(1)使用列表推导式实现嵌套列表的平铺
vec = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
>>>[num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

(2)不符合条件的元素：在列表推导式中可以使用if子句来筛选，只在结果列表中保留符合条件的元素。
#列出当前文件夹下所有Python源文件：
>>>import os
>>>[filename for filename in os.listdir('.') if filename.endswith('.py')]     #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
#从列表中选择符合条件的元素组成新的列表：
>>>alist = [-1, -4, 6, 7.5]
>>>[i for i in alist if i > 0]
#已知一个包含成绩的字典，计算最高最低和平均，并查找所有最高分同学
>>>scores = {"Alice": 25, "han": 100, "zhou": 100, "dong": 60}
>>>highest = max(scores.values())
>>>lowest = min(scores.values())
>>>average = sum(scores.values()) / len(scores)
>>>highest_person = [name for name,score in scores.items() if score == highest]

(3)在列表推导式中使用多个循环，实现多序列元素的任意组合，并且可以结合条件语句过滤特定元素
>>>[(x, y) for x in range(2) for y in range(2)]
[(0, 0), (0, 1), (1, 0), (1, 1)]
>>>[(x, y) for x in range(2) for y in range(2) if x != y]
[(0, 1), (1, 0)]

(4)使用列表推导式实现矩阵转置
>>>matrix = [[1, 2, 3], [4, 5, 6]]
>>>[[row[i] for row in matrix] for i in range(3)]
[[1, 4], [2, 5], [3, 6]]

#使用内置函数zip()和list()来实现矩阵转置
>>>list(zip(*matrix))

(5)列表推导式可以使用函数或者复杂表达式
def f(v):
    if v % 2 == 0:
        v = v ** 2
    else:
        v += 1
    return v
>>>print([f(v) for v in [1, 2, 3, -1] if v > 0])
[2, 4, 4]
>>>print([v ** 2 if v % 2 == 0 else v + 1 for v in [1, 2, 3, -1] if v > 0])
[2, 4, 4]

(6)列表推导式支持文件对象迭代
>>>fp = open('C:\test.txt', 'r')
>>>print([line for line in fp])
>>>fp.close()

(7)使用列表推导式生成100以内的所有素数
import math
>>>[p for p in range(2, 100) if 0 not in [p % d for d in range(2, int(math.sqrt(p)) + 1)]]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

12.使用列表实现向量运算
>>>[1, 2] * 2
[1, 2, 1, 2]
python列表不支持与整数的加减除运算，也不支持列表之间的减乘除运算。列表的加法表示列表元素的合并，是生成了新的列表，而不是有向量意义的加法。
>>>[1, 2] + [3]
[1, 2, 3]

13.tuple 属于不可变序列，不可修改元素的值，也无法增加或者删除元素，如果确实要修改，只能再创建一个新的元组

14.元组的创建与删除：
(1)=赋值,如果要创建只包含一个元素的元组，只把元素放在括号里是不行的，要在后面加一个逗号，创建多个元素的元组没有这个限制。
>>>a_tuple = ('a',) #len(a_tuple) == 1
>>>a = (1)          #则 a == 1 不是元组，而是数值
>>>x = ()           #空元组
>>>a = 1, 2         #a == (1, 2)是元组
(2)tuple()函数可以将其他类型的序列转换为元组
>>>print(tuple('abc'))
('a', 'b', 'c')
>>>tuple(list)      #tuple()可以转换list为tuple，反之不行
元组只能使用del命令删除整个元组对象，不能只删除其中的元素

15.元组与列表的区别
元组没有append()/extend()/insert()等方法，无法向元组中添加元素，修改元素，也没有remove()/pop()
元组也支持切片操作，但是只能通过切片访问元组中的元素，不能修改和删减元素
元组的访问和处理速度比列表快，元组可以用作字典的键，因为不可变，而列表不可以
虽然元组不可变，但是如果元组中有list，改变list中的元素还是可以的：
>>>x = ([1, 2], 3)
>>>x[0][0] = 0
>>>x
([0, 2], 3)
>>>x[0].append(0)
>>>x
([0, 2, 0], 3)
>>>x[0] = x[0] + [2]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

16.序列解包：可以用非常简洁的形式完成复杂的功能，提高代码可读性
(1)用序列解包功能对多个变量同时赋值
>>>x, y, z = 1, 2, 3
>>>print(x, y, z)
1 2 3
(2)序列解包可以作用于列表和字典，对字典使用，默认对于键操作，若要操作键值对，应该用.items()方法，若对值操作，用.values()方法，
>>>a = [1, 2, 3]
>>>b, c, d = a
>>>s = {'a': 1, 'b': 2, 'c': 3}
>>>b, c, d = s.items()
>>>b
('a', 1)
(3)序列解包方便遍历多个序列
>>>keys = ['a', 'b', 'c']
>>>values = [1, 2, 3]
>>>for k, v in zip(keys, values):
     print(k, v)
a 1
b 2
c 3

(4)序列解包支持以下用法：
>>>print(*[1, 2],2)
1 2 2
>>>def demo(a, b):
     print(a, b)
>>>demo(**{'a':1, 'b': 2})
1 2
>>>*range(4), 4
(0, 1, 2, 3, 4)
>>>[*range(4), 4]
[0, 1, 2, 3, 4]
>>>{*range(3), *(1,)}
{0, 1, 2}

17.生成器推导式：生成器推导式使用圆括号而列表推导式使用方括号。生成器推导式的结果是个生成器对象，不是列表也不是元组，使用时在转化为列表货源足，也可以用
生成器对象的next()(p2)方法，或者__next__()方法(p3)进行遍历，或者直接作为迭代器对象使用，但是当所有元素访问结束以后，需要重新访问其中的元素，必须重新创建
生成器对象。
>>>g = ((i + 2) ** 2 for i in range(10))
>>>g
<generator object <genexpr> at 0x00000000035286D0>
>>>tuple(g)
(4, 9, 16, 25, 36, 49, 64, 81, 100, 121)
>>>g = ((i + 2) ** 2 for i in range(10))
>>>list(g)
[4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
>>>g = ((i + 2) ** 2 for i in range(10))
>>>g.__next__()
4
>>>g.__next__()
9

18.字典：是键-值对的无序可变序列，字典中的每个元素包含键值两部分，键值用冒号分开，相邻元素用逗号分开，{}里面放置
字典中的键可以使Python中任意不可变数据，但是不能使用可变对象，如列表等，字典中的键不可以重复，而值可以重复
用内置函数globals()返回和查看包含当前作用域内所有全局变量和值的字典，locals()返回包含当前作用域内所有局部变量和值的字典
a = (1, 2)
b = 'hello'
def demo():
    a = 0
    print('locals: ', locals())
    print('globals: ', globals())
demo()
locals: {'a': 0}
globals: {'__builtins__': {'__name__': 'builtins',
                           '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.",
                           '__package__': '', '__loader__': <}

19.字典创建与删除
(1)=赋值
>>>a_dict = {'good': 100}
>>>a_dict
{'good': 100}
(2)使用内置函数dict()通过已有数据快速创建字典
>>>keys = ['han', 'zhou']
>>>values = [100, 99]
>>>dict1 = dict(zip(keys, values))
>>>dict1
{'han': 100, 'zhou': 99}
#空字典
>>>x = dict()
>>>x = {}
(3)dict()函数给定键值对创建字典
>>>dict2 = dict(han = 100, zhou = 99)
>>>dict2
{'han': 100, 'zhou': 99}
(4)给定内容为键，创建值为空的字典
>>>dict3 = dict.fromkeys(['han', 'zhou'])
>>>dict3
{'han': None, 'zhou': None}

20.字典元素的读取

