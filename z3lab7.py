import numpy as np
tab = np.zeros((3, 3))

#tab[1:,:2] =1 #wycinek1
#tab[:, 2:] =1  #wycinek2
#tab[:2, 0] =1  #wycinek4
tab[:2, [0,2]] =1
print(tab)

