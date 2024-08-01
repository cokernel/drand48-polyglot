# drand48 in Ruby and Python

This package includes partial translations of Martin Birgmeier's implementation of the
rand48 pseudorandom number generator from C into Ruby and Python.

Martin Birgmeier's code includes the following copyright notice and license:

```C
/*
 * Copyright (c) 1993 Martin Birgmeier
 * All rights reserved.
 *
 * You may redistribute unmodified or modified versions of this source
 * code provided that the above copyright notice and this and the
 * following conditions are retained.
 *
 * This software is provided ``as is'', and comes with no warranties
 * of any kind. I shall in no event be liable for anything that happens
 * to anyone/anything when using this software.
 */
```

## Usage

For my own use case, the behavior of `drand48` after seeding with small integers is
of particular importance, so a driver for each language is included that runs the
equivalent of

```C
for (int n = 0; n <= 1000000; ++n) {
    srand48(n);
    printf("%f\n", drand48());
}
```

You can run the included script `test.sh` to run the driver for each language and
compare outputs.

## Who built this

This translation was performed, and the test scripts were developed, by MLE Slone.
