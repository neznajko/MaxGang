#! /usr/bin/env python3
#  coding = utf-8
#[80]###########################################################################
import sys
#[72]###################################################################
#[64]###########################################################
#[56]###################################################
#[48]###########################################
import numpy as np
#[40]###################################
#[32]###########################
#[24]###################
#[56]###################################################
# ‡or reading Captain's data, run the program without
# options. To get maximum gang for a random generated
# data, run MaxGang.py n [d], vhere n is the number of
# outlaws, and d is the probability for a collaboration,
# e.g.: MaxGang.py 20 .65
#[40]###################################
def geropt():                          #
    argc = len(sys.argv)               #
    if argc == 1: return ()            # no arguments
    else:                              #
        n = int(sys.argv[1])           #
        if argc > 2:                   #
            d = float(sys.argv[2])     #
        else:                          #
            d = .5                     # dfólt probbltÿ
    return n, d                        #
#########################################[##]#### geropt
#[56]###################################################
def read_data():
    with open("Captain.dat") as f:
        dat = f.read().split()
    n = len(dat)
    a = np.zeros((n, n), dtype=int)
    for i, line in enumerate(dat):
        for j, char in enumerate(line):
            a[i, j] = int(char)
    return a
#######################[##]################### read_data
#[64]###########################################################
# input: n - nmbr of outlaws
#        d - probblity of collaboration
def rand_data(n, d):
    a = np.identity(n, dtype=int)
    for i in range(1, n):
        for j in range(0, i):
            a[i, j] = np.random.random() < d
    return a
##############################[##]#################### rand_data
#[72]###################################################################
# Gray Code Composition:         0 0 00 00 000 000 0000
#                                1 1 01 01 001 001 0001
# Here, Gray, Code, for, subsets,¯ 1 11 11 011 011 0011
# is, used, to, get, more, easily, 0 10 10 010 010 0010
# a, list, of, gang, candidates,     ¯¯ 10 110 110 0110
# (see, line, 98, at, maxgang),         11 111 111 0111
#                                       01 101 101 0101
#                                       00 100 100 0100
#                                          ¯¯¯ 100 1100
#[40]###################################       101 1101                
def GrayCode(n):                       #       111 1111
    if n == 0: return [0]              #       110 1110
    gc = GrayCode(n-1)                 #       010 1010
    f = 1 << (n-1)               # front       011 1011
    gc.extend([f|l for l in reversed(gc)]) #   001 1001
                                       #       000 1000
    return gc                          #           ¯¯¯¯
######[##]##################################################### GrayCode
#[80]###########################################################################
def dumpGC(gc):
    spec = '0{}b'.format(len(gc).bit_length() - 1)
    print(*map(lambda x: format(x, spec), gc), sep='\n')
#####################[##]################################################ dumpGC
#[56]###################################################
# Ok, so we have a list of indices and a low triangular
# array </a>, and we want to ck vhether a[i, j] are 1's
# for all {i, j: i > j} from </ls>.
#[24]################### 
def gangp(ls, a):      # predicate (lisp)
    ls.sort()          # 
    for k, j in enumerate(ls):
        for i in ls[k + 1:]: # discard j and below lmnts
            if a[i, j] == 0: return False
    return True        #       
#####################[##]######################### gangp
#[56]###################################################
#[32]###########################
def maxgang(a):                #
    n  = a.shape[0]            # number of outlaws
    gc = GrayCode(n)           # all subsets
    ls = []                    # candidates buffer
    maxlen = -1                # 
    maxls  = []                # 
    for j in range(1, len(gc)):#
        p, c = gc[j - 1:j + 1] # previous / current
        i = (p^c).bit_length() - 1 # diff lmnt pos
        if (c > p):            #
            ls.append(i)       #
        else:                  #
            ls.remove(i)       #
        if gangp(ls, a):       # collaboration ck
            l = len(ls)        #
            if l > maxlen:     #
                maxlen = l     #
                maxls = ls[:]  # copy
    return maxls               #
##############################[##]############## maxgang
#[64]###########################################################
if __name__ == '__main__':
    opt = geropt()
    if not opt:
        a = read_data()
    else:
        a = rand_data(*opt)
    print(sys.argv, *a, maxgang(a), sep='\n')
#################################[##]###################### log:
# cure: 
# next: 
