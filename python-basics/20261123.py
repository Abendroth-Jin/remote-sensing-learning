#空格和逗号，分别在哪里
print("Python AI")
print("Python", "AI")
print("Python","AI")
print("Python,AI")
#前三行结果相同，但空格来源不同；代码行首的缩进另有作用。

#用sep控制输出项之间的分隔
print("2026", "09", "01", sep="-")
print("Python", "AI", sep="")    #一个空格（默认）
print("Python ", "AI", sep=" ")    #两个空格  #字符串自带的空格不会被sep删除。

#用end控制本次输出的结尾
print("课程：", end="")
print("Python", "入门", sep="·", end=" ")
print("开始")
print("下一行")
#默认end是换行。四次调用，只显示两行。

#输出算式，还是输出计算结果
print("报名总人数：", "18 + 7")    #文本原样输出
print("报名总人数：", 18 + 7)    #表达式先求值

#按要求得到一行精确输出
#目标：姓名:林宁,组别:A——半角标点、不含空格、行末换行。
print("姓名:林宁", "组别:A", sep=",")
print("姓名:林宁,组别:A")
#两种写法都可满足目标；检查输出时要同时看字符、空格和换行。

#显示相同，不等于类型相同
print(12)
print("12")
print(type(12))
print(type("12"))

#位与字节：用二进制表示75
#8位 = 1字节。把值为1的位置所对应的权值相加。
#二进制01001011  对应后即75 = 64 + 8 + 2 + 1

#负数整除，不是直接删小数
print(-7 / 2)    #-3.5
print(-7 // 2)   #-4
print(-7 % 2)    #1
print((-7 // 2) * 2 + (-7 % 2))    #-7
#/、//、%的除数不能为0。否则触发ZeroDivisionError

#乘方的两处特殊组合规则
print(2 + 3 * 4)    #14
print((2 + 3) * 4)   #20
print(2 * 3 ** 2)   #18
print(20 / 5 * 2)   #8.0
print(2**3**2)    #512
print((2**3)**2)    #64
print(2**(3**2))    #512
print(-3**2)    #-9
print((-3)**2)    #9

#int与round，采用不同规则
print(int(3.8))    #3
print(int(-3.8))   #-3
#向零截断，舍去小数部分
print(round(3.8))    #4
print(round(-3.8))   #-4
#取最接近的整数
print(round(2.5))    #2
print(round(3.5))    #4
#恰好居中时，选择偶数

#名称要合法，也要说明用途
#蛇形命名：temperature_total、unit_price、total_length_m
#1.只能由字母、数字、下划线组成  sample_2、unit_price
#2.首字符必须是字母或下划线  sample、_count
#3.不能使用Python关键字  class_count、for_count

#半径变了，面积会自动更新吗
pi = 3.14159
radius = 2.0
area = pi * radius ** 2
print(radius, area)
radius = radius + 1
print(radius, area)
area = pi * radius ** 2
print(radius, area)
#第一次求面积：使用当时的radius = 2.0
#只更新半径：area仍保存原来的结果
#再次求面积：使用新半径，更新area
