使用`urllib.request`库来保存网站上的图片。 
测试网站是豆瓣电影上某电影海报网址 
使用以下code成功的建立了一个文件夹，并且在其中 
保存该页面上的17张海报图片。

```python
from urllib import request
import os

def url_open(url):
    req = request.Request(url)
    response = request.urlopen(url)
    html = response.read()
    return html

def find_imgs(url):             
    html = url_open(url).decode('utf-8') 
    '''
    img_addrs = []                 
    a = html.find('img src=')
    while a != -1:                 
        b = html.find('.jpg',a, a+100) 
        if b != -1:
            c = html[a+9:b+4]     
            if 'view' in c:      
                print(c)          
                img_addrs.append(c)   
        else:                     
            b = a + 100             
        a = html.find('img src=',b)
      '''
    return img_addrs

def save_imgs(folder,img_addrs):
    os.mkdir(folder)         
    os.chdir(folder)         
    for each in img_addrs: 
        filename = each.split("/")[-1]
        with open(filename,'wb')as f:
            img = url_open(each)
            f.write(img)

def download_jpg():
    folder = 'D:/eclmn/tobeD' 
    url = "https://movie.douban.com/subject/6390825/photos?type=R&start=0&sortby=like&size=a&subtype=o"
    img_addrs = find_imgs(url)  
    print("共保存 %d 张图片"% len(img_addrs)) 
    save_imgs(folder,img_addrs) 

if __name__ == '__main__':  
    download_jpg()
```
可以使用`正则表达式`完成,用以下code 代替上面的注释code，不要忘记`import re`

```
p=r'<img src="([^"]+view[^"]+.jpg)"
img_list=re.findall(p,html)
```