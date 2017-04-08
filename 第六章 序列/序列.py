序列：成员是有序排列的，可以通过下标偏移量访问
    包括 字符串、元组、列表

# 6.1 序列
有着相同的访问模式：每个元素都能通过指定一个偏移量的方式得到，同时多个元素可以通过切片方式得到
    | 标准类型操作符
    | 序列类型操作符
        成员关系操作符：in、not in
        连接操作符： +
        重复操作符： *
        切片操作符： []、[:]、[::]
        用步长索引来进行扩展的切片操作：[::-1]表示翻转 [::2]表示隔一个
        切片索引的更多内容：for i in [None] + range(-1,-len(s),-1): 每次删除最后一个
    | 内建函数（BIF）
        类型转换： list()、str()、tuple()
        可操作： enumerate(iter)、len(seq)、max(iter,key=None)、max(iarg0,arg1,arg2...,key=None)、reversed(seq)、sorted(iter,func=None,key=None,reverse=False)、sum(seq,init=0)、zip([it0,it1,it2])

# 6.2 字符串
单引号或者双引号的作用是相同的
# 6.3 字符串和操作符
    | 标准类型操作符：=、>、、、
    | 徐磊操作符切片：[],[:]
# 6.4 只适用于字符串的操作符
    | 格式化操作符 %
# 6.5 内建函数
    | 标准类型函数： cmp()
    | 序列类型函数： len()、max()、min()、enumerate()、zip()
    | 字符串类型函数：raw_input()、chr()、unichr()、ord()
# 6.6 字符串内建函数
    | string.capitalize()：第一个字符大写
    | string.center（width)：返回一个原字符串居中，并使用空格填充至长度width的新字符串
    | string.count(str,beg=0,end=len(string))：返回str在string中出现的次数，可以指定范围
    | string.decode(encoding='UTF-8',errors='strict')：以指定的编码格式解码string，如果出错默认报错异常除非errors指定的是'ignore'或者'replace'
    | string.endswith(obj,beg=0,end=len(string))：检查字符串是否以obj结束，可以查询指定范围内是否以obj结束
    | string.expandtabs(tabsize=8)：把字符串中的tab符号转换为空格，默认的空格数量tabsize是8
    | string.find(str,beg=0,len(stirng))：查询是否含str
    | string.index(str,beg=0,len(string))：类似find，但是如果str不在string会报error
    | string.isalnum()：如果string至少有一个字符并且所有字符都是字母或者数字，返回True
    | string.isalpha()：如果string至少有一个字符并且所有字符都是字母，返回True
    | string.isdecimal()：只包含十进制返回True
    | string.isdigit()：只包含数字返回True
    | string.islower()：至少包含一个区分大小写的字符，并且都是小写为True
    | string.isnumeric()：只包含数字字符，返回True
    | string.isspace()：只包含空格返回True
    | string.istitle()：标题化的返回True
    | string.isupper()：全都是大写返回True
    | string.join(seq)：以string作为分隔符，将seq中所有的元素合并为一个新字符
    | stirng.ljust(width)：返回一个原字符串左对齐，并使用空格填充至长度width的新字符串
    | string.lower()：转换为小写
    | string.lstrip()：截掉string左边的空格
    | string.partition(str)：有点像find()和split()的结合体，从str出现的第一个位置起，吧字符串string分成一个3元组(string_pre_str,str,string_post_str)，如果string中不包括str,那么string_pre_str = string
                m = ' hello Python '
                print m.partition('haha') :(' hello Python ', '', '')
                print m.partition('ll') :(' he', 'll', 'o Python ')
    | string.replace(str1,str2,num=string.count(str1))：吧string中的str1替换成str2，如果num指定，则替换不超过num次
    | string.rfind(str,bg=0,end=len(string))：类似find()，从右边开始查找
    | string.rindex(str,beg=0,end=len(string))：类似index()，右边开始查找
    | string.rjust(width)：返回一个字符串右对齐，并使用空格填充到长度为width
    | string.rpartition(str)：类似partition()函数，右边开始查找
    | string.rstrip()：删除string字符串尾部的空格
    | string.split(str="",num=string.count(str))：以str分隔符切片string，如果num有指定值，则仅分割num个字符串
    | string.splitlines(num=stirng.count('\n'))：按照行分割，返回一个包含各行作为元素的里列表，如果指定num，则仅切片num行
    | string.startswith(obj,beg=0,end=len(string))：检查字符串是否以obj开头，返回True
    | string.strip([obj])：在string上执行lstrip()和rstrip()
    | string.swapcase：翻转string中的大小写
    | string.title()：返回"标题化"的string，也就是所有单词都是以大写开始
    | string.translate(str,del="")：根据str给出的表，转换string的字符，要过滤掉的字符放到del参数中
    | string.upper()：小写转为大写
    | string.zfill(width)：返回长度为width的字符串，右对齐，前面填充0
