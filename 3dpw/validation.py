import pickle
import numpy as np

file3 = ("G:/sequenceFiles/train/new/courtyard_arguing_00.pkl")
x = pickle.load(open(file3)) 
poses2d1 = x['poses2d']
print(x.keys())
print(x.keys())
x2 = np.array(poses2d1)
print(x2)
print(x2.shape)