import tensorflow as tf
from scipy import ndimage
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
import cv2
from sliding_window import sliding
stored_values=[]

def add(op1, op2):
	return op1+op2

def subtract(op1, op2):
	return op1-op2

def multiply(op1, op2):
	return op1*op2

def divide(op1, op2):
	return op1/op2

names=["zero","one","two", "three", "four", "five", "six","seven", "eight", "nine", "sum", "subtract", "product", "divide"]
sess=tf.Session() 
signature_key = tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
input_key = "images"
output_key = "scores"
export_path =  "./savemodel" 
meta_graph_def = tf.saved_model.loader.load(sess,[tf.saved_model.tag_constants.SERVING],export_path)
signature = meta_graph_def.signature_def

x_tensor_name = signature[signature_key].inputs[input_key].name
y_tensor_name = signature[signature_key].outputs[output_key].name

X = sess.graph.get_tensor_by_name(x_tensor_name)
Y = sess.graph.get_tensor_by_name(y_tensor_name)
path="./dataset/compute/samp1.jpg"
sliding(path)

#predict
for i in range(1,4):
		path = "C:/Users/pramesh/PycharmProjects/BODMASS/capture/"+"samp"+str(i)+".jpg"
		im=np.array(ndimage.imread(path,flatten=False))
		plt.imshow(im)
		try:
			if im.shape[2]==3:
				im=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		except:
			print("error")
		im=scipy.misc.imresize(im,size=(28,28)).reshape(1,28*28*1)
		im=np.reshape(im,(im.shape[0],28,28,1))
		y_out = sess.run(Y, {X: im})
		prediction=tf.argmax(y_out,1)
		value=np.squeeze(sess.run(prediction))
		# print(value)
		print(names[value],value)
		stored_values.append(value)
		plt.show()
print(stored_values[1])
result=""
if stored_values[1]==10:
	result=add(stored_values[0],stored_values[2])
if stored_values[1]==11:
	result=subtract(stored_values[0],stored_values[2])
if stored_values[1]==12:
	result=multiply(stored_values[0],stored_values[2])
if stored_values[1]==13:
	result=divide(stored_values[0],stored_values[2])
print("Resut is: ",result)

