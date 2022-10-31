# -*- coding: utf-8 -*-
from code import interact
import geatpy as ea  # 导入geatpy库
import csv
import pandas as pd
import os
import bpy
import math as m
import cv2 as cv
import numpy as np
import time as wsleep

# import matplotlib
# import matplotlib.pyplot as plt

# path = 'F://First//University_03//Material//ZJDX//Program//Genetic_Algorithm_01//SGA_result.xlsx'
# data_01 = pd.ExcelFile(path)

# render_data = pd.read_excel(path)

def input_FitV():
    fit=input("please enter the score:")
    return float(fit)

def get_render_data(data):
        bpy.context.object.modifiers["GeometryNodes"]["Input_2"]=data.iloc[0]
        bpy.context.object.modifiers["GeometryNodes"]["Input_3"]=data.iloc[1]
        bpy.context.object.modifiers["GeometryNodes"]["Input_4"]=int(data.iloc[2])
        bpy.context.object.modifiers["GeometryNodes"]["Input_5"]=int(data.iloc[3])
        bpy.context.object.modifiers["GeometryNodes"]["Input_6"][1]=data.iloc[4]/180*m.pi
        bpy.context.object.modifiers["GeometryNodes"]["Input_7"][1]=data.iloc[5]/180*m.pi
        bpy.context.object.modifiers["GeometryNodes"]["Input_8"]=data.iloc[6]
        

        bpy.context.object.modifiers["GeometryNodes"]["Input_9"][0]=data.iloc[7]
        bpy.context.object.modifiers["GeometryNodes"]["Input_9"][1]=data.iloc[8]
        bpy.context.object.modifiers["GeometryNodes"]["Input_9"][2]=data.iloc[9]

        bpy.context.object.modifiers["GeometryNodes"]["Input_10"][0]=data.iloc[10]
        bpy.context.object.modifiers["GeometryNodes"]["Input_10"][1]=data.iloc[11]
        bpy.context.object.modifiers["GeometryNodes"]["Input_10"][2]=data.iloc[12]

        bpy.context.object.modifiers["GeometryNodes"]["Input_11"][0]=data.iloc[13]
        bpy.context.object.modifiers["GeometryNodes"]["Input_11"][1]=data.iloc[14]
        bpy.context.object.modifiers["GeometryNodes"]["Input_11"][2]=data.iloc[15]

        bpy.context.object.modifiers["GeometryNodes"]["Input_12"][0]=data.iloc[16]
        bpy.context.object.modifiers["GeometryNodes"]["Input_12"][1]=data.iloc[17]
        bpy.context.object.modifiers["GeometryNodes"]["Input_12"][2]=data.iloc[18]
        
# #render_Image(data_01)

