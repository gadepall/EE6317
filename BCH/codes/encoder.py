# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:34:10 2019

@author: theresh
"""

import numpy as np
from gf2_div import gf2_div


def Encoder(x,g,k,n):
    #x=message	
    #c=codeword
    #g=generator polynomial
    #k=3078   # M E S S A G E  L E N G T H
    #n=3240   # C O D E W O R D  l E N G T H
    m=np.concatenate((x,np.zeros(n-k,dtype=int)))
    q,r=gf2_div(m,g)
    if (len(r)!=len(g)-1):
        r=np.concatenate((np.zeros(len(g)-1-len(r),dtype=int),r))
    c=np.concatenate((x,r))
    return c
