# 8.1 if语句
组成部分：关键字本身，用于判断结果真假的条件表达式，以及当表达式为真或者非零时执行的代码块
if expression:
    expr_true_suite
    | 多重条件表达式
        单个if语句可以通过使用布尔操作符and,or 和not实现多重判断条件或是否判断条件。
    | 单一语句的代码块
        符合语句的代码块仅仅包含一行代码，那么可以写一行上
# 8.2 else语句
if expression:
    expr_true_suite
else:
    expr_false_suite
    | 避免“悬挂else”
        强制缩进，代码对其
# 8.3 elif（即else-if）语句
# 8.4 条件表达式（即“三元操作符”）
X if C else Y
# 8.5 while语句
如果条件为真会一直执行，直到循环条件不再为真
    | 一般语法
    | 计数循环
    | 无线循环
# 8.6 for语句
    | 一般语法：访问一个可迭代对象
        for  in
    | 用于序列类型
        - 通过序列项迭代 for eachName in list:
        - 通过序列索引迭代  for nameIndex in range(len(list)):
        - 使用项和索引迭代 for i,eachName in enumerate(list):
    | 用于迭代器类型
    | range() 内建函数
    | xrange() 内建函数 类似于range() 性能高，不完全拷贝
    | 与序列相关的内建函数
        sorted(),reversed(),enumerate(),zip()
# 8.7 break语句
可以结束当前循环，跳转到下条语句
# 8.8 continue语句
# 8.9 pass语句
    不做任何事情
# 8.10 再谈else语句
# 8.11 迭代器和iter()函数
    | 什么是迭代器：他为序列对象提供了一个类序列的接口
    | 为什么要迭代器：
        提供了可扩展的迭代器接口：
        对列表迭代带来了性能上的增强
        在字典迭代中性能提升
        创建真正的迭代接口，而不是原来的随机对象访问
        与所有已经存在的用户定义的类以及扩展的模拟序列和映射的对象向后兼容
        迭代飞序列集合时，可创建更简洁可读的代码
    | 如何迭代
    | 使用迭代器：
        序列：for i in seq:
        字典：for i in dict:
        文件：myFile = open('')  - for eachLine in myFile:
    | 可变对象和迭代器
        在迭代可变对象的时候修改他们并不是好主意。因为除了列表外其他的序列都是不可变的，一个序列的迭代器只是记录你当前到达多少个元素，如果你在迭代时改变了元素，更新会立即反映到你所在的条目上
    | 如果创建迭代器
        对于一个对象调用iter()就可以得到迭代器
# 8.12 列表解析 [expr for iter_var in iterable if cond_expr]
# 8.13 生成器表达式 (expr for iter_var in iterable if cond_expr)
    列表解析的一个不足之处就是必须生成所有的数据，用于创建这个列表。这可能对有大量数据的迭代器有负面效应。生成器表达式通过结合列表解析和生成器解决了这个问题
