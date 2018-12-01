---

## 参考资料
+ [百度百科](https://baike.baidu.com/item/Python#reference-%5B1%5D-21087-wrap)
+ [维基百科](https://en.wikipedia.org/wiki/Python_%28programming_language%29)

---

整理了一些百度百科和维基百科的内容：

### Python 简介

Python（英国发音：`/ˈpaɪθən/` 美国发音：`/ˈpaɪθɑːn/`）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人`Guido van Rossum`于 1989 年发明，第一个公开发行版发行于 1991 年。

Python 具有动态类型系统和自动内存管理，支持多种编程范式，包括面向对象、祈使、函数式编程和程序的样式。它有一个大型和全面的标准库。

### Python 设计定位

Python的设计哲学是“优雅”、“明确”、“简单”。Python开发者的哲学是“用一种方法，最好是只有一种方法来做一件事”。在设计Python语言时，如果面临多种选择，Python开发者一般会拒绝花俏的语法，而选择明确的没有或者很少有歧义的语法。这些准则被称为Python格言。在Python解释器内运行import this可以获得完整的列表。

Python开发人员尽量避开不成熟或者不重要的优化。一些针对非重要部位的加快运行速度的补丁通常不会被合并到Python内。所以很多人认为Python很慢。不过，根据二八定律，大多数程序对速度要求不高。在某些对运行速度要求很高的情况，Python设计师倾向于使用JIT技术，或者用使用C/C++语言改写这部分程序。可用的JIT技术是PyPy。

Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。有两个标准库`(functools, itertools)`提供了`Haskell`和`Standard ML`中久经考验的函数式程序设计工具。

Python可能被粗略地分类为`“脚本语言”（script language）`,而Python的支持者较喜欢称它为一种`高级动态编程语言`，原因是“脚本语言”泛指仅作简单程序设计任务的语言，如shellscript、VBScript等只能处理简单任务的编程语言，并不能与Python相提并论。

Python本身被设计为`可扩充的`。并非所有的特性和功能都集成到语言核心。Python提供了丰富的API和工具，以便程序员能够轻松地使用C语言、C++、Cython来编写扩充模块。Python编译器本身也可以被集成到其它需要脚本语言的程序内。因此，很多人还把Python作为一种`“胶水语言”（glue language）`使用。使用Python将其他语言编写的程序进行集成和封装。在Google内部的很多项目，例如Google Engine使用C++编写性能要求极高的部分，然后用Python或Java/Go调用相应的模块。《Python技术手册》的作者马特利（Alex Martelli）说：“这很难讲，不过，2004 年，Python 已在Google 内部使用，Google 召募许多 Python 高手，但在这之前就已决定使用Python，他们的目的是 Python where we can, C++ where we must，在操控硬件的场合使用 C++，在快速开发时候使用 Python。”

### Python 执行

Python在执行时，首先会将`.py`文件中的源代码编译成Python的`byte code（字节码）`，然后再由Python `Virtual Machine（Python虚拟机）`来执行这些编译好的byte code。

### Python 基本语法

Python的设计目标之一是让代码具备高度的可阅读性。它设计时尽量使用其它语言经常使用的标点符号和英文单字，让代码看起来整洁美观。

#### 缩进

Python开发者有意让违反了缩进规则的程序不能通过编译，以此来强制程序员养成良好的编程习惯。并且Python语言利用缩进表示语句块的开始和退出（Off-side规则），而非使用花括号或者某种关键字。增加缩进表示语句块的开始，而减少缩进则表示语句块的退出。缩进成为了语法的一部分。

#### 控制语句

- `if语句`，当条件成立时运行语句块。经常与`else`, `elif(相当于else if)` 配合使用。
- `for语句`，遍历列表、字符串、字典、集合等迭代器，依次处理迭代器中的每个元素。
- `while语句`，当条件为真时，循环运行语句块。
- `try语句`。与`except`,`finally`配合使用处理在程序运行中出现的异常情况。
- `class语句`。用于定义类型。
- `def语句`。用于定义函数和类型的方法。
- `pass语句`。表示此行为空，不运行任何操作。
- `assert语句`。用于程序调试阶段时测试运行条件是否满足。
- `with语句`。Python2.6以后定义的语法，在一个场景中运行语句块。比如，运行语句块前加密，然后在语句块运行退出后解密。
- `yield语句`。在迭代器函数内使用，用于返回一个元素。自从Python 2.5版本以后。这个语句变成一个运算符。
- `raise语句`。制造一个错误。
- `import语句`。导入一个模块或包。
- `from import语句`。从包导入模块或从模块导入某个对象。
- `import as语句`。将导入的对象赋值给一个变量。
- `in语句`。判断一个对象是否在一个字符串/列表/元组里。

#### 表达式

- 主要的算术运算符与C/C++类似。`+, -, *, /, //, **, ~, %`分别表示加法或者取正、减法或者取负、乘法、除法、整除、乘方、取补、取余。`>>, <<`表示右移和左移。`&, |, ^`表示二进制的AND, OR, XOR运算。`>, <, ==, !=, <=, >=`用于比较两个表达式的值，分别表示大于、小于、等于、不等于、小于等于、大于等于。在这些运算符里面`~, |, ^, &, <<, >>`必须应用于整数。
- Python使用`and, or, not`表示逻辑运算。
- `is, is not`用于比较两个变量是否是同一个对象。
- `in, not in`用于判断一个对象是否属于另外一个对象。
- Python支持`“列表推导式”（list comprehension）`，比如计算0-9的平方和:


```python
sum(x * x for x in range(10))
```


    285


- Python使用lambda表示匿名函数。匿名函数体只能是表达式。比如：


```python
add=lambda x, y : x + y
add(3,2)
```



    5


- Python使用`y if cond else x`表示条件表达式。意思是当`cond为真`时，表达式的值为`y`，否则表达式的值为`x`。相当于C++和Java里的`cond?y:x`。
    Python区分列表(list)和元组(tuple)两种类型。list的写法是[1,2,3]，而tuple的写法是(1,2,3)。可以改变list中的元素，而不能改变tuple。在某些情况下，tuple的括号可以省略。tuple对于赋值语句有特殊的处理。因此，可以同时赋值给多个变量，比如：


```python
 x, y=1,2   #同时给x,y赋值
print(x,y)
```

    1 2
    


```python
# 特别地，可以使用以下这种形式来交换两个变量的值：
x, y=y, x 
print(x,y)
```

    2 1


- Python使用'(单引号)和"(双引号)来表示字符串。
- Python支持序列的切片处理

#### 函数

Python的函数支持递归、默认参数值、可变参数，但不支持函数重载。为了增强代码的可读性，可以在函数后书写“文档字符串”(Documentation Strings，或者简称docstrings)，用于解释函数的作用、参数的类型与意义、返回值类型与取值范围等。可以使用内置函数help()打印出函数的使用帮助。

#### 对象的方法

对象的方法是指绑定到对象的函数。调用对象方法的语法是`instance.method(arguments)`。它等价于调用`Class.method(instance, arguments)`。当定义对象方法时，必须显式地定义第一个参数，一般该参数名都使用`self`，用于访问对象的内部数据。这里的self相当于C++, Java里面的this变量，但是我们还可以使用任何其它合法的参数名，比如this 和 mine 等，self与C++,Java里面的this不完全一样，它可以被看作是一个习惯性的用法，我们传入任何其它的合法名称都行。

#### 类型

Python采用**`动态类型系统`**。在编译的时候，Python不会检查对象是否拥有被调用的方法或者属性，而是直至运行时，才做出检查。所以操作对象时可能会抛出异常。不过，虽然Python采用动态类型系统，它同时也是强类型的。Python禁止没有明确定义的操作，比如数字加字符串。

与其它面向对象语言一样，Python允许程序员定义类型。构造一个对象只需要像函数一样调用类型即可，比如，自定义的Fish类型，使用Fish()。类型本身也是特殊类型type的对象(type类型本身也是type对象)，这种特殊的设计允许对类型进行反射编程。

Python内置丰富的数据类型。与Java、C++相比，这些数据类型有效地减少代码的长度。下面这个列表简要地描述了Python内置数据类型(适用于Python 3.x)：

类型(Type)|描述|例子
:-|:-|:-
`str`|字符串|`'Wikipedia'`,`"Wikipedia"`,`"""Spanning multiple lines"""`
`bytes`|不可变字节序列|`b'Some ASCII'`, `b"Some ASCII"`
`unicodes`|Unicode字符串|`u'Hello`
`list`|可以包含多种类型的可改变的序列|`[4.0, 'string', True]`
`tuple`|可以包含多种类型的不可改变的序列|`(4.0, 'string', True)`
`set, frozenset`|与数学中集合的概念类似。无序的、每个元素唯一。|`{4.0, 'string', True}`,`frozenset([4.0, 'string', True])`
`dict`|一个可改变的由键值对组成的映射。|`{'key1': 1.0, 3: False}`
`int`|精度不限的整数|`42`
`float`|浮点数。精度与系统相关。|`3.1415927`
`complex`|复数|`3+2.7j`
`bool`|逻辑值。只有两个值：真、假|`True`,`False`
`bytearray`|可变字节序列|`bytearray(b'Some ASCII')`,`bytearray(b"Some ASCII")`,`bytearray([119, 105, 107, 105])`

除了各种数据类型，Python语言还用类型来表示函数、模块、类型本身、对象的方法、编译后的Python代码、运行时信息等等。因此，Python具备很强的动态性。

Python允许像数学的常用写法那样连着写两个比较运行符。比如`a < b < c`与`a < b and b < c`等价。C++的结果与Python不一样，首先它会先计算a < b，根据两者的大小获得0或者1两个值之一，然后再与c进行比较。
