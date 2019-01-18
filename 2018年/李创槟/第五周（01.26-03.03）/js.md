**了解javascipt******

1、是一种基于对象和事件驱动并具有安全性的解释性语言，目的是增强和WEB客户交互。弥补了HTML的缺陷。

2、*可以*使网页更具有交互性，给用户提供更好的体验。确保用户在表单中输入有效的信息，可以节省业务开支。即时创建HTML页面。还可以处理表单，设置cookie，创建基于WEB的应用程序

3、*不可以*读写客户机器上的文件。不允许写服务器上的文件。不能关闭不是由它打开的窗口。不能从来自另一个服务器的已经打开的网页中读取信息**

**脚本如何写******

1、脚本写在&lt;head&gt;&lt;/head&gt;中。

2、标准定义：&lt;script type=”text/javascript&gt;&lt;/script&gt;

3、在&lt;script&gt;标签下写程序代码

4、alert(“hello world”)弹出提示窗口，有确认按钮。

5、Confirm(“hello world”)确认对话框，有确认和取消按钮。

6、Prompt(“how old are you”,”23”)为回答对话框，有默认回答，有确认取消按钮

7、document.write(“hello world”)输出文本

8、可以在&lt;script&gt;标签下定义函数function a(){}。然后在标签中onclick=”a()”，加载事件驱动。不建议用关键字作函数名

**关闭一个浏览器窗口**

1、标签关闭：&lt;a href=”javascipt:self.close()”&gt;关闭窗口&lt;/a&gt;

2、按钮关闭：在函数中加入代码，function a(){window.close();}。加入标签&lt;input type=”button” value=”close” onclick=”a()”&gt;

**语言基础******

1、基本数据类型

a) 整型：只能储存整数。可以十、八、十六进制。八进制数字前加”0”。十六进制数字前加”0x”

b) 浮点型：能储存小数。某些平台对浮点型支持不稳定，尽量不用

c) 字符串型：用双引号或单引号包起来的0个或多个字符，引号可以嵌套使用

d) 布尔型：常用语判断，只有true和false两个值，两个值是保留字，属于常数

2、声明变量：var&lt;变量&gt;[=&lt;值&gt;]; 如：var a=10;var b=10.3;var c=”sfds”;var d=true;

3、变量命名要求

a) 只包含字母、数子、/、_

b) 只能用字母和_开头

c) 不能太长，最好控制在10个以内

d) 不能使用javascript关键字做变量名

e) 区分大小写

4、没有声明的变量不能使用，否则会出错：“未定义”

5、变量作用域：全局变量定义在所有函数体外；局部变量定义在函数体内，只对该函数可见

6、转义字符：一些字符在屏幕不能显示或者在javascript语法上有特殊用途，用到这些字符要用转义字符。以\开头，如\’单引号、\”双引号、\n换行、\r回车

7、表达式：算数表达式，字符串表达式，赋值表达式等

8、运算符优先级 ： [!、-、++、--]、[*、/、%]、[+、-]、[&lt;&lt;、&gt;&gt;、&gt;&gt;&gt;]、[&lt;、&lt;=、&gt;、&gt;=]、[==、!=、===、!==]、[&、^、|]、[&&、||]、[?:]、[=、+=、-=、*=、/=、%=、&=、^=、|=、&lt;&lt;=、&gt;&gt;=]

9、数组声明：var arr=[0,1,2,3,4];操作则取arr[0]

10、控制语句

a) 选择结构：if、if/else、?:、switch

b) 循环结构：for、while、do/while

c) 特殊循环： for(var i in arr){}遍历对象每个元素

d) break、continue、return条件控制

**函数介绍******

1、函数是由事件驱动的或者当它被调用时执行的可重复使用的代码块

a) 函数被调用时，它是运行在他被声明时的语法环境中的

b) 函数自己无法运行，它总是被对象调用的，函数运行时，函数体内的this指针指向调用该函数的对象，如果调用函数时没有明确指明对象，this默认指向window

c) 函数是一种带有可执行代码的对象类型数据

2、参数是函数的传入值。如：function add(a,b){}全局变量可以被内部函数引用，而局部变量无法被外部函数引用

3、函数调用就是指直接使用函数名对函数进行调用，事件驱动是指在标签中给该函数定义了驱动的事件发生后函数才能被调用

4、Javascript是面向过程的。事件驱动有两种方式，一种是在标签中,onclick=”fun”;一种是&lt;button id=”button”&gt;调用&lt;/button&gt;

 &lt;script type=”text/javascript&gt;document.getElementById(“button”).onclick=fun;&lt;/script&gt;

5、如果&lt;script&gt;标签下使用window.onload=function(){}，那么文档加载完才会调用这个函数

