# -*- coding: utf-8 -*-
"""**Another Infinity Pi Calculate:**"""

import sys


def calcPi():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr


pi_digits = calcPi()
i = 0
j = 0
ij = 0
file_num = 0
for d in pi_digits:
    sys.stdout.write(str(d))
    i += 1
    j += 1
    ij += 1
    file = open("/pi/{}.txt".format(file_num), "a+")
    file.write(str(d))
    file.close()
    if ij == 10:
        file = open("/pi/{}.txt".format(file_num), "a+")
        file.write(" ")
        file.close()
        ij = 0
    if i == 50:  # Write new line
        print("")
        file = open("/pi/{}.txt".format(file_num), "a+")
        file.write("\n")
        file.close()
        i = 0
    if j == 1000:
        file_num += 1
        j = 0