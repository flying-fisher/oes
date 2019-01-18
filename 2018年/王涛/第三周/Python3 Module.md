##Python3 Module

#### 引入模块

首先用文本编辑软件写入一下代码，并保存为fibo.py文件。这就创建了一个module，因为module是一段Python代码的集合。

``` python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result 
```

我们可以通过`>>>import fibo`来使用里面的内容（这里是两个定义的函数）

```python
>>> fibo.fib(1000)
>>> 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
>>> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__      # __name__是文件名字
>>> 'fibo'
```

####Executing modules as scrips

`python`后面的两个参数是会以List的形式存储在sys.argv中。想使用，需要`import sys`

```
python fibo.py <arguments>
```

在fibo.py文件末尾处增加以下内容

```
print(__name__)
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

使用命令行运行模块文件的时候，Python解释器会把特殊变量`__name__`置为`__main__`，所以会执行fib(50)

```
$ python fibo.py 50
__main__
1 1 2 3 5 8 13 21 34
```

#### 模块搜索目录

当引入一个模块时，会首先在内置模块区搜索，如果找不到，会继续搜索在`sys.path`（`sys`模块中的一个变量）定义的目录列表。`sys.path`初始为：

- 包含输入脚本文件的目录（若没有指定文件则为当前目录）


- `PYTHONPATH`(系统中环境变量`PYTHONPATH`包含的目录).
- The installation-dependent default.

可以输入通过以下代码来查看在`sys.path`中储存的目录List

```
>>>import sys
>>>sys.path
```

因为`sys.path`是一个List变量，可以通过`append`来增加自己指定的目录。因为这种方法是在运行时修改，运行结束后失效。

第二种方法是设置环境变量`PYTHONPATH`，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

#### dir（）函数

内置的dir()函数用来查看一个module定义的names，它返回一个字符串列表

```
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
 '__package__', '__stderr__', '__stdin__', '__stdout__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
 '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
 'call_tracing', 'callstats', 'copyright', 'displayhook',
 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
 'thread_info', 'version', 'version_info', 'warnoptions']
```

#### 包

包（Packages）是Python中的组织结构，用来包含modules