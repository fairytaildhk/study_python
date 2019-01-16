import re

'''
正则表达式学习
全局匹配函数使用格式	re.compile(正则表达式).findall(源字符串)

普通字符	正常匹配
\n			匹配换行符  
\t 			匹配制表符
\w 			匹配字母、数字、下划线
\W 			匹配除字母、数字、下划线
\d 			匹配十进制数字
\D 			匹配除十进制数字
\s 			匹配空白字符
\S 			匹配除空白字符
[ab89x]		原子表，匹配ab89x中的任意一个
[^ab89x]		原子表，匹配除ab89x以外的任意一个字符
'''


def test1():
    a = re.compile('yu').findall('aliyun')
    print(a)


def test2():
    str = 'aliyun\nsss'
    pat = 'yun\n'
    print(re.compile(pat).findall(str))


def test3():
    str = 'aliyu89787nedu'
    pat = '\w\d\w\d\d\w'
    print(re.compile(pat).findall(str))


def test4():
    str = 'study12345python'
    pat = '\w\d[python]\w'
    print(re.compile(pat).findall(str))


'''
.	匹配除换行外任意一个字符
^	匹配开始位置
$	匹配结束位置
*	前一个字符出现0\1\多次 
?	前一个字符出现0\1次
+	前一个字符出现1\多次
{n}	前一个字符恰好出现n次
{n,}	前一个字符至少n次
{n,m}前一个字符至少n，至多m次 
|	模式选择符或
()	模式单元，通俗来说就是：想提取出什么内容，就在正则中用小括号将其括起来

'''


if __name__ == '__main__':
    print('hello python')
    test1()
    test2()
    test3()
    test4()
