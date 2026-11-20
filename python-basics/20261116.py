#应用于bool型的逻辑操作符

#money_earned = 0
#money_spent = 3000
#if money_earned < money_spent:
#    print("赚钱了")

#gate_key = True
#door_key = False
#enter_room = gate_key and door_key
#print(enter_room)

#字符串对象(string类型)

#hi = "Hello"
#name = "Alice"
#greeting = hi + ", " + name + "!"
#print(greeting)
#biggreeting = hi + ", " + name*3
#print(biggreeting)

#输入与输出：print;print函数将内容输出到控制台(屏幕)

#age = 18
#print("I am " + str(age) + " years old!")

#输入与输出：input("");input函数可以直接接受用户输入

#text = input("Type something: ")
#print(5*text)

#程序分支和Python代码的缩进

#x = float(input("Enter a number for x: "))
#y = float(input("Enter a number for y: "))
#if x == y:
#    print("x and y are equal")
#    if y != 0:
#        print("therefore, x / y is", x/y)
#elif x < y:
#    print("x is smaller")
#else:
#    print("y is smaller")

#while语句以保留字while为标志
#条件返回True或False
#如果条件返回True，执行while循环内部代码块中的表达式
#代码块执行完毕后，重新对条件进行检验
#重复执行while循环内的代码块，直至条件返回False

#while循环示例
#year = input("Which year was China University of Geosciences founded?\n")
#while (year != '1952'):
#    year = input("You guessed wrong! Have another try!\n")
#print('Congratulations! You guessed right!')

#for语句
#相比while循环，for循环提供了一种语言机制更加简化的迭代方式

#例如：使用循环的方式依此输出1, 2, 3, 4, 5
#while循环方式：
#n=0
#while n < 5:
#    n = n+1
#    print(n)
#for循环方式：
#for n in range(5):     #range(5) generates a sequence of numbers from 0 to 4
#    print(n+1)

#range()函数的一般形式：range(start, stop, step)
#可设置3个参数，其中：
#start和step为可选参数，表示起始值和步距，默认值为start=0和step=1
#stop表示序列终点，序列的最后一个取值为stop-1

#mysum = 0
#for i in range(7, 10):
#    mysum += i    #+= is a shorthand for mysum = mysum + i
#print(mysum)

#mysum = 0
#for i in range(5, 11, 2):   #5, 7, 9
#    mysum += i
#print(mysum)

#break语句
#break的功能：立即退出当前所在循环
#break的特征：
#当循环程序执行过程中遇到break时，跳过当前代码块的所有剩余表达式
#在执行嵌套循环时，只退出当前所在的循环

#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1   #break语句后面的代码不会被执行
#print(mysum)   #print(mysum)输出结果为5

#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 11:    #if语句没有被触发
#        break
#        mysum += 1
#print(mysum)    #print(mysum)输出结果为21
