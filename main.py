import numpy as np
tab2=np.random.randint(low=0,high=50,size=(5,5))
print(tab2)
print("Maximum wartość",tab2.max())
print("Min wartość",tab2.min())
print("Maximum wartość wiersza",tab2.max(axis=1))
print("Maximum wartość kolumn",tab2.max(axis=0))
print("Min wartość wiersza",tab2.min(axis=1))
print("Min wartość kolumn",tab2.min(axis=0))
print(tab2.sum(axis=0))
print(tab2.sum(axis=1))

