# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i]
# bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses
# some pile of bananas and eats k bananas from that pile. If the pile has less than k 
# bananas, she eats all of them instead and will not eat any more bananas during
# this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before
# the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

from time import time

# piles = [3,6,7,11]
# h = 8
# # output: 4

# piles = [30,11,23,4,20]
# h = 5
# # output: 30

piles = [30,11,23,4,20]
h = 6
# output: 23


def minEatingSpeed(piles: list[int], h: int) -> int:
    start = time()
    min_k = sum(piles)//h
    max_k = max(piles)
    ks = [k for k in range(min_k, max_k + 1)] 
    l = 0
    r = len(ks) - 1
    p1 = time()
    print('SETTING VARIABLES: ', p1 - start)

    while l <= r:
        m = (l + r)//2
        hours = h
        
        for banans in piles:
            if banans % ks[m] == 0:
                hours -= banans/ks[m]
            else:
                hours -= (banans//ks[m]) + 1
        p2 = time()
        print('DETERMINING HOURS: ', time() - start)

        zeros = []
        if hours < 0:
            l = m + 1
        elif hours > 0:
            r = m - 1
        else:
            zeros.append(ks[m])
            r -= 1
    print('APPENDING ZEROS: ', time() - start)
    return min(zeros)

minEatingSpeed(piles, h)