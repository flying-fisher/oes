# HTML

### 入门

HTML（HyperText Markup Language，超文本标记语言）和CSS（Cascading Style Sheets，层叠样式表）用于创建网页。Web服务器存储并提供由HTML和CSS创建的网页，浏览器获取页并显示网页的内容。

- HTML用于建立网页的结构。
- CSS用于控制HTML的表现。



HTML利用标记标示内容，提供结构。我们将匹配标记及其包围的内容称为元素。

- 元素通常由3部分组成：开始标记+内容+结束标记。
- 开始标记中可以使用属性，小写属性
- 结束标记的标记名前有"/"



所有HTML页面都有<html>元素，其中还有<head>元素和<body>元素

- 网页信息放在<head>元素中

- <body>元素中的内容将在浏览器页面中显示

- 浏览器会忽略大多数空白符（制表符、回车、空格），但可以使用空白符让HTML更具可读性

- CSS 可以通过以下方式添加到HTML中:

  - 内联样式- 在HTML元素中使用"style"属性
  - 内部样式表 - 在HTML文档头部<head>中使用<style>元素来包含CSS
  - 外部引用 - 使用外部CSS文件

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <title>一个页面</title>
    </head>
    <body style="background-color:yellow;">
      <h1 style="font-family:verdana;">一个标题</h1>
      <p style="font-family:arial;color:red;font-size:20px;">一个段落。</p>
    </body>
  </html>
  ```

  ​

### HTML <head>元素

<head> 元素包含了所有的头部标签元素，用于定义文档的信息。

可以添加在头部区域的元素标签为: <title>, <style>, <meta>, <link>,  <script>, <noscript>, 和<base>

- <title>元素定义文档标题
- <style>元素定义了HTML文档的样式文件引用地址，也可以直接添加样式来渲染 HTML 文档
- <meta>元素提供了元数据。元数据不显示在页面上，但会被浏览器解析，META 元素通常用于指定网页的描述，关键词，文件的最后修改时间，作者，和其他元数据。元数据可以使用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他Web服务。
- <link>元素定义了一个文档和外部资源之间的关系
- <script>元素定义了客户端的脚本文件
- <noscript>元素
- <base>元素标签描述了基本的链接地址/链接目标，该标签作为HTML文档中所有的链接标签的默认链接

### 块级元素与内联元素

- 块级block-level元素在浏览器显示时，通常会以新行来开始（和结束），如: <h1>, <p>, <ul>, <table> 等
- 内联inline元素在显示时通常不会以新行开始，如: <b>, <td>, <a>, <img>等

### 超文本

标记语言（ML）用于描述网页结构，而超文本（HT）则代表该文本中具有链接到其他文本的链接点。

使用<a>元素创建链接点

- 属性herf指定了链接的目标文件，可以使用相对路径指向同一网站的其他文件

- <a>元素的内容为链接的标签，可以为文字或图像

  ```html
  <p><a href="http://www.runoob.com" target="_blank">这是一个链接</a></p>

  <p>图片链接:
    <a href="http://www.runoob.com/html/html-tutorial.html">
  	<img  border="0" src="smiley.gif" alt="HTML 教程" width="32" height="32">
    </a>
  </p>
  ```

- 链接到当前文本的其他位置：使用<a>元素的id属性创建不显示的书签标记

  ```html
  <p><a href="#C4">查看章节 4</a></p>

  <h2>章节 1</h2>
  <h2>章节 2</h2>
  <h2>章节 3</h2>
  <h2><a id="C4">章节 4</a></h2>
  ```

### 文本格式化

```html
<!DOCTYPE html>
<html>
  <head> 
    <meta charset="utf-8"> 
    <title>菜鸟教程(runoob.com)</title> 
  </head>
  <body>

    <em>强调文本</em><br>
    <strong>加粗文本</strong><br>
    <dfn>定义项目</dfn><br>
    <code>一段电脑代码</code><br>
    <samp>计算机样本</samp><br>
    <kbd>键盘输入</kbd><br>
    <var>变量</var>

  </body>
</html>
```

### HTML表格

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>
每个表格从一个 table 标签开始。 
每个表格行从 tr 标签开始。
每个表格的数据从 td 标签开始。
</p>

<h4>一列:</h4>
<table border="1">
<tr>
  <td>100</td>
</tr>
</table>

<h4>一行三列:</h4>
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
</table>

<h4>两行三列:</h4>
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>

<h4>两行三列:</h4>
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>

</body>
</html>
```



###  <div> 和 <span>元素

作为容器将HTML元素组合起来

```html
<html>
  <head> 
    <meta charset="utf-8"> 
    <title>菜鸟教程(runoob.com)</title> 
  </head>
  <body>

  <div id="container" style="width:500px">

    <div id="header" style="background-color:#FFA500;">
    <h1 style="margin-bottom:0;">主要的网页标题</h1></div>

    <div id="menu" style="background-color:#FFD700;height:200px;width:100px;float:left;">
      <b>菜单</b><br>
      HTML<br>
      CSS<br>
      JavaScript</div>

    <div id="content" style="background-color:#EEEEEE;height:200px;width:400px;float:left;">
    	内容在这里</div>

    <div id="footer" style="background-color:#FFA500;clear:both;text-align:center;">
    	版权 © runoob.com</div>

  </div>

  </body>
</html>
```

### HTML 表单和输入

HTML 表单用于收集不同类型的用户输入

- 使用表单标签 <form> 来设置的包含表单元素的区域

- 表单元素是允许用户在表单中输入内容,比如：文本域(textarea)、下拉列表、单选框(radio-buttons)、复选框(checkboxes)等等

  ```html
  <form>
    文本域：<input type="text" name="firstname"><br>
    密码字段：<input type="password" name="pwd"><br>
    单选框：<input type="radio" name="sex" value="male">Male<br>
    <input type="radio" name="sex" value="female">Female<br>
    复选框：<input type="checkbox" name="vehicle" value="Bike">I have a bike<br>
    <input type="checkbox" name="vehicle" value="Car">I have a car <br>
  </form>
   
  <form name="input" action="html_form_action.php" method="get">
    	提交内容: <input type="text" name="user">
    	<input type="submit" value="提交按钮">
  </form> 

  ```

  ​