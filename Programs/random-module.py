
# here random is a module

import random

random_int = random.randint(1, 50)
print(random_int)

# random_float = random.random() # this random() will get you floating point number between 0 to 1 by default
# print(random_float)            # not including 0 and 1


# how can you print the random float numbers between 0 to 5 (means, not including 0 and 5)

# that means from 0.00000000 ... to 4.9999999 (any random floating point number, if i divide it by 5 it will give me
# a return value till 4.9999999)

random_float = random.random()
print(random_float * 5)

