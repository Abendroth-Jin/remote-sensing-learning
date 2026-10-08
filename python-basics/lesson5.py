#1.算数运算符（运算规则同数学运算规则）
# 1.1 +-*/
print(1+1)
print(1-2)
print(2*2)
print(1/1)  #使用算术运算符/，商一定是浮点数,且除数不能为零
# 1.2 // 取整除  取商的整数部分，向下取整
# 向下取整：不管四舍五入的规则，只要后面有小数，就忽略小数
a = 5
b = 2
print(a//b)
# 1.3 % 取余数  只取余数部分
print(a%b)
# 1.4 ** 幂  m**n:m的n次方
print(a**b)
print(7.0//2)  #使用算术运算符其中，若有浮点数，结果也会用浮点数表示
print(3**2+5/2)

#2.赋值运算符
# 2.1给变量赋值
num1 = 5
num2 = 8
# 将一个变量的值赋给另一个变量
num3 = num1
print(num3)
# 将运算的值赋给变量
total = num1 + num2
print(total)

# 2.2 +=
a = 1
print(a)
a += 1  #等效于 a = a + 1
print(a)

n1 = 99 #成本价
n2 = 66 #利润
n1 += n2 #等效于n1 = n1 + n2
print(n1)

# 2.3 -=
b = 1
print(b)
b -= 1  #等效于b = b - 1
print(b)
# 赋值运算符必须连着写，中间不能有空格，否则会报错
#n += 10  # n = n + 10,n没有被提前定义，所以不能参加加法运算
#print(n)
#print(10+=3)  #纯数字也不能使用，报错语法错误，因为赋值运算符是针对变量存在的

#3.输入函数input()
# input(prompt) prompt是提示，会在控制台中显示

#name = input("请输入姓名：") #在控制台中填写完后按回车键再运行即可输出
#print(name)
#pwd = input("请输入你的密码：")
#print(pwd)

#4.转义字符
# 4.1  \t 制表符   通常表示空四个字符，也称缩进
print('six\tstar')
print("姓名\t年龄\t电话")
# 4.2  \n 换行符 表示将当前位置移到下一行开头
print('haha\nxixi')
# 4.3  \r 回车  表示将当前位置移到本行开头
print("six\rrsdhd")
# 4.4  \\ 反斜杠符号
print('six\\star')
print(r'six\\star')  #r原生字符串，默认取消转义