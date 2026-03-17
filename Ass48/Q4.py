import numpy as np
from sklearn.preprocessing import StandardScaler

p1 = np.array([25, 20000])
p2 = np.array([35, 80000])

# Before scaling
dist_before = np.linalg.norm(p1 - p2)

# After scaling
scaler = StandardScaler()
data = np.array([p1, p2])
scaled = scaler.fit_transform(data)

dist_after = np.linalg.norm(scaled[0] - scaled[1])

print("Distance before scaling:", dist_before)
print("Distance after scaling:", dist_after)