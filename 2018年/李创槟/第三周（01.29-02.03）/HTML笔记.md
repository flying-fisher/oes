**HTML概述******

1、HTML是一种制作万维网页面的标准语言

a) 是一种标记语言，有成对的，也有单个的标签

b) 通过浏览器执行

c) 语法不区分大小写

**HTML版本******

1、可以分为两大版本

a) HTML4.01：以前的网页制作标准，各浏览器互相排斥，语法比较乱

b) HTML5：作为HTML的第五次重大修改，仍处于完善之中。

i. 大部分现代浏览器已经具备某些HTML5支持

ii. 不同浏览器执行可能会有差异

iii. 对移动webapp支持良好

c)	被废弃的元素：&lt;acronym&gt;、&lt;applet&gt;、&lt;basefont&gt;、&lt;big&gt;、&lt;center&gt;、&lt;dir&gt;、&lt;font&gt;、&lt;frame&gt;、&lt;frameset&gt;、&lt;noframes&gt;、&lt;strike&gt;、&lt;tt&gt;等

d)	在开发环境下，默认文档类型则改为HTML5

**基本结构******

&lt;!doctype html&gt;    //代表当前网页基于HTML5语法

&lt;html&gt;

&lt;head&gt;文档元信息&lt;/head&gt;

&lt;body&gt;网页主体内容&lt;/body&gt;

&lt;/html&gt;

**基本知识******

1、注释：注释会被浏览器直接忽略。格式为：&lt;!--内容--&gt;

2、&lt;head&gt;下的标签：

a) &lt;meta&gt;：单一标签，用于描述一个HTML网页文档的属性。charset属性用于描述文档编码

b) &lt;title&gt;：双标签，用于描述HTML网页标题

3、标记中可以有一个或多个属性，属性就是对标签的具体设置，不同标签属性可能有不同的属性，也可能有相同属性。在&lt;body&gt;中设置属性可以应用到整个页面，常用属性：

a) bgcolor：背景颜色，

b) text：文字颜色

4、网页颜色表示法

a) 16进制表示法，如#000000黑色到#ffffff白色

b) 英文关键字表示法，选择较少，不推荐。如：red

c) RGB表示法，常用于CSS，如白色rgb(255,255,255)

**文字和段落******

1、基本文字格式：

a) 加粗，将文字用&lt;b&gt;&lt;/b&gt;包含起来

b) 倾斜，将文字用&lt;i&gt;&lt;/i&gt;包含起来

c) 下划线，将文字用&lt;u&gt;&lt;/u&gt;包含起来

d) 三个功能平行，可以嵌套

**段落格式******

1、在源代码中的换行空格等是无法在网页中显示出来的

2、段落：将一个自然段的文字用&lt;p&gt;&lt;/p&gt;包含起来，在网页可以显示成一段。段间有段间距。

a) 属性：align 值：left(默认)，right，center，justify(基线对齐)

3、换行：&lt;br&gt;可以作为一个换行符，为单一标签

**标题文字******

1、标题标签H1~H6，字体依次从最大到最小的双标签。如&lt;h1&gt;&lt;/h1&gt;

2、属性：align 值：left(默认)，right，center，justify(基线对齐)

**PRE预格式化文本******

1、如果希望源代码格式原封不动显示到网页上，就用&lt;pre&gt;&lt;/pre&gt;将这段文字包含起来

**列表******

1、OL有序列表，UL无序列表，LI列表元素。每个列表可以包含多个li子标签

2、OL列表元素前会显示序号。可以设置属性type，可以设置为1/a/A/i/I等

3、UL列表元素前无序号，默认显示为实心圆点。最常用。可以设置属性type，可以设置为circle(空心圆)，square(实心方块)等

4、OL和UL都可以嵌套，做成多级列表

**DL DT DD标签******

1、类似于列表，对标题和内容会产生格式化效果，内容会自动缩进。

a) &lt;DL&gt;&lt;/DL&gt;代表一个完整的列表。

b) &lt;DT&gt;&lt;/DT&gt;代表标题，其中可以包含&lt;h1&gt;&lt;/h1&gt;作为标题文字

c) &lt;DD&gt;&lt;/DD&gt;代表内容

**图片******

1、使用&lt;img&gt;单一标签

2、必须属性：

a) src：值为URL，规定显示图像的URL

3、常用可选属性：

b) alt：值为text，规定图像的替代文本。在图片不正常显示时显示

