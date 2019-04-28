# encoding=utf-8

from lettuce import *


# 用于计算整数的阶乘函数
def factorial(number):  # 被测试对象，告诉怎么计算阶乘的
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, number + 1))  # 算阶乘的方法，后续自己演练#一下


# 可以对比一下zero.feature里用例的三个关键字语句和下面的三个函数的映射关系，就是一#一对应的，一个语句对应一个函数，这就是行为驱动
# 下面的@是装饰器的用法，括号里是给装饰器穿的参数
@step('I have the number (\d+)')  # 跟feature里的Given所指的一样
def have_the_number(step, number):
    # 将通过正则表达式匹配的数字存于全局变量world中
    # world是lettuce里的命名空间，这命名空间里的所有变量在所有lettuce方法中共用，类似全局变量

    # 做了一个类型转换
    world.number = int(number)  # world是lettuce里的命名空间，这空间里的所有变量在所有lettuce里公用


@step('I compute its factorial')  # 同步features文件，然后用正则
def compute_its_factorial(step):
    # 从全局变量world中取出匹配的数字，
    # 计算其阶乘，并将结果再存回world中
    world.number = factorial(world.number)  # 把world.number传给函数，返回后又传给自己了


@step('I see the number (\d+)')
def check_number(step, expected):  # step对应I see the number ，expected对应分组(\d+)
    # 通过正则匹配到预期数字
    expected = int(expected)  # 把字符串转成整形
    # 断言计算阶乘结果是否等于预期
    assert world.number == expected, "Got %d" % world.number