6、匿名函数就是没有名字的函数，可以用来当参数传递，在ajax被当成回调函数

7、闭包一般用于变量初始化，只会执行一次，后面不会被调用，所以是匿名函数，如(function(){alert(“hello world!”)})();

8、对象有属性，方法，子对象，实例:

Var person={

Name:”job”,

Eat:function(){},

Eys:{

Name:”眼睛”,

Scroll:function(){}

}

}

调用： person.eat();

9、namespace即命名空间，可以理解为对象，用于多人开发时避免命名冲突

10、可以像css一样，单独建立一个js文件，里面写JavaScript代码，然后在调用的html文档中的&lt;script&gt;标签中加入属性src，值为js文件路径

**内置对象String******

1、String字符串。声明方法。一种var str=”str”;更常用。一种var str=new String(“str”);

2、属性：length。用法：&lt;字符串对象&gt;.length。作用：返回该字符串长度

3、方法：

a)charAt()。用法&lt;字符串对象&gt;.charAt(&lt;位置&gt;)。作用：返回位于参数处的单个字符。位置从0开始 

b)charCodeAt()。用法：类似charAt()，只是返回的是ascll码

c)String.fromCharCode(a,b,c...)。返回一个字符串，每个字符的ascll码由参确定

 	d)indexOf()。用法：返回参数在字符串所在位置，从0开始，为-1则不存在

e)split()。用法：&lt;字符串对象&gt;.split(&lt;分隔符字符&gt;);作用：返回一个由分隔符分割的数组

f)subString()。用法：&lt;字符串对象&gt;.subString(&lt;始&gt;[,&lt;终&gt;]);作用：返回原字符串的子串，如果没有，则返回空。如果没有终的参数，则返回始参数到原字符串尾

g)substr()。与subSting()类似，但是&lt;终&gt;改为&lt;长&gt;。返回从&lt;始&gt;开始长度为&lt;长&gt;的子串

h)toLowerCase()。用法：&lt;字符串对象&gt;.toLowerCase()。返回全小写字符串

i)toUpperCase()。用法：&lt;字符串对象&gt;.toUpperCase()。返回全大写字符串

**内置对象Array数组******

1、数组定义方法：var&lt;数组名&gt;=new Array();  数组下标从0开始

2、要添加元素，就用：&lt;数组名&gt;[&lt;下标&gt;]=...;（在这里的方括号不是省略，而是语法）

3、如果要在定义数组时直接初始化。则：var&lt;数组名&gt;=new Array(&lt;元素1&gt;,&lt;元素2&gt;,...);

4、或者直接赋值。var &lt;数组名&gt;=[&lt;元素1&gt;,&lt;元素2&gt;,...];

5、要遍历数组。就用：for(var &lt;自定变量名&gt; in &lt;数组名&gt;){}

6、Javascript只有一维数组。要使用多维数组就是用虚拟法：var &lt;数组名&gt;=new Array(new Array(),new Array(),...);  调用时则用：&lt;数组名&gt;[&lt;一维下标&gt;][&lt;二维下标&gt;][...]

7、二维数组直接定义法：var &lt;数组名&gt;=[[&lt;元素&gt;,...],[&lt;元素&gt;,...],...];

8、遍历二维： for(var i in arr){for(var j in arr[i]){}}，普通的for循环也可以

9、属性：length。用法：&lt;数组对象&gt;.length。返回数组长度即元素个数

10、方法：

a) join()。用法：&lt;数组对象&gt;.join(&lt;分隔符&gt;);返回字符串，内容为所有数组元素，用分隔符拼接而成

b) reverse()。用法：&lt;数组对象&gt;.reverse();使数组元素顺序颠倒

c) slice()。用法：&lt;数组对象&gt;.slice(&lt;始&gt;[,&lt;终&gt;]);返回数组子集。无&lt;终&gt;则取到结尾

d) sort()。用法：&lt;数组对象&gt;.sort([&lt;方法函数&gt;]);默认按照字母顺序排序。如果指定方法函数，则按照方法函数指定的排序方法排序。按照数字大写排序方法function(a,b){return a-b;}

**内置对象Math******

1、属性：用法为：Math.&lt;属性名&gt;

a) E：返回自然数e，即2.71828....

b) LN2：返回2的自然对数

c) LN10：返回10的自然对数

d) LOG2E：返回以2为底e的对数

e) LOG10E：返回以10为底e的对数

f) PI：返回圆周率，即3.1415...

g) SQRT1_2：返回1/2的平方根

h) SQRT2：返回2的平方根

2、方法：用法为：Math.&lt;函数名&gt;(&lt;参数&gt;)

a) acos(x)：返回x的反余弦值。asin(x)：返回x的反正弦值。atan(x)：返回x的反正切值。用弧度表示

