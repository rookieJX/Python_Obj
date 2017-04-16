# 10.1 什么是异常
    | 错误
    | 异常
# 10.2 Python中的异常
所有错误，无论是语义还是逻辑上的，都是由于和Python解释器不相容导致的，其后果就是引发异常
    | NameError:尝试访问一个未申明的变量
        表示我们访问了一个没有初始化的变量
    | ZeroDivisionError:除数为0
    | SyntaxError:Python解释器语法错误
        是唯一一个不是在运行时发生的异常
    | IndexError:请求的索引超出序列范围
    | KeyError:请求一个不存在的字典关键字
    | IOError:输入/输出错误
    | AttributeError:尝试访问位置的对象属性
# 10.3 检测和处理异常
异常可以通过try语句来检测
主要形式：try-except 和 try-finally.这两个语句是互斥的
    | try-except 语句
    | 包装内建函数
        def safe_float(obj):
            try:
                retval = float(obj)
            except ValueError:
                retval = 'could not convert non-number to float'
        return retval
    | 带有多个except的try语句
    | 处理多个异常的except语句
        def safe_float(obj):
            try:
                retval = float(obj)
            except (ValueError,TypeError):
                retval = 'could not convert non-number to float'
        return retval
    | 捕获所有异常
        try:
           :
        except Exception,e:
    | 异常参数
    | 在应用使用我们封装的函数
    | dels子句
    | finally子句
    | try-finally 语句
    | try-except-else-finally:厨房一锅端
# 10.4 上下文管理
    | with 语句
    try-finally 和 try-except语句的一种特定的配合用法是保证共享的资源的唯一分配，并在任务结束的时候释放他。比如文件（数据，日志，数据库等）、线程资源、简单同步、数据库连接，等。with语句的目标就是应用在这种场景。
    with open('/etc/passwd','r') as f:
        for eachline in f:
            # do ...
    这段代码片段是，如果一切正常，吧文件对象赋值给f.然后用迭代器遍历文件中的每一行，当完成时，关闭文件。无论的在这一段开始，中间，还是结束是发生异常，会至此那个清理的代码，此外文件仍会自动的关闭
# 10.6 触发异常
    | raise 语句
        语法与惯用法
    raise [SomeException [, args [, traceback]]]
    第一个参数 SomeException,是触发异常的名字。如果有，必须是一个字符串，类或实例。
    第二个符号为可选的args，来传给异常
# 10.7 断言
断言是一句必须等价于布尔真的判定，发生异常也以为这表达式为假
    | 断言语句
    assert expression[,arguments]
    -----示例----
    assert 1==1
    assert 2+2 == 2*2
    AssertionError 异常和其他的异常一样可以用 try-except 语句块捕捉，但是如果没有捕捉，他将终止程序运行，并且会提供一个如下的跟踪记录
# 10.8 标准异常
    | BaseException           所有异常的基类
    | SystemExit              Python解释器请求退出
    | KeyboardInterrupt       用户中断执行（通常是输入^c）
    | Exception               常规错误的基类
    | StopIteration           迭代器没有更多的价值
    | GeneratorExit           生成器发生异常来通知退出
    | StandardError           所有的内建标准异常的基类
    | ArithmeticError         所有数值计算错误的基类
    | FloatingPointError      浮点计算错误
    | OverflowError           数值运算超出最大限制
    | ZeroDivisionError       除（或者取模）零（所有数据类型）
    | AssertionError          断言语句失败
    | AttributeError          对象没有这个属性
    | EOFError                没有内建输入，到达EOF标记
    | EnvironmentError        操作系统错误的基类
    | IOError                 输入/输出操作失败
    | OSError                 操作系统错误
    | WindowsError            Windows系统调用失败
    | ImportError             导入模块/对象失败
    | LookupError             无效数据查询的基类
    | IndexError              序列中没有此索引
    | KeyError                映射中没有这个键
    | MemoryError             内存溢出错误（对于Python解释器不是致命的）
    | NameError               未声明/初始化对象（没有属性）
    | UnboundLocalError       访问未初始化的本地变量
    | ReferenceError          弱引用视图访问已经垃圾回收了的对象
    | RuntimeError            一般的运行时错误
    | NotImplementedError     尚未实现的方法
    | SyntaxError             Python语法错误
    | IndentationError        缩进错误
    | TabError                Tab和空格混用
    | SystemError             一般的解释器系统错误
    | TypeError               对类型无效的操作
    | ValueError              传入无效的参数
    | UnicodeError            Unicode相关的错误
    | UnicodeDecodeError      Unicode解码时的错误
    | UnicodeEncodeError      Unicode编码时错误
    | UnicodeTranslateError   Unicode转换时错误
    | Warning                 警告的基类
    | DeprecationWarning      关于被弃用的特性的警告
    | FutureWarning           短语构造将来语句会有改变的警告
    | OverflowWarning         旧的关于自动提升为长整形（long）的警告
    | PendingDeprecationWarining 关于特性将会被废弃的警告
    | RuntimeWarning          可疑的运行时行为的警告
    | SyntaxWarning           可以的语法的警告
    | UserWarning             用户代码生成的警告
