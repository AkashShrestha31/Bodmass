import numpy as np
from scipy import ndimage
path = "C:/Users/pramesh/PycharmProjects/BODMASS/dataset/pics/samp3.jpg"
image=np.array(ndimage.imread(path,flatten=False))
print(image.shape)
