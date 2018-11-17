from model import *
from temp import*
import cv2
# from prepare_dataset import *
# main()
from prepare_dataset_for_images import *
X_train,Y_train,names=prepare_dataset_for_images(1010,28,14,"C:/Users/pramesh/PycharmProjects/BODMASS/dataset/train/")#762
X_test,Y_test,names=prepare_dataset_for_images(220,28,14,"C:/Users/pramesh/PycharmProjects/BODMASS/dataset/test/")
X_train=X_train/255
X_test=X_test/255

model(X_train,Y_train,X_test,Y_test,names)