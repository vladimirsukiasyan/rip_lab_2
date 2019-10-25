#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['A', 'a', 'b', 'B']
[print(res) for res in Unique(data1, ignore_case=True)]
print(list(Unique(data3)))
# or
# [print(res) for res in Unique(data3, ignore_case=False)]
