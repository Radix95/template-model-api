
import numpy as np

feat1 = np.asarray([0, 1, 2, 3])
feat2 = np.asarray([1, 2, 3, 4])
feat3 = np.asarray([2, 3, 4, 5])

feats = np.asarray([feat1, feat2, feat3]).T

for feat in feats:
    print(feat)   
    for f in feat:
        print(f)   

#print(np.reshape(feat, (-1,3)))