import random as rd
import numpy as np
import geatpy as ea
from numpy import loadtxt
from myProblem import my_problem # 导入自定义问题类
import pandas as pd

path = '.\\data.xlsx'
data = pd.read_excel(path)
#a=loadtxt('data.txt',delimiter=' ')

problem=my_problem() # 实例化问题对象

Encoding='RI'# 编码方式
NIND=7 # 种群规模
Field=ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) # 创建区域描述器
population=ea.Population(Encoding, Field, NIND,data) # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）

myAlgorithm=ea.soea_SGA_templet(problem, population) # 实例化一个算法模板对象
myAlgorithm.MAXGEN=4 # 最大进化代数
myAlgorithm.drawing=1 # 设置绘图方式（0：不绘图；1：绘图）
myAlgorithm.verbose=True # 设置是否打印遗传算法的内部信息
myAlgorithm.run() # 执行算法模板，得到帕累托最优解集NDSet
# NDSet=myAlgorithm.NDSet # 获得最优种群

[BestIndi, population] = myAlgorithm.run()#执行算法模板，得到最优个体以及最后一代种群
BestIndi.save()#把最优个体的信息保存到文件中


# print('评价次数：%d'%(myAlgorithm.evalsNum))
# print('时间已过：%f'%(myAlgorithm.passTime))
# if BestIndi.sizes != 0:
#     print('最优的目标函数值为：%s'% BestIndi.ObjV[0][0])
#     print('最优的控制变量值为：')
#     for i in range(BestIndi.Phen.shape[1]):
#         print(BestIndi.Phen[0, i])
#     else:
#         print('没找到可行解。')