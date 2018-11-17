#SLIDING WINDOW TEST
import numpy as np
from numpy import *
from scipy import ndimage
import scipy.misc
import matplotlib.pyplot as plt
import cv2
def sliding(path):
	image=np.array(ndimage.imread(path,flatten=False))
	A_prev=scipy.misc.imresize(image,size=(300,500)).reshape(300,500,3)
	x1=10
	y1=260
	x2=10
	y2=150
	for i in range(3):
					a_slice=A_prev[x1:y1,x2:y2,:]
					x2=x2+160
					y2=y2+200
					# plt.imshow(a_slice)
					# plt.show()
					a_slice=cv2.cvtColor(a_slice, cv2.COLOR_BGR2RGB)
					cv2.imwrite("C:/Users/pramesh/PycharmProjects/BODMASS/capture/samp"+str(i+1)+".jpg",a_slice)
					if cv2.waitKey=='q':
						cv2.destroyAllWindows()
# path="./dataset/compute/samp1.jpg"

# im=sliding(path)






