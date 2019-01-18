##### 正则表达式：

```python
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242
```
如上所示，整个过程，一共涉及到2个对象。正则对象以及Match对象
`group()`方法，可以选择性的显示group1，group2
```python
>>> phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
>>> mo.group(1)
'(415)'
>>> mo.group(2)
'555-4242'
```
使用`|`匹配多个字符串对象，返回最先匹配到的那个。
```python
>>> heroRegex = re.compile (r'Batman|Tina Fey')
>>> mo1 = heroRegex.search('Batman and Tina Fey.')
>>> mo1.group()
'Batman'
```
分组与`|`配合使用的好处可以将前缀拿出来，节约劳动力
```python
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
```
`?` 表示可以有一个，也可以表示无
```python
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
```

`search()`方法返回符合正则表达的首个字符串的Match对象，
`findall()`是正则对象的方法，以列表的形式返回符合正则表达式的全部字符串，如果有group，则返回的列表单元是tuple

The `?` matches zero or one of the preceding group.

The `* `matches zero or more of the preceding group.

The `+ `matches one or more of the preceding group.

The `{n} `matches exactly n of the preceding group.

The `{n,} `matches n or more of the preceding group.

The `{,m} `matches 0 to m of the preceding group.

The` {n,m}` matches at least n and at most m of the preceding group.

`{n,m}?` or` *? or`+?` performs a nongreedy match of the preceding group.

`^spam` means the string must begin with spam.

`spam$ `means the string must end with spam.

The` . `matches any character, except newline characters.

`\d`, `\w`, and `\s` match a digit, word, or space character, respectively.

`\D`, `\W`, and `\S` match anything except a digit, word, or space character, respectively.

`[abc] `matches any character between the brackets (such as a, b, or c).

`[^abc] `matches any character that isn’t between the brackets.
```python
>>> robocop = re.compile(r'robocop', re.I)             # 不考虑大小写

>>> namesRegex = re.compile(r'Agent \w+')
   # 用第一个参数替代匹配的字符串。sub()返回字符串。
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

>>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> import re                                # re.sub()在替换方面比str.replace()强大
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2012-11-27. PyCon starts 2013-3-13.'
```