# -*- coding: utf-8 -*-
"""
Created on Wed May 30 03:38:18 2018

@author: partha
"""

from ObjectiveFunction_Diss import ObjectiveFunction_Diss

print("Optimization Starts from Here: Wait for the Result**************")        
from pyswarm import pso
lb=[-3543.15, -3543.15, -3543.15,  -3543.15 ,-0.001, -0.001, -0.001, -0.001,  -0.001 ,-0.001, -0.001, -0.001]
ub=[-3543.00, -3543.00, -3543.00, -3543.00, 0, 0, 0, 0, 0, 0, 0, 0] 

#xopt, fopt = pso(objfunction, lb, ub) 
xopt, fopt=pso(ObjectiveFunction_Diss, lb, ub, ieqcons=[], f_ieqcons=None, args=(), kwargs={},
    swarmsize=30, omega=0.5, phip=0.5, phig=0.5, maxiter=300, minstep=1e-7,
    minfunc=1e-7, debug=False)