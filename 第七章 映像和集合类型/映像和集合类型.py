# 7.1 映射类型：字典
字典：唯一的映射类型。
    | 创建：dict = {} ，fdit = dict((['x',1],['y',2])) ， ddict = {}.fromkeys('x','y',-1)
    | 访问：
        for key in dict2.keys():
        for key in dict2:
        dict2['name']
    | 更新：
    | 删除字典元组和字典
# 7.2 映射类型操作符
不支持拼接和重复这样的操作。这些操作只对序列有意义
    | 标准类型操作符
    | 映射类型操作符
        字典的键查找操作符([])
            d[k]v : 通过键'k'，给字典中某元素赋值'v'
            d[k] : 通过键'k'，查询字典中某元素的值
        （键）成员关系操作（in 、 not in）
# 7.3 映射类型的内建函数和工厂函数
    | 标准类型函数[type()、str()和cmp()]
        cmp() : 用来比较大小，首先是字典的大小，然后是键，最后是值的大小，一般么米啥用（长度 -- 键 -- 值 -- 完全匹配）
    | 映射类型相关的函数
        dict() : 工厂函数，用来创建字典，无参数会生成空字典。
        len() : 长度
        hash() : 可以判断某个对象是否可以做一个字典的键
# 7.4 映射类型内建方法
    | dict.keys() 、 dict.values() 、 dict.items()
    | dict.clear() : 删除字典中所有元素
    | dict.cop() : 返回字典的一个浅赋复制的一个副本
    | dict.fromkeys(seq,val=None) : 创建并返回一个新字典，以seq中的元素做该字典的键，val做该字典中所有键对应的初始值，默认为None
    | dict.get(key,default=None) : 对字典dict中的键key，返回他对应的值，如果不存在则返回default
    | dict.has_key(key) : 如果键key在字典中存在，返回去True，可用 in 、 not in代替，
    | dict.items()
    | dict.keys()
    | dict.iter() : 方法iteritems()、iterkeys()、itervalues()与他们对应的非迭代方法一样，不同的是他们返回一个迭代子，而不是一个列表
    | dict.pop(key,[default]) : 和get() 相似。如果字典中key存在，删除并返回dict[key]；如果key不存在，如果有default，返回[default]；如果default不存在，报KeyError错误
    | dict.setdefault(key,default = None) : 和方法set()相似，如果字典中不存在key，由dict[key]=default为他赋值
    | dict.update(dict2) : 将字典dict2的键值对添加到字典dict中
    | dict.values()
    | dict.sorted() : 返回排序
# 7.5 字典的键
    | 不允许一个键对应多个值
    | 键必须是可哈希的（值相等的数字表示相同的键 也就是 1 和 1.0表示的哈希值是相同的）
# 7.6 集合类型
集合对象是一组无序的可哈希的值
    | 如何创建集合类型和给集合赋值
        与列表[] 和字典{} 不同，无特别的语法格式，被创建的唯一方法--用集合的工厂方法 set() 和 frozenset()
        s = set('che')  --  print s === seet(['c','h','e'])
    | 如何访问 in 、 not in
    | 如何更新 s.add() s.update() s.remove() s-=set()
# 7.7 集合类型操作符
    | 标准类型操作符 in,not in
        等价/不等价（>= , <=）
        子集/超集 （子集：<,<=）（超集：>,>=）
    | 集合类型操作符
        联合（|）
        交集（&）
        差补/相对补集（-）
        对称差分（^: 异或）
    | 集合类型操作符（仅适用于可变集合）
        update ( |= ) 等价于 update()
        Retention/Intersection Update ( &= ):保留操作保留与其他集合的共有成员也就是交集 等价于 intersection_update()
        Difference Update ( -= ):差更新
        Symmetric Difference Update: 异或更新
# 7.8 内建函数
    | 标准类型函数 len()
    | 集合类型工厂函数 set()  frozenset()
# 7.9 集合类型内建方法
    | 方法（所有的集合方法）
        s.issubset(t) : s是t子集返回True
        s.issuperset(t) : s是t的超级返回True
        s.union(t) : 并集
        s.intersection(t) : 交集
        s.difference(t) : 返回新集合，是s成员但是不是t成员
        s.symmetric_difference(t) : 是s或者t成员，但不是共有的
        s.copy() : 浅复制
    | 方法（仅适用于可变集合）
s.update(t) :
s.intersection_update(t) : s中的成员是共同属于s和t的元素
s.difference_update(t) : s中的成员是属于s但是不包含在t中的元素
s.symmetric_difference_update(t) : s中的成员更新为那些包含在s或者t中，但是不是s和t共有的元素
s.add(obj)
s.remove(obj)
s.discard(obj) : 如果obj是集合s中的元素，从集合s中删除对象obj
s.pop() : 删除集合s中的任意一个对象，并返回它
s.clear() : 删除集合s中的所有元素
