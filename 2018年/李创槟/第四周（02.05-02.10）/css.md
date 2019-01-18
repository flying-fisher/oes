# **CSS******

**CSS样式******

1、为什么需要CSS样式表。首先，HTML标签的外观样式比较单一：颜色只有黑白，字体类型和大小无变化。其次，样式表的作用相当于华丽的衣服。重要，样式表能实现内容与样式的分离，方便团队开发，程序员写代码，美工做样式

2、要使用CSS，首先在&lt;head&gt;标签中添加&lt;style type=”text/css”&gt;&lt;/style&gt;。然后在&lt;style&gt;标签下声明选择器。选择器的构成为：  选择器名{属性:值;属性:值;.....}。选择器名实际就是一个标签名。样式表可实现标签的统一管理。

3、选择器可以不用标签名而改成通用类名，类名前加”.”，在要使用该选择器的标签加入属性class，值设置为类名，则该标签的样式更改为此类

4、常用的属性样式

文字属性：

1)font-size：字体大小

2)font-family：字体类型，宋体等，但一般是英文

3)font-style：字体样式，如倾斜加粗等，italic

4)color：文本颜色

5)text-align：文本对齐

方框属性：

1)margin:四个边界

2)margin-top：局部边界，还有left，right，bottom

3)border-width：边框宽度

4)border-right-width：边框局部宽度

5)border-style：边框样式，如solid实线，dashed虚线

6)border-left-style：边框局部样式

7)border-color：边框颜色

8)border-top-color：边框局部颜色

9)padding：四个填充

10)padding-left：局部填充。还有right，top，bottom

背景属性：

1)background-image：用于块级元素，背景图片，值为url

2)background-repeat：是否平铺，如no-repeat不平铺

3)Background：背景，可以是图片url，也可以是颜色

超链接：

1)a:link选择器：链接默认样式

2)a:visited选择器：链接点击过的样式

3)a:hover选择器：鼠标移到链接的样式

4)a:active选择器：鼠标点中链接的样式

5)无下划线属性：text-decoration：none;

**引入方式******

1、样式表的三种应用方式

1)内嵌样式表，即使用类选择器。用于希望网页内所有同类标签采用统一样式

2)行内(嵌入)样式表，即直接在标签中用style属性，不推荐。

3)外部样式表文件，方便管理，最常用。在html文档外部建立css文件。css文件中可以只有选择器。然后在html中的&lt;head&gt;标签下，使用&lt;link href:”(css文件路径)” rel:”stylesheet” type:”text/css”&gt;标签。或者在&lt;style&gt;&lt;/style&gt;标签下@import url(“(css文件路径)”)进行导入

**CSS选择器******

1、要使用CSS对HTML页面中的元素实现一对一，一对多，多对一的控制就需要用到CSS选择器。HTML页面中的元素就是通过CSS选择器进行控制的。

2、*基础的选择器：***

1)*：通用元素选择器，匹配任何元素

2)E：标签选择器，匹配所有使用E标签的元素

3).info和E.info：class选择器，匹配所有class属性中包含info的元素。一个元素可以引用多个class选择器。class可以有很多个

4)#info和E#info：id选择器，匹配所有id属性等于info的元素，主要用于javascript。Id只能有一个

*组合选择器：***

1)E，F：多元素选择器，用时匹配所有E和F元素，E和F之间用逗号隔开

2)E F：后代元素选择器，匹配所有属于E元素后代的F元素，E和F之间用空格隔开。如果一个元素嵌套在另一个元素下，则一个元素是另一个元素的后代。

3)E&gt;F：子元素选择器，匹配所有E的子元素F，E和F用大于号隔开。后代可以是嵌套中再加嵌套，而子元素只能是第一个嵌套

4)E+F：毗邻元素选择器，匹配所有紧随E元素之后的同级元素F，E和F之间用加号隔开

* *

*属性选择器：***

1)E[att]：匹配所有具有att属性的E元素，不考虑它的值(E可以省略，[]不可省略，下同)

2)E[att=”val”]：匹配所有att属性等于”val”的E元素

3)E[att~=”val”]：匹配所有att属性其中一个值等于”val”的E元素

4)E[att|=”val”]：匹配att属性以”val”开头的所有E元素

*伪类选择器：***

1)E:link：匹配所有未被点击的链接

2)E:visited：匹配所有已被点击的链接

3)E:active：匹配鼠标已经按下还未释放的E元素

4)E:hover：匹配鼠标悬停其上的E元素

5)E:focus：匹配获取当前焦点的E元素。聚焦一般对文本框有效，即点击文本框

结构性伪类选择器**：******

1)E:root：匹配文档的根元素，即&lt;html&gt;

2)n编号从1开始，可以使odd奇数，even偶数，也可以是表达式3n+0等

3)E:nth-child(n)：匹配其父元素的第n个子元素

4)E:nth-last-child(n)：匹配其父元素的倒数第n个子元素

5)E:nth-of-type(n)：匹配同种标签的父元素的第n个子元素

6)E:nth-last-of-type(n)：匹配同种标签的父元素的倒数第n个子元素

7)E:last-child：匹配父元素的最后一个子元素，同E:nth-last-child(1)

8)E:first-of-type：匹配父元素下同种标签的第一个子元素，同E:nth-of-type(1)

9)E:last-of-type：匹配父元素下同种标签的第一个子元素，同E:nth-last-of-type(1)

10)E:only-child：匹配父元素下仅有的一个子元素

11)E:only-of-type：匹配父元素下使用同种标签的唯一一个子元素

12)E:empty：匹配一个不包含子元素的元素。注意：文本也被看做子元素