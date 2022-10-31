from re import M, X
import numpy as np
import geatpy as ea

#交互式遗传算法
#Problem：导入10种初始种群，每种种群为1个一维数组，每个数组为1个种群。

class my_problem(ea.Problem): # 继承父类Problem
    def __init__(self): # 初始化问题相关参数
        name = 'my_problem' # 初始化name（函数名称，可以随意设置）
        M = 1 # 初始化M（目标维数）
        # maxormin = 1 # 初始化maxormin（最小最大化标记，1：最小化目标；-1：最大化目标）
        Dim = 19 # 初始化Dim（决策变量维数）
        maxormins = [1] * M # 初始化maxormins（目标函数最小最大化标记，可以有多个目标函数）
        varTypes = [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #varTypes = [0]*Dim # 初始化varTypes（决策变量的类型，0：实数；1：整数）
        lb = [0.5,
              0.01,
              5,
              3,
              0,
              -30,
              5,
              -13,
              0,
              -1,
              0,
              -40,
              -3,
              -30,
              0,
              0,
              -3,
              0,
              -1] # 初始化lb（决策变量下界）
        ub = [7.0,
              0.8,
              21,
              15,
              60,
              40,
              30,
              3,
              15,
              6,
              2,
              8,
              5,
              1,
              3,
              4,
              2,
              4,
              3] # 初始化ub（决策变量上界）
        # lb=[0]*Dim
        # ub=[1]*Dim
        lbin = [1] * Dim # 初始化lbin（决策变量下边界类型，0：不包含下边界，1：包含下边界）
        ubin = [1] * Dim # 初始化ubin（决策变量上边界类型，0：不包含上边界，1：包含上边界）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def calf(coff,aimMatrix):
        f=np.zeros((aimMatrix.shape[0],1), dtype=np.float)
        for i in range(aimMatrix.shape[1]):
            f=f+coff[i]*aimMatrix[:,[i]]
        return f

    def aimFunc(self, pop): # 目标函数
        Vars = pop.Phen # 得到决策变量矩阵
        aimMatrix=np.array(Vars)
        for i in range(aimMatrix.shape[1]):
            aimMatrix[:, [i]] = 1.0 / (1 + np.exp(-(aimMatrix[:, [i]])))  # 第0列均值方差归一化
            
        coff=np.array([8,5,4,4,5,5,2,3,4,5,3,4,3,2,3,2,5,4,3])
        f = np.sin(my_problem.calf(coff,aimMatrix))
        pop.ObjV = f # 计算目标函数值，赋值给pop种群对象的ObjV属性