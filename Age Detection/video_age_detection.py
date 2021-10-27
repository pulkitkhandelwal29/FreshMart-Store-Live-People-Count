# -----------------------------
#   USAGE
# -----------------------------
# python video_age_detection.py --face face_detector --age age_detector --gender gender_detector

# -----------------------------
#   IMPORTS
# -----------------------------
# Import the necessary packages
from imutils.video import VideoStream,FileVideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import re
import os
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='freshmartstoredb')

cursor = cnx.cursor()


# -----------------------------
#   FUNCTIONS
# -----------------------------
def detect_and_predict_age(frame, faceNet, ageNet, genderNet, minConf=0.5):
    """
        Age detection and prediction function.
        :param frame: Input image frame
        :param faceNet: Face detection model
        :param ageNet: Age detection model
        :param genderNet: Gender detection model
        :param minConf: Minimum confidence probability
        :return: results with predictions
    """
    # Define the list of age buckets that the age predictor will predict
    AGE_BUCKETS = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]
    #List of genders
    gender_list = ['Male', 'Female']
    # Initialize the results list
    results = []
    # Grab the dimensions of the frame and then construct a blob from it
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    # Pass the blob through the network and obtain the face detections
    faceNet.setInput(blob)
    detections = faceNet.forward()
    # Loop over the detections
    for i in range(0, detections.shape[2]):
        # Extract the confidence (i.e, probability) associated with the prediction
        confidence = detections[0, 0, i, 2]
        # Filter out weak detections by ensuring the confidence is greater than the minimum confidence probability
        if confidence > minConf:
            # Compute the (x, y) coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            # Extract the ROI of the frame
            face = frame[startY:endY, startX:endX]
            # Ensure that the ROI is sufficiently large
            if face.shape[0] < 20 or face.shape[1] < 20:
                continue
            # Construct a blob from *just* the face ROI
            faceBlob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746),
                                             swapRB=False)
            # Make predictions on the age and find the age bucket with the largest corresponding probability
            ageNet.setInput(faceBlob)
            preds = ageNet.forward()
            i = preds[0].argmax()
            age = AGE_BUCKETS[i]
            ageConfidence = preds[0][i]
            
            # Make predictions on the gender
            genderNet.setInput(faceBlob)
            gender_preds = genderNet.forward()
            i = gender_preds[0].argmax()
            gender = gender_list[i]
            genderConfidence = gender_preds[0][i]

            age = re.sub(r'[()]','',age)
            min_age = age.split('-')[0]
            max_age = age.split('-')[1]

            details = ("INSERT INTO customer_details "
               "(gender,minimum_age,maximum_age) "
               "VALUES (%s, %s, %s)")

            record = (gender,min_age,max_age)
            cursor.execute(details, record)
            cnx.commit()

            print('data inserted')
            
            
            # Construct a dictionary consisting of both the face bounding box location along with the age prediction
            # then update the results list
            d = {
                "loc": (startX, startY, endX, endY),
                "age": (age),
                "gender":(gender),
            }
            results.append(d)
    # Return results to the calling function
    return results


# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="Path to face detector model directory")
ap.add_argument("-a", "--age", required=True, help="Path to age detector model directory")
ap.add_argument("-g", "--gender", required=True, help="Path to gender detector model directory")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="Minimum probability to filter weak detections")
args = vars(ap.parse_args())

# Load the serialized face detector model from disk
print("[INFO] Loading face detector model...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
weightsPath = os.path.sep.join([args["face"], "res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# Load the serialized age detector model from disk
print("[INFO] Loading age detector model...")
prototxtPath = os.path.sep.join([args["age"], "age_deploy.prototxt"])
weightsPath = os.path.sep.join([args["age"], "age_net.caffemodel"])
ageNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# Load the serialized gender detector model from disk
print("[INFO] Loading gender detector model...")
prototxtPath = os.path.sep.join([args["gender"], "deploy_gender.prototxt"])
weightsPath = os.path.sep.join([args["gender"], "gender_net.caffemodel"])
genderNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# Initialize the video stream and allow the camera sensor to warm up
print("[INFO] Starting video stream...")

#If video file, uncomment this
vs = FileVideoStream(path='store.mp4').start()

#If directly want to stream web camera, refer this line
# vs = VideoStream(0).start()

time.sleep(2.0)

# Loop over the frames from the video stream
while True:
    # Grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    # Detect the faces in the frame and for each face in the frame predict the age
    results = detect_and_predict_age(frame, faceNet, ageNet, genderNet, minConf=args["confidence"])
    # Loop over the face age detection results
    for r in results:
        # Draw the bounding box of the face along with the associated age
        (startX, startY, endX, endY) = r["loc"]
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
        #cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        overlay_text = "%s" % (r["gender"])
        cv2.putText(frame, overlay_text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    # Show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # If the 'q' key was pressed, break from the loop
    if key == ord("q"):
        break

# Do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
