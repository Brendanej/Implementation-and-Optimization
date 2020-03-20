#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:34:40 2020

@author: safak
"""

#%%

import numpy as np
from random import seed
from random import randint
import seaborn as sns
import matplotlib.pyplot as plt


class Dice(object):
    def __init__(self,seedn):
        self.seed = seed(seedn)
                
    def Roll(self,n_sample,n_rolled):
        self.rolled_dices_sample = np.zeros((n_sample,n_rolled+1))
        self.seed
        for i in range(n_sample):
            for j in range(n_rolled):
                value=randint(1,6)
                self.rolled_dices_sample[i,j]=value
        return self.rolled_dices_sample

    def meanRoll(self,rolled_dice):
        sum_of = 0
        for i in range(rolled_dice.shape[0]):
            sum_of=0
            for j in range(rolled_dice.shape[1] - 1):
                sum_of = sum_of+rolled_dice[i,j]
                rolled_dice[i,rolled_dice.shape[1] - 1] = sum_of/(rolled_dice.shape[1] - 1)
        return rolled_dice        

   
if __name__ == "__main__":
    
   N_DATA = 10000
   N_ROLL = 10

   experiment = Dice(1)
   
   rolled_dice=experiment.Roll(N_DATA,N_ROLL)
   
   rolled_dice = experiment.meanRoll(rolled_dice)
   
   x = np.zeros(N_DATA)
   y= rolled_dice[:,N_ROLL]
   
   sns.distplot(y)
   plt.show()
    
