# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:50:32 2021

@author: wesva399
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(f'Hello World from process {rank}')