# 6.7 字符串的独特特性
    | 特殊字符串和控制字符
    | 三引号
    | 字符串不变性
# 6.8 Unicode
    程序中出现字符串时一定要加个前缀u
    不要用str()函数，用unicode()代替
    不要用过时的string模块
    不到必须的时候不要在你的程序中边学解码Unicod字符。只在你要写入文件或者数据库或者网络时，才调用encode()函数；相应的，值在你需要把数据读回来的时候才调用decode()函数
# 6.9 相关模块
    string,re,struct,c/StringIO,base64,...
# 6.10 字符串关键点总结
    一些引号分隔的字符
    不可分字符串类型
    字符串格式化操作（%）提供类似printf()的功能
    三引号
    原始字符串对每个特殊字符串都使用它的原意
    Python字符串不是通过NUL或者'\0'来结束的
# 6.11 列表
    可以包含不同类型的对象
# 6.12 caozuofu
    标准类型操作符
    序列类型操作符
        切片( [] 和 [:] )
        成员关系( in , not in)
        连接操作符 ( + )
        重复操作符 ( * )
# 6.13 内建函数
    | 标准类型函数:cmp()
        对两个列表的元素进行比较
        如果比较的元素是相同类型的，则比较值，返回结果
        如果两个元素不是同一类型，则检查他们是否是数字
            如果是数字，执行必要的数字强制类型转换，然后比较
            如果有一方的元素是数字，则另一方的元素”大“（数字是”最小的“）
            否则，通过类型名字的字母顺序进行比较
        如果有一个列表首先到达末尾，则另一个长一点的列表大
        如果我们用尽力两个列表的元素而且所有元素都是相等的，那么结果就是个平局，就是说返回一个0
    | 序列类型函数 ： len(),max(),min(),sorted(),reversed(),enumerate(),zip(),sum(),list(),tuple()
# 6.14 列表类型的内建函数
    | list.append(obj)
    | list.count(objc)
    | list.extend(seq) ： 把序列seq的内容添加到列表中
    | list.index(obj,i=0,j=len(list))
    | list.insert(index,obj)
    | list.pop(index=-1)：默认是最后一个
    | list.remove(obj)
    | list.reverse()
    | list.sort(func=None,key=None,reverse=False)：以指定的方式排序列表中成员，如果func和key参数指定，则按照指定的方式比较各个元素，如果reverse标识被置为True，则列表以反序排列
# 6.15 列表的特殊特性
    堆栈：
        LIFO
    队列：
        FIFO
# 6.16 元组
    一旦创建，不可变
# 6.17 元组操作符和内建函数
    标准类型操作符、序列类型操作符和内建函数
# 6.18 元组的特殊特性
    不可变性给元组带来了什么影响
# 6.19 相关模块
# 6.20 拷贝Python对象、深拷贝和浅拷贝
    浅拷贝：
        默认的拷贝方式
        完全切片([:]])、利用工厂函数(list(),dict())等、使用copy模块的copy函数。这些都得到的是浅拷贝
    深拷贝：
        需要copy模块的copy.deepcopy()函数
        非容器类型（比如数字，字符串和其他'原子'类型的对象）没有被拷贝一说，浅拷贝是用完全切片操作来完成的。
        如果元组变量值包含原子类型的变量，对他的深拷贝将不会进行
