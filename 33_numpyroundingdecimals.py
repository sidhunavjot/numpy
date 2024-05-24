# rounding decimals : there are 5 types of rounding off decimals in numpy: truncation, fix, rounding, floor, ceil.

# truncation : trunc() and fix()

# here we are truncating the below array, these commands remove the decimals and return the float number closest to zero

import numpy as np
x = np.trunc([-3.45323, 4.32456])
print(x)

# fix()

import numpy as np
x = np.fix([-3.45323, 4.32456])
print(x)

# rounding : the around() - this func increments preceding digit or decimal by nearest to 1 : if n>5 = 1 or n<=0

import numpy as np
x = np.around(-3.46623, 2)
print(x)

# floor() - round off decimals to their lower integer
import numpy as np
x = np.floor([-3.45323, 4.32456])
print(x)

# ceil() - round off to upper integer

import numpy as np
x = np.ceil([-3.45323, 4.32456])
print(x)

