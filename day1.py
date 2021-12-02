"""
    Day 1: Sonar Sweep
"""

import numpy as np
class SonarSweep():
    
    
    
    with open("C:\\Users\\yunus\\OneDrive\\Masaüstü\\AdventofCode\\2021\\Day - 1\\input.txt", "r") as fp:
        num =  fp.readlines()
    num = [int(i.split("\n")[0]) for i in num]
    def partOne(self,x):
        increment = 0
        difference = np.diff(x)
        for i in difference:
            if i > 0:
                increment += 1
        return print("PartOne: ",increment)

    
    def partTwo(self,x):
        z = 0
        prev = 0
        for i in range(1,len(x)):
            if sum(x[i:i+3]) > prev:
                z += 1
            prev = sum(x[i:i+3])
        return print("PartSecond: ",z)
    

    partOne("",num)
    partTwo("", num)