a) height：定义图像高度，只设置一个则会等比例缩放

b) width：设置图像宽度

c) 其他属性不常使用，推荐用CSS设置样式

**超级链接******

1、在&lt;a&gt;&lt;/a&gt;中包含链接载体，可以是文字，也可以图片等。

2、属性href的值代表链接的路径，为URL，可以是网页或其他文件

3、若链接文件浏览器能直接打开，则显示。不能直接打开则采取下载的方式

4、URL有绝对路径和相对路径

a) 绝对路径，如http://www.baidu.com

b) 相对路径，my/hello.html。要求在用一个根目录下

4、target属性：

a) _self：默认值，在本窗口打开

b) _blank：在新空白窗口打开

c) 其他

5、空链接：herf属性设置为#，网页不做任何跳转。作用：内容未实现

6、调用javascript：herf属性设置为javascript:alert(1);作用：调用JS程序

6、锚点，可以理解为书签。作用：点击链接后移动到本网页的某一个地方

a) 设定锚点：在需要设置位置处添加a标签，设置name属性作为标记

b) 属性href设置为#&lt;锚点名称&gt;，如#top，点击后即可回到锚点处****

**水平线******

1、&lt;hr&gt;单一标签，起到分割作用

2、不推荐使用其属性，而是用CSS设置，如：align，size，width等。设置width为百分比，则可以随着父容器大小改变，设置为像素，则大小固定不变

3、HTML有些特殊属性不需设置属性值，如&lt;hr&gt;的noshade属性，可以使水平线没有凹效果

**表格元素******

1、table标记：表格。th标记：标题行。tr标记：行。td标记：单元格。作用：排版布局

2、常用属性：

a) 不推荐使用：align：水平对齐。calign：垂直对齐。bgcolor：背景颜色

b) width：宽度，可以百分比，也可以像素。

c) border：边框宽度。大多数设置为0，即不出现边框。像素。

d) cellpadding：规定边框与内容的间距。百分比或像素

e) cellspacing：规定单元格之间的空白。百分比或像素

3、对tr改变属性，则子td属性全部改变；对td改变属性，则只对该单元格生效

**合并单元格(不建议)******

1、在&lt;td&gt;标签下，加colspan属性表示跨列，属性的值为跨多少列

2、在&lt;td&gt;标签下，加rowspan属性表示跨行，属性的值为跨多少行

**嵌套表格(建议)******

1、表格嵌套表格：若表格间每一行的单元格个数都不同，或每一列单元格的个数不同，就需要用到嵌套表格。

2、每一行个数不同实现方法是：在一个&lt;tr&gt;&lt;td&gt;标签下再增加&lt;table&gt;标签，嵌套下的table只有一行，因此只有一个&lt;tr&gt;标签。

3、每一列单元格的个数不同实现方法是：增加&lt;table&gt;&lt;/table&gt;标签，与该行的其他&lt;td&gt;&lt;/td&gt;标签平行

**内联元素和块级元素******

1、内联元素(inline)：

a) 可以多个元素同处一行的空间

b) 常见的内联元素：SPAN,A,STRONG,EM,LABEL,INPUT,SELECT,TEXTAREA,IMG,BR

c) 通过CSS样式，可以把一些内联元素也变成块级元素；或反过来

2、块级元素(block)：

a) 每个元素必须独占一行空间

b) 常见的块级元素：DIV,FORM,TABLE,P,PRE,H1~H6,DL,OL,UL

c) 除了&lt;p&gt;标签不允许嵌套，其他标签基本都可以嵌套

**DIV绝对定位******

1、id属性代表给一个元素起一个唯一的标志

2、在类选择器中设置position:absolute;实现绝对定位

3、每一个DIV都处在单独的一层

4、类选择器中的z-index属性设置z坐标及层次坐标，越大显示优先级越高

5、类选择器中的visibility属性设置div的可见性。visible可见，hidden则不可见

6、类选择器常见还有width，height，background-color等属性

**DIV浮动布局(应用较广)******

1、在类选择器中设置浮动属性float，则设置了float属性的div处于同一个输出流中，可以实现不同DIV处在同一行中。float可设置为left,center,right

2、通过clear:both可以清除浮动

**带语义的布局元素(相对于HTML4.1有重大改革)******

1、语义化标签

a) 就是尽量使用有相对应的结构的含义HTML的标签，如table是表格，img是图片

b) 带语义的布局元素解决了DIV嵌套过多，代码可读性变差的问题

