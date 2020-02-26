# Pi-Calculate
Calculate Math.Pi by python in Google Colab

[Notebook](https://colab.research.google.com/drive/1NcCpb8ic_oBXhi7gvdnc7tFGsMwgBgBN)

I use [Google Colab](https://colab.research.google.com/) to calculate Pi numbers just for fun.

> Pi Calculate Method from : [this](https://rosettacode.org/wiki/Pi#Python)    

a website talk about Pi : [link](http://www.math.com/tables/constants/pi.htm)    
to compare solutions, use [this](https://text-compare.com/) and [this](https://www.browserling.com/tools/remove-all-whitespace)

[pi_calculate.py](https://github.com/JuenTingShie/Pi-Calculate/blob/master/pi_calculate.py)
```pyhon
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
    sys.stdout.write(str(d))  # Comment this line to disable showing numbers
    i += 1
    j += 1
    ij += 1
    file = open("/pi/{}.txt".format(file_num), "a+")
    file.write(str(d))
    file.close()
    if ij == 10:  # Write a space ever 10 number
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
    if j == 1000:  # Change this to manage nambers in a single file
        file_num += 1
        j = 0
```

The result is :
> 1. Each file cost 1 minute to output to google drive
> 2. Research I found online claim that Google Colab will keep calculate for 12hr, but I only get 333 files and it only run 3hr(2020/02/25-20:47 to 2020/02/26-01:16)