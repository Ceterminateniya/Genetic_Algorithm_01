import imp
import numpy as np
import geatpy as ea
import matplotlib.pyplot as plt
import time

def aim(Phen):
    x1=Phen[:,0]
    x2=Phen[:,1]
    x3=Phen[:,2]
    x4=Phen[:,3]
    x5=Phen[:,4]
    x6=Phen[:,5]
    return x1, x2, x3, x4, x5

x1=[1,2]
x2=[0.01,0.1]