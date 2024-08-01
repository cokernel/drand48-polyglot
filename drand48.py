#!/usr/bin/env python

import math

# This file includes a partial translation of Martin Birgmeier's implementation of the
# rand48 pseudorandom number generator from C into Python.
#
# /*
#  * Copyright (c) 1993 Martin Birgmeier
#  * All rights reserved.
#  *
#  * You may redistribute unmodified or modified versions of this source
#  * code provided that the above copyright notice and this and the
#  * following conditions are retained.
#  *
#  * This software is provided ``as is'', and comes with no warranties
#  * of any kind. I shall in no event be liable for anything that happens
#  * to anyone/anything when using this software.
#  */
#

RAND48_SEED_0 = 0x330e
RAND48_SEED_1 = 0xabcd
RAND48_SEED_2 = 0x1234
RAND48_MULT_0 = 0xe66d
RAND48_MULT_1 = 0xdeec
RAND48_MULT_2 = 0x0005
RAND48_ADD    = 0x000b

_rand48_seed = [
    RAND48_SEED_0,
    RAND48_SEED_1,
    RAND48_SEED_2,
]

_rand48_mult = [
    RAND48_MULT_0,
    RAND48_MULT_1,
    RAND48_MULT_2,
]

_rand48_add = RAND48_ADD

# unsigned short xseed[3]
def _dorand48(xseed):
    temp = [0, 0]

    accu = _rand48_mult[0] * xseed[0] + _rand48_add
    temp[0] = accu & 0xffff # lower 16 bits
    accu >>= 16
    accu += _rand48_mult[0] * xseed[1] + _rand48_mult[1] * xseed[0]
    temp[1] = accu & 0xffff # middle 16 bits
    accu >>= 16
    accu += _rand48_mult[0] * xseed[2] + _rand48_mult[1] * xseed[1] + _rand48_mult[2] * xseed[0]
    xseed[0] = temp[0]
    xseed[1] = temp[1]
    xseed[2] = accu & 0xffff

# long int seed
def srand48(seed):
    _rand48_seed[0] = RAND48_SEED_0
    _rand48_seed[1] = seed & 0xffff
    _rand48_seed[2] = (seed >> 16) & 0xffff
    _rand48_mult[0] = RAND48_MULT_0
    _rand48_mult[1] = RAND48_MULT_1
    _rand48_mult[2] = RAND48_MULT_2
    _rand48_add = RAND48_ADD

# unsigned short xseed[3]
def erand48(xseed):
    _dorand48(xseed)
    return(math.ldexp(float(xseed[0]), -48)
           + math.ldexp(float(xseed[1]), -32)
           + math.ldexp(float(xseed[2]), -16))

def drand48():
    return erand48(_rand48_seed)

def lrand48():
    _dorand48(_rand48_seed)
    return (_rand48_seed[2] << 15) + (_rand48_seed[1] >> 1)
