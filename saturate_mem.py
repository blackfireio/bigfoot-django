import sys
import time

a = ["a"] * int(sys.argv[1])

for i in range(len(a)):
    time.sleep(1)
    print(i, a[i])
