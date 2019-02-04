# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:46:41 2019

@author: theresh
"""

import numpy as np
from generator_polynomial import gen_poly
import kbch_nbch_selection
from alpha_tables import alpha_lookup_tables
from index import index

def syndromes(code_rate,N,dxcm):
    g,Gg=gen_poly(N)
    kbch,nbch=kbch_nbch_selection.K_N(code_rate,N)
    m1,m=Gg.shape
    m=m-1
    t=12
    n_bch=nbch #(2**(m))-1
    alpha=alpha_lookup_tables(code_rate,N)
    S=np.zeros((2*t,m),dtype=int)
    s=np.zeros(2*t,dtype=int)
    for i in range(2*t):
        for j in range(nbch):
            if dxcm[j]==0:
                S[i,:]=S[i,:]
            else:
                S[i,:]=np.mod((S[i,:]+alpha[(i*j-i)% n_bch,:]),2)
        s[i]=index(S[i,:],code_rate,N)
    return S,s
        
    
    
    
  
    
    
    
    