b) atan2(x,y)：返回复平面内点(x,y)对应的复数的幅角，用弧度表示，-pi~pi

c) sin(x)：返回x的正弦值。cos(x)：返回x的余弦值。tan(x)：返回x的正切值

d) exp(x)：返回自然数e的x次幂。log(x)：返回x的自然对数

e) abs(x)：返回x的绝对值

f) ceil(x)：返回大于等于x的最小整数。floor(x)：返回小于等于x的最大整数。round(x)：返回x的四舍五入后的值

g) max(a,b)：返回a和b中较大的数。min(a,b)：返回a和b中较小的数

h) pow(n,m)：返回n的m次幂

i) random()：返回0~1的一个随机数

j) sqrt(x)：返回x的平方根

**内置对象Date******

1、声明：var &lt;对象名&gt;=new Date([&lt;年&gt;,&lt;月&gt;,&lt;日&gt;]); 无参数则表示当前时间

2、方法：get方法为返回，set方法为设置，下面只列举get方法

a) getFullYear()。用法：&lt;对象名&gt;.getFullYear()。返回四位数年份

b) getYear()。用法：&lt;对象名&gt;.getYear()。返回二位数年份

c) getMonth()。用法：&lt;对象名&gt;.getMonth()。返回月份，0表示1月

d) getDate()。用法：&lt;对象名&gt;.getDate()。返回该月的第几天

e) getDay()。用法：&lt;对象名&gt;.getDay()。返回星期几。0表示周日

f) getHours()。用法：&lt;对象名&gt;.getHour()。返回小时。24小时制

g) getMinutes()。用法：&lt;对象名&gt;.getMinutes()。返回分钟

h) getSeconds()。用法：&lt;对象名&gt;.getSeconds()。返回秒

i) getMilliseconds()。用法：&lt;对象名&gt;.getMilliseconds()。返回毫秒，1~999

j) getTime()。用法：&lt;对象名&gt;.getTime()。返回1970年1月1日到日期对象指定时间的毫秒数

k) getTimezoneOffset()。返回对象时区与格林威治相差的分钟数。在东方为负数

l) toString()。返回日期对象时间。格式为：Fri Jul 21 15:43:46 UTC+0800 2016

m) toLocaleString()。返回日期对象时间。格式为：2016-07-21 15:43:46

n) toGMTString()。用GMT格式返回日期对象时间

o) toUTCString()。用UTC格式返回日期对象时间

p) parse()。用法：Date.parse(&lt;日期对象&gt;);返回该日期对象的内部表达方式

3、函数setInterval()。用法setInterval(&lt;方法&gt;,&lt;刷新间隔&gt;);方法可以是匿名方法，刷新间隔	单位为毫秒

**全局函数******

1、eval(&lt;字符串&gt;)。把参数当做标准语句或表达式运行

2、isFinite(&lt;数&gt;)。如果参数是有限的返回true；否则返回false。MIN_VALUE和MAX_VALUE之间

3、IsNaN(&lt;数&gt;)。如果参数是非数字值返回true；否则返回false

4、parseInt(&lt;字符串&gt;)。把参数转为整数。如果无法转成整数，返回NaN

5、parseFloat(&lt;字符串&gt;)。把参数转为浮点数。如果无法转成浮点数，返回NaN

6、toString()。用法：&lt;对象&gt;.toString([&lt;进制&gt;]);把对象转化成字符串

**宿主对象******

1、使用浏览器的内部对象系统（宿主对象），可实现与HTML文档进行交互，它的作用是将相关元素组织包装起来，提供给程序设计人员使用，从而减轻劳动，提高设计WEB页面的能力

2、浏览器对象(navigator)：提供有关浏览器的信息

3、屏幕对象(screen)：反映了当前用户的屏幕设置

4、窗口对象(windows)：处于对象层次的最顶端，提供了处理navigator窗口的属性和方法

5、位置对象(location)：提供了与当前打开的URL一起工作的方法和属性，是静态对象

6、历史对象(history)：提供了与历史清单有关的信息

7、文档对象(document)：包含了与文档元素(element)一起工作的对象，将这些元素包装起来供编程人员使用

**浏览器对象******

1、属性

a) appCodeName：返回浏览器的代码名，IE返回Mozilla

b) appName：返回浏览器名，IE返回Microsoft Internet Explorer

c) appVersion：返回浏览器版本号，包括版本号，语言，操作平台等

d) language：返回浏览器编译语言

e) platfrom：返回操作平台

** **

** **

**屏幕对象******

1、描述屏幕的显示及颜色属性。属性：

a) availHeight：屏幕区域的可用高度，单位是px分辨率

b) availWidth：屏幕区域的可用宽度

