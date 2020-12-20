import numpy as np
import random
import math
import sys

"""A taskset generator for experiments with real-time task sets

Copyright 2010 Paul Emberson, Roger Stafford, Robert Davis. 
All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, 
      this list of conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation 
      and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY EXPRESS 
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO 
EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT 
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE 
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are 
those of the authors and should not be interpreted as representing official 
policies, either expressed or implied, of Paul Emberson, Roger Stafford or 
Robert Davis.

Includes Python implementation of Roger Stafford's randfixedsum implementation
http://www.mathworks.com/matlabcentral/fileexchange/9700
Adapted specifically for the purpose of taskset generation with fixed
total utilisation value

Please contact paule@rapitasystems.com or robdavis@cs.york.ac.uk if you have 
any questions regarding this software.
"""


def stafford_utilizations (n=12, u=2.1, nsets=1, a=0.05, b=0.6):
    # This function is adapted from here:
    # https://gitlab.retis.santannapisa.it/t.cucinotta/rtsim/blob/3e8a1f9b3bb9914dd971fe7bbbc626e76b5651a3/src/taskset_generator/taskgen.py#L48
    # The adaption introduces the possibility to generate values in range [a, b], subject to n*a <= u <= n*b.
    # Check stafford.m file in this folder.

    # deal with n=1 case
    if n == 1:
        return np.tile(np.array([u]),[nsets,1])
    u = (u-n*a)/(b-a)
    k = np.floor(u)
    s = u
    step = 1 if k < (k-n+1) else -1
    s1 = s - np.arange( k, (k-n+1)+step, step )
    step = 1 if (k+n) < (k-n+1) else -1
    s2 = np.arange( (k+n), (k+1)+step, step ) - s

    tiny = np.finfo(float).tiny
    huge = np.finfo(float).max

    w = np.zeros((n, n+1))
    w[0,1] = huge
    t = np.zeros((n-1,n))

    for i in np.arange(2, (n+1)):
        tmp1 = w[i-2, np.arange(1,(i+1))] * s1[np.arange(0,i)]/float(i)
        tmp2 = w[i-2, np.arange(0,i)] * s2[np.arange((n-i),n)]/float(i)
        w[i-1, np.arange(1,(i+1))] = tmp1 + tmp2;
        tmp3 = w[i-1, np.arange(1,(i+1))] + tiny;
        tmp4 = np.array( (s2[np.arange((n-i),n)] > s1[np.arange(0,i)]) )
        t[i-2, np.arange(0,i)] = (tmp2 / tmp3) * tmp4 + (1 - tmp1/tmp3) * (np.logical_not(tmp4))

    m = nsets
    x = np.zeros((n,m))
    rt = np.random.uniform(size=(n-1,m)) #rand simplex type
    rs = np.random.uniform(size=(n-1,m)) #rand position in simplex
    s = np.repeat(s, m);
    j = np.repeat(int(k+1), m);
    sm = np.repeat(0, m);
    pr = np.repeat(1, m);

    for i in np.arange(n-1,0,-1): #iterate through dimensions
        e = ( rt[(n-i)-1,...] <= t[i-1,j-1] ) #decide which direction to move in this dimension (1 or 0)
        sx = rs[(n-i)-1,...] ** (1/float(i)) #next simplex coord
        sm = sm + (1-sx) * pr * s/float(i+1)
        pr = sx * pr
        x[(n-i)-1,...] = sm + pr * e
        s = s - e
        j = j - e #change transition table column if required

    x[n-1,...] = sm + pr * s
    
    #iterated in fixed dimension order but needs to be randomised
    #permute x row order within each column
    for i in range(0,m):
        x[...,i] = (b-a) * x[np.random.permutation(n),i] + a

    return np.transpose(x)