# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 01:31:41 2018

@author: theresh
"""""



import numpy as np

def K_N(code_rate,N):
    if (N==64800):        
        if code_rate== np.divide(1,4.0):
            K=16008
            N=16200
        elif code_rate == np.divide(1,3.0):
            N=21600
            K=21408
        elif code_rate == np.divide(2,5.0):
            N=25920
            K=25728
        elif code_rate == np.divide(1,2.0):
            N=32400
            K=32208
        elif code_rate == np.divide(3,5.0):
            N=38880
            K=38688
        elif code_rate == np.divide(2,3.0):
            N=43200
            K=43040
        elif code_rate == np.divide(3,4.0):
            N=48600
            K=48408
        elif code_rate == np.divide(4,5.0):
            N=51840
            K=51648
        elif code_rate == np.divide(5,6.0):
            N=54000
            K=53840
        elif code_rate == np.divide(8,9.0):
            N=57600
            K=57472
        elif code_rate == np.divide(9,10.0):
            N=58320
            K=58192
    elif (N==16200):
        if code_rate== np.divide(1,4.0):
            N=3240
            K=3072
        elif code_rate == np.divide(1,3.0):
            N=5400
            K=5232
        elif code_rate == np.divide(2,5.0):
            N=6480
            K=6312
        elif code_rate == np.divide(1,2.0):
            N=7200
            K=7032
        elif code_rate == np.divide(3,5.0):
            N=9720
            K=9552
        elif code_rate == np.divide(2,3.0):
            N=10800
            K=10632
        elif code_rate == np.divide(3,4.0):
            N=11880
            K=11712
        elif code_rate == np.divide(4,5.0):
            N=12600
            K=12432
        elif code_rate == np.divide(5,6.0):
            N=13320
            K=13152
        elif code_rate == np.divide(8,9.0):
            N=14400
            K=14232
            
    return K,N
    