# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:38:01 2019

@author: theresh
"""

import numpy as np
from generator_polynomial import gen_poly
import kbch_nbch_selection

#code_rate=np.divide(1,4.0)
#N=16200

def alpha_lookup_tables(code_rate,N):
    g,Gg=gen_poly(N)
    kbch,nbch=kbch_nbch_selection.K_N(code_rate,N)
    m1,m=Gg.shape
    m=m-1
    n_bch=nbch  #(2**(m))-1
    alpha=np.zeros((n_bch,m),dtype=int)
    alpha[1:m+1,:]=np.identity(m)
    for i in range(m+1,n_bch):
        alpha[i,:]=np.mod((alpha[i-m,:]+alpha[i-m+1,:]),2) 
    return alpha
    
#alpha=alpha_lookup_tables(code_rate,N)
#    
#kbch,nbch=kbch_nbch_selection.K_N(code_rate,N)  
#g,Gg=gen_poly(N)  
    
    
    
    
    
    
    
    
    
    
    
    
    
#mm=14
#alpha=np.zeros((nbch,mm),dtype=int)
#alpha[1:mm+1,:]=np.identity(mm)
#for i in range(mm+1,nbch):
#    alpha[i,:]=(alpha[i-mm,:]+alpha[i-mm+1,:])%2    