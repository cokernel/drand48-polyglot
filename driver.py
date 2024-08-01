#!/usr/bin/env python

from drand48 import drand48, srand48

for n in range(1000001):
    srand48(n)
    print(drand48())
