# -*- coding: utf-8 -*-
import datetime
import random

# 生成一个唯一的id标识
def Uid():
    nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S"); # 生成当前时间 
    randomNum=random.randint(1000,9999); 
    randomNums = random.randint(1000,9999);
    uniqueNum=str(nowTime)+str(randomNum)+str(randomNums);  

    return uniqueNum