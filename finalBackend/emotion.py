from config.definitions import CNN_DIR
from config.definitions import CV_FRONT_FACE
from config.definitions import IMG_SRC

def getEmotion():
    class_labels= {0: 'Angry', 1: 'Fear', 2: 'Happy', 3: 'Neutral', 4: 'Sad', 5: 'Surprise'}

    from keras.models import load_model

    classifier = load_model(CNN_DIR)

    from keras.models import load_model
    from keras.preprocessing import image
    import numpy as np
    import os
    import cv2
    import numpy as np
    from os import listdir
    from os.path import isfile, join
    from tensorflow.keras.utils import img_to_array

    face_classifier = cv2.CascadeClassifier(CV_FRONT_FACE)

    def face_detector(img):
        # Convert image to grayscale
        gray = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        if faces is ():
            return (0,0,0,0), np.zeros((48,48), np.uint8), img
        
        allfaces = []   
        rects = []
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation = cv2.INTER_AREA)
            allfaces.append(roi_gray)
            rects.append((x,w,y,h))
        return rects, allfaces, img

    img = cv2.imread(IMG_SRC)
    rects, faces, image = face_detector(img)

    i = 0
    for face in faces:
        roi = face.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        # make a prediction on the ROI, then lookup the class
        preds = classifier.predict(roi)[0]
        label = class_labels[preds.argmax()]   

        return label

