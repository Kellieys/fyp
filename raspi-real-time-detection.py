import os
import cv2
import time
import imutils
import numpy as np
from imutils.video import VideoStream
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# function that detect face and determine mask wearing
def detection_prediction(window, predictFace, predictMask):

	# initialize list for face, location of face and predictions
	faces = []
	locs = []
	preds = []

	# construct a blob from the dimensions of the window
	(h, w) = window.shape[:2]
	blob = cv2.dnn.blobFromImage(window, 1.0, (224, 224),(104.0, 177.0, 123.0))

	# insert blob to the FacePrediction net
	predictFace.setInput(blob)
	detections = predictFace.forward()
	print("Face Detected:",detections.shape)

	# detection for loop
	for i in range(0, detections.shape[2]):
		# extract the probability associated with the current detection
		probability = detections[0, 0, i, 2]

		# ignore weak detection that is lower than 0.5
		if probability > 0.5:
			# compute the (x, y)-coordinates of the bounding box for the face
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# arrange the bounding boxes so that it fall within dimensions of the window
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extract the face ROI, convert it from BGR to RGB channel ordering, resize and preprocess
			face = window[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)

			# insert the face and bounding boxes to their respective lists
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	# if a face is detected, make prediction
	if len(faces) > 0:
		faces = np.array(faces, dtype="float32")
		preds = predictMask.predict(faces, batch_size=32)

	# return 2-tuple of the face locations and their corresponding locations
	return (locs, preds)


# pre-trained Caffe deep learning model provided by OpenCV to detect faces
#.prototxt file(s) define the model architecture (i.e., the layers themselves)
#.caffemodel file which contains the weights for the actual layers
prototxtPath = "/home/pi/COMP3025/opencv_facedetector/deploy.prototxt"
weightsPath = "/home/pi/COMP3025/opencv_facedetector/res10_300x300_ssd_iter_140000.caffemodel"
predictFace = cv2.dnn.readNet(prototxtPath, weightsPath)

# load in the face mask model that was traiend 
predictMask = load_model("/home/pi/COMP3025/trained_model/Real-person-dataset-model.model")

# initialize
print("[INFO] Starting Video Stream")
camera = VideoStream(src=0).start()

while True:
	# resize window to maximum width of 400 pixels
	window = camera.read()
	window = imutils.resize(window, width=400)

	# call function() for detection
	(locs, preds) = detection_prediction(window, predictFace, predictMask)

	# constantly updating the detected face locations
	for (box, pred) in zip(locs, preds):
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred

		# display bounding box and text according to class label
		label = "Mask" if mask > withoutMask else "No Mask"
		color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

		# format to 100% for predicted probability 
		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

		# output to window
		cv2.putText(window, label, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(window, (startX, startY), (endX, endY), color, 2)

	# display the output window
	cv2.imshow("Window", window)
	key = cv2.waitKey(1) & 0xFF

	# stop camera if q is pressed
	if key == ord("q"):
		break

# end window and camera 
cv2.destroyAllWindows()
camera.stop()