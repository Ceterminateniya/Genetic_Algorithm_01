from lib2to3.pgen2 import grammar
from logging import error
import random
from secrets import choice
from statistics import variance
from tkinter import E


def get_data():
    number_set = []
    for i in range(10):
        number_set.append(i)
    return number_set

def create_answer(number_set,n): #随机选择n个数字作为答案，并返回答案(生成种群)
    result = []
    for i in range(n):
        result.append(random.sample(number_set,10))
    return result 


def error_level(new_answer,number_set):#计算答案的误差,误差越小遗传概率越大(轮盘选择？)
    error =[]
    right_answer =sum(number_set)/10
    for item in new_answer:
        value=abs(right_answer-sum(item))
        if value==0:
            error.append(10)
        else:
            error.append(1/value)
    return error

def choice_selected(old_answer,number_set):#交叉互换模拟交配生殖的结果(交叉)
    result = [] #存放交配后的结果
    error=error_level(old_answer,number_set)#计算误差
    error_one=[item/sum(error) for item in error]#归一化
    for i in range(1,len(error_one)):
        error_one[i]+=error_one[i-1]#叠加化
    for i in range(len(old_answer)//2):#随机选择两个父代
        temp=[]#临时种群
        for j in range(2):#随机选择两个父代
            rand=random.uniform(0,1)#随机数
            for k in range(len(error_one)):#寻找随机数在哪个区间
                if k==0:#第一个区间
                    if rand<error_one[k]:#随机数在第一个区间
                        temp.append(old_answer[k])#添加父代
                else:#其他区间
                    if rand>=error_one[k-1] and rand<error_one[k]:#随机数在其他区间
                        temp.append(old_answer[k])#添加父代
    #交叉操作
    #解集为10个数字，随机生成起点下标为0-6，随机切出一段长度为3的部分进行交换
        random_start=random.randint(0,6)  #随机生成起点
        temp_1=temp[0][:random_start]+temp[1][random_start:random_start+3]+temp[0][random_start+3:]#交换
        temp_2=temp[1][:random_start]+temp[0][random_start:random_start+3]+temp[1][random_start+3:]
        result.append(temp_1)
        result.append(temp_2)
    return result

def variantion(old_answer,number_set,pro):#变异操作(变异),随机选择一个种群,随机选择一个数字,随机选择一个数字进行交换
        for i in range(len(old_answer)):#随机选择一个种群
            if random.uniform(0,1)<pro:
                rand_index=random.randint(0,9)#随机生成下标
                old_answer[i]=old_answer[i][:rand_index]+random.sample(number_set,1)+old_answer[i][rand_index+1:]#交换
        return old_answer

number_set=random.sample(range(0,1000),50) # create a set of numbers
middle_answer = create_answer(number_set,100) #随机生成100个答案
greater_answer =[]  #存放每次迭代的最优种群
first_answer = middle_answer[0] #存放第一次迭代的最优种群
for i in range(1000):
    middle_answer=choice_selected(middle_answer,number_set)#交叉
    middle_answer=variantion(middle_answer,number_set,0.1)#变异
    error=error_level(middle_answer,number_set)#计算误差,误差越小遗传概率越大(适应度)
    index=error.index(max(error))#找到最小误差的种群,即最优解,因为取的是倒数，所以取最大值max(error)
    greater_answer.append([middle_answer[index],error[index]])#添加最优解
    
    # new_answer = create_answer(number_set,1)
    # error_level = error_level(new_answer,number_set)
    # if error_level<error_level(middle_answer,number_set):
    #     middle_answer = new_answer
    # else:
    #     pass

greater_answer.sort(key=lambda x:x[1],reverse=True)#按照误差排序,误差越小排序越靠前
print("正确答案为",sum(number_set)/10)
print("给出最优解",greater_answer[0][0])#输出最优解
print("和为",sum(greater_answer[0][0]))#输出最优解的和
print("误差为",greater_answer[0][1])#输出最优解的误差(选择系数)
print("最初解为",first_answer)#输出最初解
print("最初和为",sum(first_answer))#输出最初解的和
# print("最初误差为",error_level(first_answer,number_set))#输出最初解的误差(选择系数)