2、语义化的布局元素，整体还是放在DIV中，为最外层容器

a) article：标签装载显示一个独立的文章内容

b) section：标签定义文档中的节（section、区段）

c) aside：用来装载非正文类的内容

d) hgroup：用于对网页或区段的标题元素（H1~H6）进行组合

e) header：定义文档的页面头部，通常是一些引导和导航信息

f) footer：定义section或document的页脚

g) nav：定义导航链接

3、从上往下，从左往右进行布局

4、语义化标签本身只是标签，并不能真正的实现排版的功能，只有加上CSS才能实现排版

**HGROUP******

1、与H1~H6标题标签相关

2、作用是将H标签包含起来，形成一个标题组，使代码结构清晰

 



**表单元素******

1、form表单：表单用于向服务器传输数据，本身是一个不可见元素。表单能够包含表单元素，比如文本字段、复选框、单选框、提交按钮等等

2、常用元素：

a) name：给表单起名

b) method：默认为get，一般使用post

c) action：值为url。向url提交数据

3、表单元素的通用属性

a) name：是必须设置的属性，服务器通过该属性识别表单元素从而获取数据

b) value：是常用属性，设置表单元素默认值

c) disabled：禁用，单一属性，表示表单元素失效

d) placeholder：文本框中灰字提示，内容为空时显示

e) auofocus：单一属性，自动获取焦点

4、单行文本框：最常用，&lt;input type=”text”&gt;。常用属性

a) size：文本框大小

b) maxlength：允许输入的最大长度

c) readonly：只读（无法获得焦点），单一属性

5、密码框：特殊的单行文本框，&lt;input type=”password”&gt;。输入文本不显示，用圆点表示

6、文本区域：内容较多的文本框，&lt;textarea&gt;&lt;/textarea&gt;。默认值不用value属性，而是直接写在&lt;textarea&gt;标签下

7、单选按钮：几选一的情况，&lt;input name=”xxx” type=”radio”&gt;。一组中同一时间只能选一个，同一组name属性值相同。要设置默认值，则添加单一属性checked

8、复选按钮：多选多的情况，&lt;input name=”xxx” type=”checkbox”&gt;。要设置默认值，则添加单一属性checked

9、列表框：&lt;select name=”xxx”&gt;&lt;/select&gt;。默认的默认值是第一个列表框元素

10、列表框元素：&lt;option value=”xxx”&gt;&lt;/option&gt;。要设置默认值，则添加单一属性selected

11、隐藏域：不可视元素，&lt;input name=”xxx” type=”hidden”&gt;。在提交表单时仍然提交，用于不需用户看到仍需提交的情况

12、文件域：上传文件按钮，&lt;input type=”file” name=”xxx”&gt;。点击按钮弹出文件选择对话框

13、提交按钮：最常用&lt;input type=”submit” name=”xxx” value=”提交”&gt;。将表单内容提交

14、重置按钮：&lt;input type=”reset” name=”xxx” value=”重置”&gt;。将表单恢复成默认状态，而不是清空

15、按钮：&lt;input type=”button” name=”xxx” value=”注册”&gt;。无预置功能，用于自定义

**HTML5新增表单元素(浏览器不支持时当成普通元素  部分无法在PC端显示)******

1、查询文本框：&lt;input type=”search”&gt;。文本框右边有”X”可以清空文本框内容。常用于搜索和查询

2、列表提示：&lt;datalist id=”xxx”&gt;&lt;/datalist&gt;。本身依赖于文本框，使文本框聚焦时会有列表提示。在文本框中需要设置list属性值为列表提示的id的值以进行绑定。输入时匹配提示项进行显示，点击文本框右边的倒三角也可以显示列表提示框

3、列表提示元素：&lt;option value=”xxx” label=”xxx”&gt;&lt;/option&gt;。左边为value，右边为label

4、数字文本框：&lt;input type=”number” max=”9” min=”0”&gt;。只能输入数字，最大值为max，最小值为min。右边有上下箭头进行加减，过界就不变。step属性设置步长，默认为1

5、滑动条：&lt;input type=”range” max=”9” min=”0” value=”5” step=”2”&gt;。起始值value，最大值max，最小值min，步长step(默认为1)

6、颜色文本框：&lt;input type=”color” value=”#000000”&gt;。点击按钮打开颜色选取对话框。文本框显示选择的颜色，默认颜色为value

