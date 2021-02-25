# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:04:20 2021

@author: wesva399
"""

from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
 
ranks = np.zeros(1)
total = np.zeros(1)

# Send to rank 0
ranks[0] = np.sum(rank)

comm.Reduce(total, ranks, op=MPI.SUM, root=0)

if rank == 0:
	print("Sum of ranks:", total.item())

