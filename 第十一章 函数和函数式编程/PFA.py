from operator import add , mul
from functools import partial
add1 = partial(add,1)      # add1(x) == add(1,x)
mul100 = partial(mul,100)  # mul100 == mul(100,x)

print add1 (10)
print mul100 (10)