7、电话文本框：&lt;input type=”phone”&gt;。无法在PC端看到效果。点击按钮后自动在手机端调用数字输入虚拟键盘

8、网址输入：&lt;input type=”url”&gt;。希望用户输入网址。调用网址输入虚拟键盘

9、邮箱输入：&lt;input type=”email”&gt;。希望用户输入邮箱。调用邮箱输入虚拟键盘

10、日期选择：&lt;input type=”date” max=”2100-01-01” min=”1900-01-01” value=”2016-01-01”&gt; 最大可选日期max，最小可选日期min，默认日期value

11、时间选择：&lt;input type=”time” max=”18:00:00” min=”12:00:00” value=”15:00:00”&gt; 最大可选时间max，最小可选时间min，默认时间value

12、UTC日期时间：&lt;input type=”datetime”&gt;。在手机浏览器中才能显示效果。末尾显示Z

13、本地时间：&lt;input type=”datetime-local”&gt;。本地时间。选择日期+时间。

**Fieldset标记******

1、本身严格来说不算表单元素，但一般用于美化表单。是一个环绕表单的外框

2、用法：&lt;fieldset&gt;&lt;legend&gt;xxx&lt;/legend&gt;&lt;form&gt;&lt;/form&gt;&lt;fieldset&gt;

3、&lt;legend&gt;XXX&lt;/legend&gt;中XXX就是外框要显示的文字信息，在外框左上角

**度量和进度条******

1、度量&lt;meter&gt;&lt;/meter&gt;：默认为一个横向短柱形条。类似于手机电池显示条

2、度量属性：

a) min：柱型条起点值

b) max：柱形条终点值

c) low：低值临界点，低于此显示黄色

d) high：高值临界点，高于此显示黄色

e) value：柱形条当前值，不超过临界点显示绿色

3、进度条&lt;progress&gt;&lt;/progress&gt;：默认为一个横向短柱形条，默认时动画效果灰色小块左右来回弹。

4、进度条属性：

a) max：柱形条终点值

b) min：柱形条起点值

c) value：进度条当前值，不再动

**浮动框架******

1、框架：

a) 在页面中嵌入其他页面

b) HTML5取消了拆分式的frameset和frame

c) HTML5保留了浮动框架(嵌入框架、内联框架)iframe

2、浮动框架：不对页面做拆分，在网页局部位置上直接嵌入网页

3、使用：&lt;iframe&gt;&lt;/iframe&gt;，缩放比例嵌入。属性：

a) src：重要属性，代表嵌入网页的url

b) frameboarder：框架边框。为0时无边框

c) width：宽度。百分比或像素

d) height：高度。百分比或像素

e) scrolling：滚动条。yes(始终有),no(始终无),auto(内容超出有,默认)

f) name：规定名称，作为浮动框架标识

4、通过&lt;a href=”test.html” target=”name”&gt;，将target的值设置为&lt;ifame&gt;的name属性，可将链接动作在指定的框架内发生。

**实体字符******

1、HTML中的预留字符必须被替换成为字符实体

a) 在HTML中，某些字符时预留的

b) 不能使用小于号(&lt;)和大于号(&gt;)，因为浏览器会误认为它们是标签

c) 如果希望显示预留字符，必须使用字符实体进行转义

2、字符实体类似于：&amp;&lt;实体名&gt;;或&amp;#&lt;实体号&gt;;

3、常用字符实体

a) &lt;：&amp;lt分号

b) &gt;：&amp;rt分号

c) 空格： &amp;nbsp分号

d) “：&amp;quot分号

e) &amp;：&amp;amp分号

4、如果希望显示字符实体，也要做一些转义，将&amp;符号改为&amp;即可

**Embed音频视频(不完全推荐使用)******

1、&lt;embed&gt;单一标签：可以在网页中嵌入音频和视频

2、不同浏览器对音频视频格式的支持也不同

3、如果浏览器不支持该文件格式，没有插件就无法播放该音频视频

4、如果用户的计算机未安装插件，无法播放音频视频

5、属性：

a) src：必须属性，值为嵌入文件的url

b) width：宽度。百分比或像素

c) height：高度。百分比或像素

**HTML自己播放音频******

1、HTML5在不适用插件的情况下也可以原生的支持音频格式文件播放，格式为

a) Ogg

b) MP3

c) Wav

2、&lt;audio&gt;&lt;/audio&gt;：定义声音，如音乐或其他音频流。在标签下放置文本内容，当浏览器不支持时就可以显示不支持该标签的信息。

