#字符串操作：获取长度
#字符串的本质是单个字符构成的序列
#==, >, <等操作符可用于字符串之间的比较
#len()函数可获取某个字符串（序列）的长度

#s = "abcde"
#print(len(s))  #返回字符串s的长度，即5

#索引
#可使用方括号[]对字符串进行索引，获取字符串中指定位置的字符0

#  s = "abc"
#   0  1  2  	正向索引
#   -3 -2 -1	反向索引

#s[0]  返回"a"
#s[1]  返回"b"
#s[2]  返回"c"
#s[3]  索引号超出边界，报错
#s[-1]  返回"c"
#s[-2]  返回"b"
#s[-3]  返回"a"

#分片
#可按[start:stop:step]的格式对字符串进行分片，其中：
#step可为空，默认值为1
#start和stop也都可为空，默认值需要视情况而定

#s = "abcdefgh"
#s[3:6]  返回"def"，等同于s[3:6:1]
#s[3:6:2]  返回"df"
#s[:3]  返回"abc"，等同于s[0:3]
#s[3:]  返回"defgh"，等同于s[3:len(s)]
#s[::]  返回"abcdefgh" ，等同于s[0:len(s):1]
#s[::-1]  返回"hgfedcba" ，等同于s[-1:-(len(s)+1):-1]
#s[4:1:-2]  返回"ec"

#字符的不可变性
#字符串一旦定义，就不能对其进行修改

#s = "hello"
#s[0] = 'y'			        程序报错
#s = 'y'+s[1:len(s)]		因字符串变量的绑定关系改变，可行

#字符串和for循环
#以下两端代码实现的功能完全相同
#右侧的实现方式更加pythonic

#较为生硬的实现方式
#s = "abcdefgh"
#for index in range(len(s)):
#    if s[index] == 'i' or s[index] == 'u':
#        print("There is an i or u")
# 更加pythonic的写法
#s = "abcdefgh"
#for char in s:
#    if char == 'i' or char == 'u':
#        print("There is an i or u")

#字符串操作的代码示例

#an_letters = "aefhilmnorsxAEFHILMNORSX"
#word = input("I will cheer for you! Enter a word: ") 
#times = int(input("Enthusiasm level (1-10): "))
#for char in word:
#    if char in an_letters:
#        print("Give me an " + char + "! " + char)
#    else:
#        print("Give me a "+char+"!"+char)
#print("What does that spell?")
#for i in range(times):
#    print(word, "!!!")

#穷举算法
#穷举法是一个猜测与检验(guess and check)的过程：
#1.给定需要求解的问题
#2.按一定的方式给出问题的猜想值
#3.检验猜想值是否为正确的解
#4.重复猜想与检验的过程。当猜想值为正确解，或已穷尽所有猜想值时，算法结束

#数列求和：
#sum = 0 
#for i in range(100):
#    sum += 1
#    print(int(sum*(sum+1)/2))

#用穷举法求取整数的立方根：
#cube = 8
#for guess in range(cube+1):
#    if guess**3 == cube:
#        print(str(cube)+'的整数立方根是'+str(guess))
#考虑负数的情形，以及不存在整数立方根的情形，对代码进行完善： 
#cube = int(input('请输入整数：'))
#for guess in range(abs(cube)+1):
#    if guess**3 >= abs(cube):
#        break
#if guess**3 != abs(cube):
#    print(cube, '没有整数立方根')
#else:
#    if cube < 0:
#        guess = -guess
#    print(str(cube)+'的整数立方根是'+str(guess))

#近似解
#通过近似的方式找到一个足够好的解
#在设定一个初始猜想值的基础上，以一定的增量单位逐步增加猜想值的大小
#持续猜想，直至猜想值达到设定的条件
#以求解立方根为例，可设定持续猜想的条件为：|guess3-cube| >= epsilon其中epsilon是一个很小的值，可称为收敛常数
#设定合理的增量单位和收敛常数是近似求解法的关键
#减小增量单位  程序变慢
#增大收敛常数epsilon  求解的精度更低

#代码示例：求取正数的立方根近似解
#cube = 27
#epsilon = 0.01
#guess = 0.0
#increment = 0.0001
#num_guesses = 0
#while abs(guess**3 - cube) >= epsilon and guess <= cube :
#    guess += increment
#    num_guesses += 1
#print('猜想次数为', num_guesses, '次')
#if abs(guess**3 - cube) >= epsilon:
#    print('未能成功求取', cube, '的立方根')
#else:
#    print(guess, '是', cube, '立方根的近似解')

#二分查找法
#二分查找法是一种比穷举法更有效率的查找方法：
#二分查找法的特点：
#每次迭代搜索空间均减半(穷举法一般搜索空间不变)
#新的猜想值取搜索范围的中间值

#代码示例：二分查找法求取立方根近似解
#cube = 27
#epsilon = 0.01
#num_guesses = 0
#low = 0
#high = cube
#guess = (high + low)/2.0
#while abs(guess**3 - cube) >= epsilon:
#    if guess**3 < cube :
#        low = guess
#    else:
#        high = guess
#    guess = (high + low)/2.0
#    num_guesses += 1
#print('猜想次数为', num_guesses, '次')
#print(guess, '是', cube, '立方根的近似解')

#二分查找法的收敛特性
#二分查找法的搜索空间随着迭代次数增加呈几何级数减小
#假设初始搜索空间为N
#第一次迭代后，搜索空间为N/2
#第二次迭代后，搜索空间为N/4
#第k次迭代后，搜索空间为N/2k
#因此，理论上在猜想次数达到log2N时，搜索空间为1，算法收敛
#但是：二分查找法只有在所求解对象为单调函数时才能起作用
