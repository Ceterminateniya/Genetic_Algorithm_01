from re import M, X
import numpy as np
import geatpy as ea

#交互式遗传算法
#Problem：导入7种初始种群，每种种群为1个一维数组，每个数组为1个种群。

class my_problem(ea.Problem): # 继承父类Problem
    def __init__(self): # 初始化问题相关参数
        name = 'my_problem' # 初始化name（函数名称，可以随意设置）
        M = 1 # 初始化M（目标维数）
        # maxormin = 1 # 初始化maxormin（最小最大化标记，1：最小化目标；-1：最大化目标）
        Dim = 19 # 初始化Dim（决策变量维数）
        maxormins = [1] * M # 初始化maxormins（目标函数最小最大化标记，可以有多个目标函数）
        varTypes = [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #varTypes = [0]*Dim # 初始化varTypes（决策变量的类型，0：实数；1：整数）
        lb = [0.5,0.01,13,3,0,-30,8,-13,7,0,1,-16,-3,-30,0,2,-3,0,-1] # 初始化lb（决策变量下界）
        ub = [2.1,0.1,21,12,44.5,40,30,1,11,6,2,8,5,1,1,3,-2,4,3] # 初始化ub（决策变量上界）
        # lb=[0]*Dim
        # ub=[1]*Dim
        lbin = [1] * Dim # 初始化lbin（决策变量下边界类型，0：不包含下边界，1：包含下边界）
        ubin = [1] * Dim # 初始化ubin（决策变量上边界类型，0：不包含上边界，1：包含上边界）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop): # 目标函数
        Vars = pop.Phen # 得到决策变量矩阵
        aimMarix=[]
        for i in range(Vars.shape[1]): 
            aimMarix.append(Vars[:, [i]])
            
        f = (0.3*aimMarix[0]**2 + 0.2*aimMarix[1]**2 + 0.05*aimMarix[2] + 0.05*aimMarix[3] + 
            0.05*aimMarix[4] + 0.05*aimMarix[5]+0.01*aimMarix[6]+0.01*aimMarix[7]+0.01*aimMarix[8]+
            0.01*aimMarix[9]+0.01*aimMarix[10]+0.01*aimMarix[11]+0.01*aimMarix[12]+0.01*aimMarix[13]+
            0.01*aimMarix[14]+0.01*aimMarix[15]+0.01*aimMarix[16]+0.01*aimMarix[17]+0.01*aimMarix[18])
        pop.ObjV = f # 计算目标函数值，赋值给pop种群对象的ObjV属性
        f1=np.hstack([aimMarix[0]-2,aimMarix[1],
                      aimMarix[7]-aimMarix[10],aimMarix[8]-aimMarix[11],aimMarix[9]-aimMarix[12],
                      aimMarix[13]-aimMarix[16],aimMarix[14]-aimMarix[17],aimMarix[15]-aimMarix[18]])
        pop.CV= f1
        
        