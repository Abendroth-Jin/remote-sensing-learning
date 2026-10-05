#1.数值类型
# 1.1  int整型（常用）：任意大小的整数
num = 1000
# 检测数据类型的方法 type（）
print(type(num))
# 1.2  float浮点数：小数
num2 = 1.5
print(type(num2))
# 1.3  bool布尔型（重点）：有固定写法，一个为True，一个为False
#   注意：True和False严格区分大小写
print(type(True))
print(type(False))
#  布尔值可以当作整型对待，True相当于整数1，False相当于整数0
print(True+False)  #1+0=1
print(True+1)  #1+1=2
# 1.4  complex复数型（了解）
#   固定写法： Z = a + bj  --a是实部，b是虚部，j是虚数单位,虚数单位只能是j，不可随意改变
print(type(2+3j))
ma = 1 + 2j
ma2 = 2 + 3j
print(ma+ma2)