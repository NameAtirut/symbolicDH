import numpy as np
from modules.dh_convention import dhTransformAll

theta_list = [45,60,30]
d_list = [0,0,0]
alpha_list = [0,0,0]
a_list = [10,10,10]

result = dhTransformAll(theta_list, d_list, alpha_list, a_list)
result = result.astype(np.float16)
print(result)