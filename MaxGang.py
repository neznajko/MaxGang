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
#[72]###################################################################
# Gray Code Composition: probbly another algorithm has to be used but
# this one has simple logic: if we have the n-bit codes, than the n + 1
# codes are obtained as a composition of two list, first one is a copy
# of the n-codes with a front inserted zero, second one is a reflection
# with an 1 inserted at the front. For example the 1-bit code is 0 and
# 1, so to get the 2-bit code we do the following:
# 0 -----> 0 -----> 00 All subsets of n-element set can be obtained by
# 1 copy   1 add 0  01 starting from 0 and adding 1 until 2^n - 1, but
# 0 -----> 1 -----> 11 Gray Codes consecutive numbers differ in a bit
# 1 reflex 0 add 1  10 only so we can get the diff by an exclusive or.
#[40]###################################
def GrayCode(n):                       #
    if n == 0: return [0]              #
    gc = GrayCode(n-1)                 #                               
    f = 1 << (n-1)                     # front
    gc.extend([f|l for l in reversed(gc)])
                                       #
    return gc                          #
######[##]##################################################### GrayCode
#[80]###########################################################################
def dumpGC(gc):
    spec = '0{}b'.format(len(gc).bit_length() - 1)
    print(*map(lambda x: format(x, spec), gc), sep='\n')
#####################[##]################################################ dumpGC
#[56]###################################################
#[32]###########################
def maxgang(a):                #
    n  = a.shape[0]            # number of outlaws
    gc = GrayCode(n)           # all subsets
    ls = []                    # candidates buffer
    maxlen = -1                # yeah!
    maxls  = []                # result
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
# input: n - nmbr of outlaws
#        d - probblity of collaboration
def rand_data(n, d):
    a = np.identity(n, dtype=int)
    for i in range(1, n):
        for j in range(0, i):
            a[i, j] = np.random.random() < d
    return a
##############################[##]#################### rand_data
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
#[56]###################################################
# For reading Captain's data, run the program without
# options. To get maximum gang for a random generated
# data, run ./MaxGang.py n [d], vhere </n> is the number
# of outlaws, and </d> is the probability for a
# collaboration, e.g.: ./MaxGang.py 20 .65
#[32]###########################
def geropt():                  #
    argv = sys.argv[1:]        #
    if len(argv) == 1:         #
        argv.append(".5")      # default </d>
    return argv                #
#########################################[##]#### geropt
#[64]###########################################################
if __name__ == '__main__':
    argv = geropt()
    if not argv:
        a = read_data()
    else:
        n, d = int(argv[0]), float(argv[1])
        a = rand_data(n, d)
    print(sys.argv, *a, maxgang(a), sep='\n')
#################################[##]###################### log:
# cure: 
# next: 