class soea_SGA_templet(ea.SoeaAlgorithm):
    """
soea_SGA_templet : class - Simple GA Algorithm(最简单、最经典的遗传算法类)

算法描述:
    本算法类实现的是最经典的单目标遗传算法。算法流程如下：
    1) 根据编码规则初始化N个个体的种群。
    2) 若满足停止条件则停止，否则继续执行。
    3) 对当前种群进行统计分析，比如记录其最优个体、平均适应度等等。
    4) 独立地从当前种群中选取N个母体。
    5) 独立地对这N个母体进行交叉操作。
    6) 独立地对这N个交叉后的个体进行变异，得到下一代种群。
    7) 回到第2步。
    
"""

    def __init__(self,
                 problem,
                 population,
                 MAXGEN=None,
                 MAXTIME=None,
                 MAXEVALS=None,
                 MAXSIZE=None,
                 logTras=None,
                 verbose=None,
                 outFunc=None,
                 drawing=None,
                 trappedValue=None,
                 maxTrappedCount=None,
                 dirName=None,
                 **kwargs):
        # 先调用父类构造方法
        super().__init__(problem, population, MAXGEN, MAXTIME, MAXEVALS, MAXSIZE, logTras, verbose, outFunc, drawing, trappedValue, maxTrappedCount, dirName)
        if population.ChromNum != 1:
            raise RuntimeError('传入的种群对象必须是单染色体的种群类型。')
        self.name = 'SGA'
        self.selFunc = 'rws'  # 轮盘赌选择算子
        if population.Encoding == 'P':
            self.recOper = ea.Xovpmx(XOVR=0.7)  # 生成部分匹配交叉算子对象
            self.mutOper = ea.Mutinv(Pm=0.01)  # 生成逆转变异算子对象
        else:
            self.recOper = ea.Xovdp(XOVR=0.7)  # 生成两点交叉算子对象
            if population.Encoding == 'BG':
                self.mutOper = ea.Mutbin(Pm=None)  # 生成二进制变异算子对象，Pm设置为None时，具体数值取变异算子中Pm的默认值
            elif population.Encoding == 'RI':
                self.mutOper = ea.Mutbga(Pm=1 / self.problem.Dim, MutShrink=0.5, Gradient=20)  # 生成breeder GA变异算子对象
            else:
                raise RuntimeError('编码方式必须为''BG''、''RI''或''P''.')

    def run(self, prophetPop=None):  # prophetPop为先知种群（即包含先验知识的种群）
        #建表===========================================================
        writer=pd.ExcelWriter('SGA_result.xlsx',engine='openpyxl') #创建一个excel文件
        # ==========================初始化配置===========================
        population = self.population
        NIND = population.sizes
        self.initialization()  # 初始化算法类的一些动态参数
        # phen=ea.bs2ri(population.Chrom, population.Field)
        # data=pd.DataFrame(phen)
        
        # print(data)
        # wsleep.sleep(10)
        # ===========================准备进化============================
        #population.initChrom(NIND)  # 初始化种群染色体矩阵(乐色,不要用)
        # # 插入先验知识（注意：这里不会对先知种群prophetPop的合法性进行检查）
        # print(population.Chrom)
        wsleep.sleep(0.5)
        if prophetPop is not None:
            population = (prophetPop + population)[:NIND]  # 插入先知种群
        self.call_aimFunc(population)  # 计算种群的目标函数值
        population.FitnV = ea.scaling(population.ObjV, population.CV, self.problem.maxormins)  # 计算适应度
        #=====初代种群的评价=======
        #记录初代种群的图像
        # phen=ea.bs2ri(population.Chrom, population.Field)
        # data=pd.DataFrame(phen)
        # data=pd.DataFrame(population.Chrom)
        # print(data)
        # wsleep.sleep(10)
        # for j in range((data.shape[0])):#每一行的数据
        #     per_data_row=data.iloc[j]# 每一行的数据
        #     #print(per_data_row)
        #     get_render_data(per_data_row)
        #     bpy.data.scenes["Scene"].render.image_settings.file_format = 'PNG'
        #     bpy.data.scenes["Scene"].render.filepath = "F://First//University_03//Material//ZJDX//Program//Genetic_Algorithm_01//render_Image//test_per"+"G"+str(self.currentGen)+"_P"+str(j)+".png"    #set save filepath
        #     bpy.data.scenes["Scene"].render.film_transparent = True
        #     bpy.ops.render.render( write_still=True )    #render and save
        # wsleep.sleep(10)
        # 记录初代种群的评价结果
        
        # if self.problem.isGraph:
        #     self.out_file.write('\n%s\n' % (ea.summary(population.Chrom, population.ObjV, population.CV)))
        # else:
        #     self.out_file.write('\n%s\n' % (ea.summary(population.Chrom, population.ObjV)))
        # ===========================开始进化============================
        while not self.terminated(population):
            # 选择
            population = population[ea.selecting(self.selFunc, population.FitnV, NIND)]
            # 进行进化操作
            population.Chrom = self.recOper.do(population.Chrom)  # 重组
            population.Chrom = self.mutOper.do(population.Encoding, population.Chrom, population.Field)  # 变异
            self.call_aimFunc(population)  # 计算目标函数值
            ##!!!!!!!!
            #print(population.Chrom)
            #将每一代数据记录到文件中
            # file=os.getcwd()+'/'+str(self.currentGen)+'_'+'SGA_result.csv'
            # data=pd.DataFrame(population.Chrom)
            # data.to_csv(file,index=False) 
            data=pd.DataFrame(population.Chrom)
            interact_FitV=np.zeros((data.shape[0],1), dtype = float)
            i=0
            for j in range((data.shape[0])):#每一行的数据
                per_data_row=data.iloc[j]# 每一行的数据
                #print(per_data_row)
                get_render_data(per_data_row)
                bpy.data.scenes["Scene"].render.image_settings.file_format = 'PNG'
                bpy.data.scenes["Scene"].render.filepath = "F://First//University_03//Material//ZJDX//Program//Genetic_Algorithm_01//render_Image//test_per"+"G"+str(self.currentGen)+"_P"+str(j)+".png"    #set save filepath
                bpy.data.scenes["Scene"].render.film_transparent = True
                bpy.ops.render.render( write_still=True )    #render and save
                img_path = bpy.data.scenes["Scene"].render.filepath
                img = cv.imread(img_path)
                windname = "G"+str(self.currentGen)+"_P"+str(j)
                cv.namedWindow(windname,cv.WINDOW_NORMAL)
                cv.resizeWindow(windname,1280,720)
                cv.imshow(windname,img)
                cv.waitKey()
                wsleep.sleep(1)
                score=input_FitV()
                # score=0.5
                interact_FitV[i]=score
                i=i+1
                cv.destroyWindow(windname)
            
            # population.FitnV = ea.scaling(population.ObjV, population.CV, self.problem.maxormins)  # 计算适应度 
            # print(population.FitnV)
            #wsleep.sleep(20)
            population.FitnV = interact_FitV # 计算适应度    
            print(population.FitnV)
            data.to_excel(writer,sheet_name=str(self.currentGen),index=False,header=False)
        writer.save() #保存文件
        return self.finishing(population)  # 调用finishing完成后续工作并返回结果