3、属性：

a) src：音频文件的url

b) controls：单一属性，向用户显示播放控件

c) autoplay：单一属性，音频就绪后就马上播放

d) loop：单一属性，音频播放结束后重新播放

**HTML5自己播放视频******

1、HTML5能在完全脱离插件的情况下播放视频，支持格式为：

a) Ogg：带有Theora视频编码+Vorbis音频编码

b) MPEG4：带有H.264视频编码+ACC音频编码

c) WebM：带有VP8视频编码+Vorbis音频编码

2、&lt;video&gt;&lt;/video&gt;：定义视频，如电影或其他视频流。在标签下放置文本内容，当浏览器不支持时就可以显示不支持该标签的信息。

3、属性：

a) src：视频文件的url

b) controls：单一属性，向用户显示播放控件

c) autoplay：单一属性，视频就绪后就马上播放

d) loop：单一属性，视频播放结束后重新播放

e) width：宽度。百分比或像素

f) height：高度。百分比或像素

4、VIDEO常用API

a) 方法：play()、pause()、load()、canPlayType()

b) 属性：currentSrc、currentTime、playbackRate、muted

c) 事件：play、pause、progress、ended

5、如果希望自己设置按钮来代替controls控制面板，则用javascript

a) 声明：&lt;script type=”text/javascript&gt;&lt;/script&gt;

b) 获取视频变量：var video=document.getElementById(“xx”);

c) 声明函数: function play(btn){}

d) 暂停时播放：if(xx.paused){xx.play();btn.value=’暂停’;}

e) 播放时暂停：else{xx.pause();btn.value=’播放’;}

f) 给按钮加上事件：&lt;input id=”play” type=”button” value=”播放” onClick=”play(this)”&gt;

g) 播放结束时将按钮值改为”播放”：xx.onended=function(){}

h) 函数添加事件：funtion(){document.getElementById(“play”).value=”播放”;}

i) 希望添加两个按钮，快进和后退

j) &lt;input type=”button” value=”快进10s” onClick=”forback(10)”&gt;

k) &lt;input type=”button” value=”后退10s” onClick=”forback(-10)”&gt;

l) 添加快进函数：function forback(i){xx.currentTime+=i;}

m) 希望添加三个按钮，快放和慢放和正常倍速

n) &lt;input type=”button” value=”3倍速快放” onClick=”speed(3)”&gt;

o) &lt;input type=”button” value=”3倍速慢放” onClick=”speed(1/3)”&gt;

p) &lt;input type=”button” value=”正常倍速播放” onClick=”speed(1)”&gt;

q) 添加变速函数：function speed(i){xx.playbackRate=i;}

**Canvas画布和SVG******

1、canvas和SVG都允许在浏览器中创建图形，但是它们在根本上是不同的

a) Svg绘制出来的每一个图形元素都是独立的DOM节点，可方便后期绑定事件或修改，而canvas输出的是一整幅画布

b) Svg输出的图形是矢量的，后期可以修改参数来自由放大缩小，无失真，canvas输出标量画布，就像一整张图片

**Canvas画布******

1、HTML5中&lt;canvas&gt;&lt;/canvas&gt;标签用于绘制图像（通过脚本，通常是javascript）

2、&lt;canvas&gt;元素本身并没有绘制能力（它仅仅是图形的容器），必须使用脚本完成实际绘图的任务。

3、getContext()方法可返回一个对象，该对象提供了用于在画布上绘图的方法和属性

4、&lt;canvas&gt;&lt;/canvas&gt;中间包含的文字可以在浏览器不支持画布时显示

5、也可以在javascript中用异常抛出语句检测是否支持画布：

try{

document.createElement(‘canvas’).getContext(‘2d’);

alert(“支持画布”);

}catch(e){

alert(“不支持画布”);

}

6、javascript中绘制线条函数：

Function drawLine(sx,sy,ex,ey){

var canvas1=document.getElementById(‘canvas1’);//获得画布对象

var context=canvas1.getContext(‘2d’);//获得2d绘制对象

context.beginPath();//绘制开始路径

context.moveTo(sx,sy);//把画笔移动到指定位置作为起点

context.lineTo(ex,ey);//把画笔移动到特定位置作为终点

context.strokeStyle=’#ff0000’//设置线条颜色

context.stroke();//画制一个线条

}

7、在javascript中调用线条函数

window.onload=function(){

drawLine(0,0,200,200);

}