c) colorDepth：颜色深度256/8 16/16 32M/32

d) height：屏幕区域的实际高度，比如除去任务栏

e) width：屏幕区域的实际宽度

**窗口对象******

1、方法：

a) open()：打开一个新窗口，大部分只能在IE下有用，第一个参数为url，第二个为窗口名，第三个参数为窗口状态参数，如下：

i. alwaysLowered：是否将窗口显示的堆栈后推一层

ii. alwaysraised：是否将窗口显示的堆栈上推一层

iii. dependent：是否将该窗口与当前窗口产生依存关系

iv. fullscreen：是否满屏显示

v. directories：是否显示连接工具栏

vi. loction：是否显示网址工具栏

vii. memubar：是否显示菜单工具栏

viii. scrollbars：是否显示滚动条

ix. status：是否显示状态栏

x. titlebar：是否显示标题栏

xi. toolbar：是否显示标准工具栏

xii. resizable是否可以改变窗口的大小

xiii. screenX：窗口左边界距离

xiv. screenY：窗口右边界距离

xv. top：窗口上边界

xvi. width：窗口宽度

xvii. height：窗口高度

xviii. left：窗口左边界

xix. outerHeight：窗口外边界高度

xx. personalbar：是否显示个人工具栏

实例：

&lt;script type=”text/javascript”&gt;

Window.onload=function(){

document.getElementById(“button”).onclick=function(){

Window.open(“screen.html”,”screen”,”width=300px,heigth=300px”);

}

}

}

2、父窗口与子窗口通信，前端设计时尽量不用，用于早期IE：

实例：

//创建窗口

Var newWin=null：

newWin=window.open(“test.html”,”hellow”,”width=300,height=300”);

//传值给子窗口

newWin.document.getElementById(“subtext”).value=document.getElementById(“text”).value;

//子窗口传值给父窗口

window.opener.document.getElementById(“text”).value=document.getElementById(“subtext”).value;

**位置对象******

1、属性

a) hash：锚点名称

b) host：主机名称，hostname：host:port

c) href：完整的URL字符串

d) pathname：路径

e) port：端口

f) protocol：协议

g) search：查询信息

2、方法

a) reload()：重新加载，可以代替刷新功能

b) replace()：用指定的网页取代当前网页，并且按下“后退”键无法返回

**历史对象******

1、方法：

a) back()：回到上一个历史记录中的网址，可以代替后退功能

b) forward()：回到下一个历史记录中的网址，可以代替前进功能

c) go(&lt;整数x或URL&gt;)：前往历史记录中的网址（整数大于0前进x个页面，小于0后退x个页面，等于0刷新）

**DOM******

1、DOM是Document Object Model文档对象模型的缩写

2、DOM是一个平台，一个中立于语言的应用编程接口（API），允许程序访问并更改文档的内容、结构、样式

3、简单说，DOM规定了HTML,XML等的一些规范，使JavaScript可以根据这些规范进行各种操作

4、创建节点：

a) 方法：document.createElement(&lt;节点类型&gt;);

b) 如创建div节点：var div=document.createElement(“div”);

5、添加节点：

a) 方法：document.&lt;节点&gt;.appendChild(&lt;节点&gt;);

b) 如插入div节点：document.body.appendChild(div);

6、插入节点：

a) 方法：document.&lt;节点&gt;.insertBefore(&lt;新节点&gt;,&lt;下一个节点&gt;);

b) 如在第一节点前插入新节点：document.body.insertBefore(div,document.body.childNodes[0]);

7、删除节点：

a) 方法：document.&lt;节点&gt;.removeChild(&lt;节点&gt;);

b) 如删除第一个节点：document.body.remove(document.body.childNodes[0]);

8、替换节点：

a) 方法：document.&lt;节点&gt;.replaceChild&lt;新节点&gt;,&lt;旧节点&gt;);

b) 如：document.body.replaceChild(div,body.children[0]);

**常用处理事件******

1、onfocus：聚焦时触发的事件

2、onblur：失去焦点时触发的事件

3、onsumit：提交表单时触发的事件

4、window.onload：窗口加载完毕触发的事件

5、onmouseover：鼠标经过时触发的事件

6、onmouseout：鼠标移除时触发的事件

实例：

&lt;script type=”text/javascript”&gt;

window.onload=function(){

document.getElementById(“a”).onfocus=function(){

if(this.value.==”请输入账号”)

this.value=””;

};

}

document.getElementById(“a”).onfocus=function(){

if(this.value.length==)

this.value=””;

};

}

}

&lt;/script&gt;

&lt;/head&gt;

&lt;body&gt;

账号:&lt;input id=”a” type=”text” value=”请输入账号”/&gt;

&lt;body&gt;