**Canvas的API******

1、线条样式

a) lineCap：设置或返回线条的结束端点样式

b) linejoin：设置或返回两线条相交时，所创建的数据类型

c) lineWidth：设置或返回当前的线条宽度

d) meterLimit：设置或返回最大斜坡长度

2、矩形

a) rect()：创建矩形

b) fillRect()：绘制填充矩形

c) strokeRect()：绘制无填充矩形

d) clearRect()：在给定的矩形内清除指定的像素

**Canvas画布绘制矩形******

1、在body中声明画布

&lt;canvas id=”canvas1” width=”200” height=”200” style=”border:1px #CCCCCC solid”&gt;

您的浏览器不支持画布操作

&lt;/canvas&gt;

2、javascript中写绘制矩形函数

function drawRect(){

var canvas1=document.getElementById(‘canvas1’);//获得画布对象

var context=canvas1.getContext(‘2d’);//获得2d绘制对象

//四个参数：起点x坐标，y坐标，宽度，高度

context.strokeRect(100,100,40,40);//绘制无填充

context.fillStyle(“#ff0000”);//给填充矩形设置颜色，默认为黑色

context.fillRect(10,20,100,50);//绘制有填充

}

3、初始化

window.onload=function(){

drawRect();

}

**Canvas画布绘制图片******

4、javascript中写绘制图像函数

Function drawCanvas(image1){

var canvas1=document.getElementById(‘canvas1’);//获得画布对象

var context=canvas1.getContext(‘2d’);//获得2d绘制对象

//五个参数：图片对象，x坐标，y坐标，宽度，高度

context.drawImage(image1,10,10,image1.width,image1.height);//绘制图片到画布中

}

5、由于浏览器加载图片对象需要一定时间，分开写初始化函数

Function init(){

var image1=new Image();//绘制图片对象

image1.src=’xxx.jpg’;//给对象指定图片

image1.onload=function(){//图片加载完后调用绘制画布程序

drawCanvas(image1);

};

}

3、在javascript中调用初始化函数

window.onload=function(){

init();

}

**SVG图形******

1、什么是SVG

a) SVG指可伸缩矢量图形(Scalable Vector Graphics)

b) SVG用于定义用于网络的基于矢量的图形

c) SVG使用XML格式定义图形

d) SVG图像在放大或改变尺寸的情况下图形质量不会有损失

e) SVG是万维网联盟的标准

2、与其他图像格式相比(如JPG,GIF)，SVG的优势

a) SVG图像可通过文本编辑器创建和修改

b) SVG图像可被搜索、索引、脚本化或压缩

c) SVG是可伸缩的

d) SVG图像可在任何分辨率下被高质量打印

e) SVG可在图像量不下降的情况下被放大

3、可直接通过&lt;svg&gt;标签创建，无需借助javascript

4、实例：

&lt;svg width=”300” height=”300”&gt;

&lt;rect x=”10” y=”10” width=”30” height=”30” stroke=”black” fill=”transparent” strok-width=”5”&gt;   //stoke为描边颜色，fill为填充色

&lt;rect x=”60” y=”10” rx=”10” ry=”10” width=”30” height=”30” stroke=”black” fill=”transparent” strok-width=”5”&gt;   //圆角矩形，rx和ry属性表示圆角大小

&lt;circle cx=”25” cy=”75” r=”20” stroke=”red” fill=”transparent” stroke-width=”5”&gt;

&lt;ecllipse cx=”25” cy=”75” rx=”20” ry=”5” r=”20” stroke=”red” fill=”transparent” stroke-width=”5”&gt;//椭圆 cx和cy为圆心，rx和ry属性表示圆角大小，r为半径

&lt;line x1=”10” x2=”50” y1=”110” y2=”150” stroke=”orange” fill=”transparent” stroke-width=”5”&gt;//直线 x1和y1为起点坐标，x2和y2为终点坐标

&lt;polylien points=”60 110 65 120 70 115 75 130 80 125 85 140 90 135 95 150 100 145” stroke=”orange” fill=”transparent” stroke-width=”5”&gt;//折线 points设置顶点的xy坐标对

&lt;polygon points=”50 160 55 180 70 180 60 190 65 205 58 195 35 205 40 190 30 100 45 180” stroke=”green” fill=”transparent” stroke-width=”5”&gt;//五角星 多边形在points中设置每个顶点的xy坐标。和折线的区别是最后一点要封死

&lt;/svg&gt;